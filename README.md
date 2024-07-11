# Citrine

Vertically integrated accounting in the CLI.

## Problem

**There is a lack of integration between command-line accounting tools and large banks.** We are tired of Intuit's monopoly. Ledger and hledger are great, but we need something to pull bank records and easily account them for bookkeeping. We are looking for something sleek and easy to use.

## Solution

We are now building Citrine, a command-line tool that integrates with financial institutions to pull transaction records, help categorize them, and generate accounting records.

## Requirements

- Developer-first - should be easy to extend with APIs and plugins
- Secure - this project stores bank information and transaction records
- Good for company accounting for tech companies - we are the target audience

## UX Map

### Main Menu

1. Import Transactions
2. Categorize Transactions
3. Track Bills and Invoices
4. Generate Reports
5. Settings
6. Exit

### Import Transactions

1. Select Bank
2. Enter Credentials
3. Fetch Transactions
4. Store Transactions

### Categorize Transactions

1. View Uncategorized
2. Apply Rules/Manual
3. Bulk Categorization
4. Save Categorized

### Track Bills and Invoices

1. Add New Bill/Invoice
2. View Outstanding
3. Mark as Paid/Resolved

### Generate Reports

1. Select Report Type
2. Customize Report
3. Generate and View

### Settings

1. Bank Credentials
2. Categorization Rules
3. Other Preferences
4. Interactive Setup
5. Custom Scripts
