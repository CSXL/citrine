import csv
from datetime import datetime
from decimal import Decimal

from beancount.core import data
from beancount.core.number import D
from beancount.core.amount import Amount
from beancount.ingest import importer

class PayPal(importer.ImporterProtocol):
    def __init__(self, account):
        self.account = account

    def name(self):
        return "PayPal"

    def identify(self, file):
        return file.name.endswith('.csv')

    def file_account(self, file):
        return self.account

    def extract(self, file, existing_entries=None):
        entries = []
        with open(file.name) as f:
            reader = csv.DictReader(f)
            for index, row in enumerate(reader):
                date = datetime.strptime(row['Date'], "%m/%d/%Y").date()
                description = row['Description']
                amount_str = row['Amount'].replace('$', '').replace(',', '')
                amount = D(amount_str)
                meta = data.new_metadata(file.name, index)
                entry = data.Transaction(
                    meta,
                    date,
                    '*',
                    row['Name'],
                    description,
                    data.EMPTY_SET,
                    data.EMPTY_SET,
                    [
                        data.Posting(self.account, Amount(amount, 'USD'), None, None, None, None),
                    ],
                )
                entries.append(entry)
        return entries


class ProvidentCUImporter(importer.ImporterProtocol):
    def __init__(self, account):
        self.account = account

    def name(self):
        return "ProvidentCUImporter"

    def identify(self, file):
        return file.name.endswith('.csv')

    def file_account(self, file):
        return self.account

    def extract(self, file, existing_entries=None):
        entries = []
        with open(file.name) as f:
            reader = csv.DictReader(f)
            for index, row in enumerate(reader):
                date = datetime.strptime(row['Date'], "%m/%d/%Y").date()
                description = row['Description']
                amount_str = row['Amount'].replace('$', '').replace(',', '')
                amount = D(amount_str)
                meta = data.new_metadata(file.name, index)
                entry = data.Transaction(
                    meta,
                    date,
                    '*',
                    description,
                    row['Comments'],
                    data.EMPTY_SET,
                    data.EMPTY_SET,
                    [
                        data.Posting(self.account, Amount(amount, 'USD'), None, None, None, None),
                    ],
                )
                entries.append(entry)
        return entries

class WellsFargoImporter(importer.ImporterProtocol):
    def __init__(self, account):
        self.account = account

    def name(self):
        return "WellsFargoImporter"

    def identify(self, file):
        return file.name.endswith('.csv')

    def file_account(self, file):
        return self.account

    def extract(self, file, existing_entries=None):
        entries = []
        with open(file.name) as f:
            reader = csv.DictReader(f)
            for index, row in enumerate(reader):
                date = datetime.strptime(row['Date'], "%m/%d/%Y").date()
                description = row['Description']
                amount_str = row['Amount'].replace('$', '').replace(',', '')
                amount = D(amount_str)
                meta = data.new_metadata(file.name, index)
                entry = data.Transaction(
                    meta,
                    date,
                    '*',
                    description,
                    "",
                    data.EMPTY_SET,
                    data.EMPTY_SET,
                    [
                        data.Posting(self.account, Amount(amount, 'USD'), None, None, None, None),
                    ],
                )
                entries.append(entry)
        return entries

CONFIG = [
    #ProvidentCUImporter('Assets:US:ProvidentCU:Checking'),
    #WellsFargoImporter('Assets:US:WellsFargo:Checking'),
    PayPal('Assets:US:PayPal'),
]