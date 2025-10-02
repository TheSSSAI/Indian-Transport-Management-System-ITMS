# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from odoo import fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class GspRequestMapper:
    """
    Transforms an Odoo 'account.move' record into a JSON-serializable dictionary
    that conforms to the GSP (GST Suvidha Provider) API's required schema for
    e-invoice generation.

    This class encapsulates the complex data transformation logic, isolating the
    rest of the application from the specific and potentially volatile structure
    of the external GSP API.
    """

    def __init__(self, env: models.api.Environment):
        """
        Initializes the mapper with the Odoo environment.

        :param env: The Odoo environment object.
        """
        self.env = env

    def map_invoice_to_gsp_payload(self, invoice: models.Model) -> dict:
        """
        Maps an Odoo invoice record to the GSP e-invoicing payload format.

        This method reads all necessary fields from the invoice and its related
        records (partner, invoice lines) and constructs a nested dictionary that
        matches the GSP's JSON structure.

        :param invoice: A single recordset of the 'account.move' model.
        :return: A dictionary representing the GSP JSON payload.
        :raises: ValueError if critical data required for the payload is missing.
        """
        invoice.ensure_one()
        _logger.debug("Starting GSP payload mapping for invoice: %s", invoice.name)

        seller = invoice.company_id
        buyer = invoice.partner_id

        if not seller.vat:
            raise ValueError("Seller GSTIN is not configured on the company profile.")
        if not buyer.vat:
            raise ValueError(f"Buyer GSTIN is missing for customer '{buyer.name}'.")

        # Main payload structure
        payload = {
            "Version": "1.1",
            "TranDtls": {
                "TaxSch": "GST",
                "SupTyp": "B2B",  # Assuming B2B for e-invoicing
                "RegRev": "N",
                "EcmGstin": None,
                "IgstOnIntra": "N",
            },
            "DocDtls": {
                "Typ": "INV",
                "No": invoice.name,
                "Dt": fields.Date.to_string(invoice.invoice_date),
            },
            "SellerDtls": {
                "Gstin": seller.vat,
                "LglNm": seller.name,
                "TrdNm": seller.name,
                "Addr1": seller.street or "",
                "Addr2": seller.street2 or "",
                "Loc": seller.city or "",
                "Pin": int(seller.zip) if seller.zip and seller.zip.isdigit() else 0,
                "Stcd": seller.state_id.code if seller.state_id else "",
                "Ph": seller.phone or "",
                "Em": seller.email or "",
            },
            "BuyerDtls": {
                "Gstin": buyer.vat,
                "LglNm": buyer.name,
                "TrdNm": buyer.name,
                "Pos": buyer.state_id.code if buyer.state_id else "",
                "Addr1": buyer.street or "",
                "Addr2": buyer.street2 or "",
                "Loc": buyer.city or "",
                "Pin": int(buyer.zip) if buyer.zip and buyer.zip.isdigit() else 0,
                "Stcd": buyer.state_id.code if buyer.state_id else "",
                "Ph": buyer.phone or "",
                "Em": buyer.email or "",
            },
            "ItemList": self._build_item_list(invoice),
            "ValDtls": {
                "AssVal": invoice.amount_untaxed,
                "CgstVal": invoice.amount_by_group[0][1] if len(invoice.amount_by_group) > 0 else 0.0,
                "SgstVal": invoice.amount_by_group[1][1] if len(invoice.amount_by_group) > 1 else 0.0,
                "IgstVal": invoice.amount_by_group[0][1] if seller.state_id != buyer.state_id else 0.0,
                "CesVal": 0.0,  # Assuming no CESS for now
                "StCesVal": 0.0,
                "OthChrg": 0.0,
                "TotInvVal": invoice.amount_total,
                "RndOffAmt": round(invoice.amount_total - sum(line.price_total for line in invoice.invoice_line_ids), 2)
            },
            "EwbDtls": None, # E-Way Bill details are out of scope for this implementation
        }
        
        # Adjust tax values based on Inter-state or Intra-state
        is_inter_state = seller.state_id != buyer.state_id
        if is_inter_state:
            payload['ValDtls']['CgstVal'] = 0.0
            payload['ValDtls']['SgstVal'] = 0.0
            payload['ValDtls']['IgstVal'] = invoice.amount_tax
        else:
            # Simple assumption for CGST/SGST split. Odoo's amount_by_group is more reliable
            # but can be complex to parse robustly. This is a common approach.
            tax_groups = invoice.amount_by_group
            cgst = sum(group[1] for group in tax_groups if 'CGST' in group[0])
            sgst = sum(group[1] for group in tax_groups if 'SGST' in group[0])
            payload['ValDtls']['CgstVal'] = cgst
            payload['ValDtls']['SgstVal'] = sgst
            payload['ValDtls']['IgstVal'] = 0.0


        _logger.info("Successfully mapped invoice %s to GSP payload.", invoice.name)
        return payload

    def _build_item_list(self, invoice: models.Model) -> list:
        """
        Constructs the 'ItemList' part of the GSP payload from invoice lines.

        :param invoice: A single recordset of the 'account.move' model.
        :return: A list of dictionaries, each representing an item line.
        :raises: ValueError if an item line is missing a HSN code or has invalid tax data.
        """
        item_list = []
        for index, line in enumerate(invoice.invoice_line_ids.filtered(lambda l: not l.display_type), 1):
            if not line.product_id:
                raise ValueError(f"Invoice line '{line.name}' is not linked to a product.")

            hsn_code = line.product_id.l10n_in_hsn_code
            if not hsn_code:
                raise ValueError(f"Product '{line.product_id.name}' is missing a HSN code.")

            tax_info = self._get_tax_info(line)

            item = {
                "SlNo": str(index),
                "PrdDesc": line.name,
                "IsServc": "Y" if line.product_id.type == 'service' else "N",
                "HsnCd": hsn_code,
                "Qty": line.quantity,
                "Unit": line.product_uom_id.name if line.product_uom_id else "NOS",
                "UnitPrice": line.price_unit,
                "TotAmt": line.price_subtotal,
                "AssAmt": line.price_subtotal,
                "GstRt": tax_info.get('rate', 0.0),
                "IgstAmt": tax_info.get('igst', 0.0),
                "CgstAmt": tax_info.get('cgst', 0.0),
                "SgstAmt": tax_info.get('sgst', 0.0),
                "CesRt": 0.0,
                "CesAmt": 0.0,
                "CesNonAdvlAmt": 0.0,
                "TotItemVal": line.price_total,
            }
            item_list.append(item)
        
        if not item_list:
            raise ValueError("Invoice must have at least one valid item line.")
            
        return item_list

    def _get_tax_info(self, line: models.Model) -> dict:
        """
        Extracts tax rates and amounts for a given invoice line.

        :param line: A single recordset of 'account.move.line'.
        :return: A dictionary containing tax details {rate, igst, cgst, sgst}.
        """
        tax_info = {'rate': 0.0, 'igst': 0.0, 'cgst': 0.0, 'sgst': 0.0}
        
        if not line.tax_ids:
            return tax_info

        # This assumes a simple tax setup. For complex scenarios, this logic might need adjustment.
        tax = line.tax_ids[0] # Assuming one tax per line for simplicity
        tax_info['rate'] = tax.amount

        is_inter_state = line.move_id.company_id.state_id != line.move_id.partner_id.state_id
        
        if is_inter_state:
            tax_info['igst'] = line.price_total - line.price_subtotal
        else:
            # Assuming tax is split evenly for CGST/SGST if not IGST
            tax_info['cgst'] = (line.price_total - line.price_subtotal) / 2
            tax_info['sgst'] = (line.price_total - line.price_subtotal) / 2
            
        return tax_info