"""
Django Ledger created by Miguel Sanda <msanda@arrobalytics.com>.
Copyright© EDMA Group Inc licensed under the GPLv3 Agreement.

Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
"""

import sys
from collections import defaultdict

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

mod = sys.modules[__name__]

# --- ASSET ROLES ----
# Current Assets ---
ASSET_CA_CASH = 'asset_ca_cash'
ASSET_CA_MKT_SECURITIES = 'asset_ca_mkt_sec'
ASSET_CA_RECEIVABLES = 'asset_ca_recv'
ASSET_CA_INVENTORY = 'asset_ca_inv'
ASSET_CA_UNCOLLECTIBLES = 'asset_ca_uncoll'
ASSET_CA_PREPAID = 'asset_ca_prepaid'
ASSET_CA_OTHER = 'asset_ca_other'

# Long Term Investments ---
ASSET_LTI_NOTES_RECEIVABLE = 'asset_lti_notes'
ASSET_LTI_LAND = 'asset_lti_land'
ASSET_LTI_SECURITIES = 'asset_lti_sec'

# Property, Plant & Equipment ---
ASSET_PPE_BUILDINGS = 'asset_ppe_build'
ASSET_PPE_BUILDINGS_ACCUM_DEPRECIATION = 'asset_ppe_build_accum_depr'
ASSET_PPE_EQUIPMENT = 'asset_ppe_equip'
ASSET_PPE_EQUIPMENT_ACCUM_DEPRECIATION = 'asset_ppe_equip_accum_depr'
ASSET_PPE_PLANT = 'asset_ppe_plant'
ASSET_PPE_PLANT_ACCUM_DEPRECIATION = 'asset_ppe_plant_depr'

# Intangible Assets ---
ASSET_INTANGIBLE_ASSETS = 'asset_ia'
ASSET_INTANGIBLE_ASSETS_ACCUM_AMORTIZATION = 'asset_ia_accum_amort'

# Other Asset Adjustments ---
ASSET_ADJUSTMENTS = 'asset_adjustment'

# LIABILITIES ----

# Current Liabilities
LIABILITY_CL_ACC_PAYABLE = 'lia_cl_acc_payable'
LIABILITY_CL_WAGES_PAYABLE = 'lia_cl_wages_payable'
LIABILITY_CL_TAXES_PAYABLE = 'lia_cl_taxes_payable'
LIABILITY_CL_INTEREST_PAYABLE = 'lia_cl_int_payable'
LIABILITY_CL_ST_NOTES_PAYABLE = 'lia_cl_st_notes_payable'
LIABILITY_CL_LTD_MATURITIES = 'lia_cl_ltd_mat'
LIABILITY_CL_DEFERRED_REVENUE = 'lia_cl_def_rev'
LIABILITY_CL_OTHER = 'lia_cl_other'

# Long Term Liabilities ---
LIABILITY_LTL_NOTES_PAYABLE = 'lia_ltl_notes'
LIABILITY_LTL_BONDS_PAYABLE = 'lia_ltl_bonds'
LIABILITY_LTL_MORTGAGE_PAYABLE = 'lia_ltl_mortgage'

# EQUITY ----
EQUITY_CAPITAL = 'eq_capital'
EQUITY_ADJUSTMENT = 'eq_adjustment'
EQUITY_COMMON_STOCK = 'eq_stock_common'
EQUITY_PREFERRED_STOCK = 'eq_stock_preferred'
EQUITY_DIVIDENDS = 'eq_dividends'

INCOME_OPERATIONAL = 'in_operational'
INCOME_INVESTING = 'in_passive'
INCOME_CAPITAL_GAIN_LOSS = 'in_gain_loss'
INCOME_INTEREST = 'in_interest'
INCOME_OTHER = 'in_other'

COGS = 'ex_cogs'

EXPENSE_REGULAR = 'ex_regular'
EXPENSE_CAPITAL = 'ex_capital'
EXPENSE_DEPRECIATION = 'ex_depreciation'
EXPENSE_AMORTIZATION = 'ex_amortization'
EXPENSE_TAXES = 'ex_taxes'
EXPENSE_INTEREST = 'ex_interest'
EXPENSE_OTHER = 'ex_other'

# ------> ROLE GROUPS <-------#

# ASSET GROUPS...
GROUP_QUICK_ASSETS = [
    ASSET_CA_CASH,
    ASSET_CA_MKT_SECURITIES
]

GROUP_CURRENT_ASSETS = [
    ASSET_CA_CASH,
    ASSET_CA_MKT_SECURITIES,
    ASSET_CA_INVENTORY,
    ASSET_CA_RECEIVABLES,
    ASSET_CA_PREPAID,
    ASSET_CA_OTHER
]

GROUP_NON_CURRENT_ASSETS = [
    ASSET_LTI_NOTES_RECEIVABLE,
    ASSET_LTI_LAND,
    ASSET_LTI_SECURITIES,
    ASSET_PPE_BUILDINGS,
    ASSET_PPE_BUILDINGS_ACCUM_DEPRECIATION,
    ASSET_PPE_EQUIPMENT,
    ASSET_PPE_EQUIPMENT_ACCUM_DEPRECIATION,
    ASSET_PPE_PLANT,
    ASSET_PPE_PLANT_ACCUM_DEPRECIATION,
    ASSET_INTANGIBLE_ASSETS,
    ASSET_INTANGIBLE_ASSETS_ACCUM_AMORTIZATION,
    ASSET_ADJUSTMENTS
]

GROUP_ASSETS = GROUP_CURRENT_ASSETS + GROUP_NON_CURRENT_ASSETS

# LIABILITY GROUPS....
GROUP_CURRENT_LIABILITIES = [
    LIABILITY_CL_ACC_PAYABLE,
    LIABILITY_CL_DEFERRED_REVENUE,
    LIABILITY_CL_INTEREST_PAYABLE,
    LIABILITY_CL_LTD_MATURITIES,
    LIABILITY_CL_OTHER,
    LIABILITY_CL_ST_NOTES_PAYABLE,
    LIABILITY_CL_WAGES_PAYABLE
]

GROUP_LT_LIABILITIES = [
    LIABILITY_LTL_NOTES_PAYABLE,
    LIABILITY_LTL_BONDS_PAYABLE,
    LIABILITY_LTL_MORTGAGE_PAYABLE,
]

GROUP_LIABILITIES = GROUP_CURRENT_LIABILITIES + GROUP_LT_LIABILITIES

# CAPITAL/EQUITY...
GROUP_CAPITAL = [
    EQUITY_CAPITAL,
    EQUITY_COMMON_STOCK,
    EQUITY_PREFERRED_STOCK,
    EQUITY_ADJUSTMENT
]

GROUP_INCOME = [
    INCOME_OPERATIONAL,
    INCOME_INVESTING,
    INCOME_INTEREST,
    INCOME_CAPITAL_GAIN_LOSS,
    INCOME_OTHER,
]

GROUP_EXPENSES = [
    COGS,
    EXPENSE_REGULAR,
    EXPENSE_INTEREST,
    EXPENSE_TAXES,
    EXPENSE_CAPITAL,
    EXPENSE_DEPRECIATION,
    EXPENSE_AMORTIZATION,
    EXPENSE_OTHER
]

GROUP_EXPENSES_NO_COGS = [
    EXPENSE_REGULAR,
    EXPENSE_INTEREST,
    EXPENSE_TAXES,
    EXPENSE_CAPITAL,
    EXPENSE_DEPRECIATION,
    EXPENSE_AMORTIZATION,
    EXPENSE_OTHER
]

GROUP_NET_PROFIT = [
    INCOME_OPERATIONAL,
    INCOME_INVESTING,
    INCOME_INTEREST,
    INCOME_CAPITAL_GAIN_LOSS,
    INCOME_OTHER,
    COGS
]

GROUP_GROSS_PROFIT = [
    INCOME_OPERATIONAL,
    COGS
]

GROUP_NET_SALES = [
    INCOME_OPERATIONAL,
    INCOME_INVESTING
]

GROUP_PPE_ACCUM_DEPRECIATION = [
    ASSET_PPE_BUILDINGS_ACCUM_DEPRECIATION,
    ASSET_PPE_EQUIPMENT_ACCUM_DEPRECIATION,
    ASSET_PPE_PLANT_ACCUM_DEPRECIATION
]

GROUP_EXPENSE_DEP_AND_AMT = [
    EXPENSE_DEPRECIATION,
    EXPENSE_AMORTIZATION
]

GROUP_EARNINGS = GROUP_INCOME + GROUP_EXPENSES
GROUP_EQUITY = GROUP_CAPITAL + GROUP_EARNINGS
GROUP_LIABILITIES_EQUITY = GROUP_LIABILITIES + GROUP_EQUITY

GROUP_INVOICE = [ASSET_CA_CASH, ASSET_CA_RECEIVABLES, LIABILITY_CL_DEFERRED_REVENUE]
GROUP_BILL = [ASSET_CA_CASH, ASSET_CA_PREPAID, LIABILITY_CL_ACC_PAYABLE]

# ############# CASH FLOW STATEMENT GROUPS...
GROUP_CFS_NET_INCOME = GROUP_EARNINGS

# ---> INVESTING ACTIVITIES <---- #
# Purchase of Assets....
GROUP_CFS_INV_PURCHASE_OR_SALE_OF_PPE = [
    ASSET_PPE_BUILDINGS,
    ASSET_PPE_PLANT,
    ASSET_PPE_EQUIPMENT
]
GROUP_CFS_INV_LTD_OF_PPE = [
    LIABILITY_LTL_NOTES_PAYABLE,
    LIABILITY_LTL_MORTGAGE_PAYABLE,
    LIABILITY_LTL_BONDS_PAYABLE
]
GROUP_CFS_INVESTING_PPE = GROUP_CFS_INV_PURCHASE_OR_SALE_OF_PPE + GROUP_CFS_INV_LTD_OF_PPE

# Purchase of Securities...
GROUP_CFS_INV_PURCHASE_OF_SECURITIES = [
    ASSET_CA_MKT_SECURITIES,
    ASSET_LTI_SECURITIES,
]
GROUP_CFS_INV_LTD_OF_SECURITIES = [
    LIABILITY_LTL_NOTES_PAYABLE,
    LIABILITY_LTL_BONDS_PAYABLE
]
GROUP_CFS_INVESTING_SECURITIES = GROUP_CFS_INV_PURCHASE_OF_SECURITIES + GROUP_CFS_INV_LTD_OF_SECURITIES

GROUP_CFS_INVESTING = GROUP_CFS_INVESTING_PPE + GROUP_CFS_INVESTING_SECURITIES

# ---> FINANCING ACTIVITIES <---- #
GROUP_CFS_FIN_ISSUING_EQUITY = [EQUITY_CAPITAL, EQUITY_COMMON_STOCK, EQUITY_PREFERRED_STOCK]
GROUP_CFS_FIN_DIVIDENDS = [EQUITY_DIVIDENDS]
GROUP_CFS_FIN_ST_DEBT_PAYMENTS = [LIABILITY_CL_ST_NOTES_PAYABLE]
GROUP_CFS_FIN_LT_DEBT_PAYMENTS = [LIABILITY_LTL_NOTES_PAYABLE]

GROUP_CFS_FINANCING = GROUP_CFS_FIN_ISSUING_EQUITY + GROUP_CFS_FIN_DIVIDENDS
GROUP_CFS_FINANCING += GROUP_CFS_FIN_ST_DEBT_PAYMENTS
GROUP_CFS_FINANCING += GROUP_CFS_FIN_LT_DEBT_PAYMENTS

# ---> INVESTING & FINANCING ACTIVITIES <---- #
GROUP_CFS_INVESTING_AND_FINANCING = GROUP_CFS_INVESTING + GROUP_CFS_FINANCING

# ---> OPERATING ACTIVITIES <---- #
# Non-Cash/Non-Current...
GROUP_CFS_OP_DEPRECIATION_AMORTIZATION = [
    EXPENSE_DEPRECIATION,
    EXPENSE_AMORTIZATION
]
GROUP_CFS_OP_INVESTMENT_GAINS = [
    INCOME_CAPITAL_GAIN_LOSS
]

# Non-Cash/Current...
GROUP_CFS_OP_ACCOUNTS_RECEIVABLE = [
    ASSET_CA_RECEIVABLES
]
GROUP_CFS_OP_INVENTORY = [
    ASSET_CA_INVENTORY
]
GROUP_CFS_OP_ACCOUNTS_PAYABLE = [
    LIABILITY_CL_ACC_PAYABLE
]
GROUP_CFS_OP_OTHER_CURRENT_ASSETS_ADJUSTMENT = [
    ASSET_CA_MKT_SECURITIES,
    ASSET_CA_PREPAID,
    ASSET_CA_UNCOLLECTIBLES,
    ASSET_CA_OTHER
]
GROUP_CFS_OP_OTHER_CURRENT_LIABILITIES_ADJUSTMENT = [
    LIABILITY_CL_WAGES_PAYABLE,
    LIABILITY_CL_INTEREST_PAYABLE,
    LIABILITY_CL_TAXES_PAYABLE,
    LIABILITY_CL_ST_NOTES_PAYABLE,
    LIABILITY_CL_LTD_MATURITIES,
    LIABILITY_CL_DEFERRED_REVENUE,
    LIABILITY_CL_OTHER,
]

ACCOUNT_ROLES = [
    ('Assets', (
        # CURRENT ASSETS ----
        (ASSET_CA_CASH, _('Current Asset')),
        (ASSET_CA_MKT_SECURITIES, _('Marketable Securities')),
        (ASSET_CA_RECEIVABLES, _('Receivables')),
        (ASSET_CA_INVENTORY, _('Inventory')),
        (ASSET_CA_UNCOLLECTIBLES, _('Uncollectibles')),
        (ASSET_CA_PREPAID, _('Prepaid')),
        (ASSET_CA_OTHER, _('Other Liquid Assets')),

        # LONG TERM INVESTMENTS ---
        (ASSET_LTI_NOTES_RECEIVABLE, _('Notes Receivable')),
        (ASSET_LTI_LAND, _('Land')),
        (ASSET_LTI_SECURITIES, _('Securities')),

        # PPE ...
        (ASSET_PPE_BUILDINGS, _('Buildings')),
        (ASSET_PPE_BUILDINGS_ACCUM_DEPRECIATION, _('Buildings - Accum. Depreciation')),
        (ASSET_PPE_PLANT, _('Plant')),
        (ASSET_PPE_PLANT_ACCUM_DEPRECIATION, _('Plant - Accum. Depreciation')),
        (ASSET_PPE_EQUIPMENT, _('Equipment')),
        (ASSET_PPE_EQUIPMENT_ACCUM_DEPRECIATION, _('Equipment - Accum. Depreciation')),

        # Other Assets ...
        (ASSET_INTANGIBLE_ASSETS, _('Intangible Assets')),
        (ASSET_INTANGIBLE_ASSETS_ACCUM_AMORTIZATION, _('Intangible Assets - Accum. Amortization')),
        (ASSET_ADJUSTMENTS, _('Other Assets')),
    )),
    ('Liabilities', (

        # CURRENT LIABILITIES ---
        (LIABILITY_CL_ACC_PAYABLE, _('Accounts Payable')),
        (LIABILITY_CL_WAGES_PAYABLE, _('Wages Payable')),
        (LIABILITY_CL_INTEREST_PAYABLE, _('Interest Payable')),
        (LIABILITY_CL_TAXES_PAYABLE, _('Taxes Payable')),
        (LIABILITY_CL_ST_NOTES_PAYABLE, _('Notes Payable')),
        (LIABILITY_CL_LTD_MATURITIES, _('Current Maturities of Long Tern Debt')),
        (LIABILITY_CL_DEFERRED_REVENUE, _('Deferred Revenue')),
        (LIABILITY_CL_OTHER, _('Other Liabilities')),

        # LONG TERM LIABILITIES ----
        (LIABILITY_LTL_NOTES_PAYABLE, _('Notes Payable')),
        (LIABILITY_LTL_BONDS_PAYABLE, _('Bonds Payable')),
        (LIABILITY_LTL_MORTGAGE_PAYABLE, _('Mortgage Payable')),
    )
     ),
    ('Equity', (

        # EQUITY ---
        (EQUITY_CAPITAL, _('Capital')),
        (EQUITY_COMMON_STOCK, _('Common Stock')),
        (EQUITY_PREFERRED_STOCK, _('Preferred Stock')),
        (EQUITY_ADJUSTMENT, _('Other Equity Adjustments')),
        (EQUITY_DIVIDENDS, _('Dividends & Distributions to Shareholders')),

        # INCOME ---
        (INCOME_OPERATIONAL, _('Operational Income')),
        (INCOME_INVESTING, _('Investing/Passive Income')),
        (INCOME_INTEREST, _('Interest Income')),
        (INCOME_CAPITAL_GAIN_LOSS, _('Capital Gain/Loss Income')),
        (INCOME_OTHER, _('Other Income')),

        # COGS ----
        (COGS, _('Cost of Goods Sold')),

        # EXPENSES ----
        (EXPENSE_REGULAR, _('Regular Expense')),
        (EXPENSE_INTEREST, _('Interest Expense')),
        (EXPENSE_TAXES, _('Tax Expense')),
        (EXPENSE_CAPITAL, _('Capital Expense')),
        (EXPENSE_DEPRECIATION, _('Depreciation Expense')),
        (EXPENSE_AMORTIZATION, _('Amortization Expense')),
        (EXPENSE_OTHER, _('Other Expense')),
    )
     )
]

ROLE_TUPLES = sum([[(r[0].lower(), s[0]) for s in r[1]] for r in ACCOUNT_ROLES], list())
ROLE_DICT = dict([(t[0].lower(), [r[0] for r in t[1]]) for t in ACCOUNT_ROLES])
VALID_ROLES = [r[1] for r in ROLE_TUPLES]
BS_ROLES = dict((r[1], r[0]) for r in ROLE_TUPLES)


def validate_roles(roles):
    if roles:
        if isinstance(roles, str):
            roles = [roles]
        for r in roles:
            if r not in VALID_ROLES:
                raise ValidationError('{rls}) is invalid. Choices are {ch}'.format(ch=', '.join(VALID_ROLES), rls=r))
    return roles


ROLES_VARS = locals().keys()
ROLES_DIRECTORY = dict()
ROLES_CATEGORIES = ['ASSET', 'LIABILITY', 'EQUITY', 'INCOME', 'COGS', 'EXPENSE']
for cat in ROLES_CATEGORIES:
    ROLES_DIRECTORY[cat] = [c for c in ROLES_VARS if c.split('_')[0] == cat]

ROLES_GROUPS = [g for g in ROLES_VARS if g.split('_')[0] == 'GROUP']

GROUPS_DIRECTORY = dict()
for group in ROLES_GROUPS:
    GROUPS_DIRECTORY[group] = getattr(mod, group)


class RoleManager:

    def __init__(self,
                 tx_digest: dict,
                 by_period: bool = False,
                 by_unit: bool = False):

        self.BY_PERIOD = by_period
        self.BY_UNIT = by_unit

        self.DIGEST = tx_digest
        self.ACCOUNTS = tx_digest['accounts']

        self.ROLES_ACCOUNTS = dict()
        self.ROLES_BALANCES = dict()

        if self.BY_PERIOD:
            self.ROLES_BALANCES_BY_PERIOD = defaultdict(lambda: dict())
        if self.BY_UNIT:
            self.ROLES_BALANCES_BY_UNIT = defaultdict(lambda: dict())
        if self.BY_PERIOD and self.BY_UNIT:
            self.ROLES_BALANCES_BY_PERIOD_AND_UNIT = defaultdict(lambda: dict())

        self.DIGEST['role_account'] = None
        self.DIGEST['role_balance'] = None
        self.DIGEST['role_balance_by_period'] = None

        self.DIGEST['group_account'] = None
        self.DIGEST['group_balance'] = None
        self.DIGEST['group_balance_by_period'] = None
        self.DIGEST['group_balance_by_unit'] = None
        self.DIGEST['group_balance_by_period_and_unit'] = None

    def digest(self):

        self.process_roles()
        self.DIGEST['role_account'] = self.ROLES_ACCOUNTS
        self.DIGEST['role_balance'] = self.ROLES_BALANCES

        if self.BY_PERIOD:
            self.DIGEST['role_balance_by_period'] = self.ROLES_BALANCES_BY_PERIOD
        if self.BY_UNIT:
            self.DIGEST['role_balance_by_unit'] = self.ROLES_BALANCES_BY_UNIT
        if self.BY_PERIOD and self.BY_UNIT:
            self.DIGEST['role_balance_by_period_and_unit'] = self.ROLES_BALANCES_BY_PERIOD_AND_UNIT

        return self.DIGEST

    def process_roles(self):

        for c, l in ROLES_DIRECTORY.items():
            for r in l:
                acc_list = list(acc for acc in self.ACCOUNTS if acc['role'] == getattr(mod, r))
                self.ROLES_ACCOUNTS[r] = acc_list
                self.ROLES_BALANCES[r] = sum(acc['balance'] for acc in acc_list)

                if self.BY_PERIOD:
                    for acc in acc_list:
                        per_key = (acc['period_year'], acc['period_month'])

                        self.ROLES_BALANCES_BY_PERIOD[per_key][r] = sum(acc['balance'] for acc in acc_list if all([
                            acc['period_year'] == per_key[0],
                            acc['period_month'] == per_key[1]]
                        )
                                                                        )


class GroupManager:

    def __init__(self,
                 tx_digest: dict,
                 by_period: bool = False,
                 by_unit: bool = False):

        self.BY_PERIOD = by_period
        self.BY_UNIT = by_unit
        self.DIGEST = tx_digest
        self.ACCOUNTS = tx_digest['accounts']

        self.GROUPS_ACCOUNTS = dict()
        self.GROUPS_BALANCES = dict()
        if self.BY_PERIOD:
            self.GROUPS_BALANCES_BY_PERIOD = defaultdict(lambda: dict())

        if self.BY_UNIT:
            self.GROUPS_BALANCES_BY_UNIT = defaultdict(lambda: dict())

        if self.BY_PERIOD and self.BY_UNIT:
            self.GROUPS_BALANCES_BY_PERIOD_AND_UNIT = defaultdict(lambda: dict())

        self.DIGEST['group_account'] = None
        self.DIGEST['group_balance'] = None
        self.DIGEST['group_balance_by_period'] = None
        self.DIGEST['group_balance_by_unit'] = None
        self.DIGEST['group_balance_by_period_and_unit'] = None

    def digest(self):

        self.process_groups()
        self.DIGEST['group_account'] = self.GROUPS_ACCOUNTS
        self.DIGEST['group_balance'] = self.GROUPS_BALANCES

        if self.BY_PERIOD:
            self.DIGEST['group_balance_by_period'] = self.GROUPS_BALANCES_BY_PERIOD
        if self.BY_UNIT:
            self.DIGEST['group_balance_by_unit'] = self.GROUPS_BALANCES_BY_UNIT
        if self.BY_PERIOD and self.BY_PERIOD:
            self.DIGEST['group_balance_by_period_and_unit'] = self.GROUPS_BALANCES_BY_PERIOD_AND_UNIT
        return self.DIGEST

    def get_accounts_generator(self, mod, g):
        return (acc for acc in self.ACCOUNTS if acc['role'] in getattr(mod, g))

    def process_groups(self):
        for g in ROLES_GROUPS:
            acc_list = list(self.get_accounts_generator(mod, g))
            self.GROUPS_ACCOUNTS[g] = acc_list
            self.GROUPS_BALANCES[g] = sum(acc['balance'] for acc in acc_list)

            if self.BY_PERIOD:
                for acc in acc_list:
                    per_key = (acc['period_year'], acc['period_month'])
                    self.GROUPS_BALANCES_BY_PERIOD[per_key][g] = sum(
                        acc['balance'] for acc in acc_list if all([
                            acc['period_year'] == per_key[0],
                            acc['period_month'] == per_key[1]]
                        ))

            if self.BY_UNIT:
                for acc in acc_list:
                    per_key = (acc['unit_uuid'],)
                    self.GROUPS_BALANCES_BY_UNIT[per_key][g] = sum(
                        acc['balance'] for acc in acc_list if acc['unit_uuid'] == per_key[0]
                    )
