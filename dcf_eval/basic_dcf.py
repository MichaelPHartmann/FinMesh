import pandas
import numpy

def free_cash(ticker):
    income_statement(ticker)
    cash_flow(ticker)
    netincome = loc()
    totalInvestingcashFlows = loc()
    return netIncome - totalInvestingcashFlows

def cost_of_capital(ticker):
    #risk free rate
    #Equity Risk Premium
    #beta
    #Default Spread
    #Debt
    #Equity
    #Tax Rate
    income_statement(ticker)
    balance_sheet(ticker)
    risk_of_debt = (riskfree + ERP)*beta
    risk_of_equity = (riskfree + defaultspread)


def basic_dcf_valuation(ticker):
    return free_cash/cost_of_capital
