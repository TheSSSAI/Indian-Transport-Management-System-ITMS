module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: ['eslint:recommended', 'prettier'],
  plugins: ['prettier'],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  globals: {
    odoo: 'readonly',
  },
  rules: {
    'prettier/prettier': 'error',
    'no-unused-vars': [
      'warn',
      { args: 'after-used', argsIgnorePattern: '^_' },
    ],
  },
};