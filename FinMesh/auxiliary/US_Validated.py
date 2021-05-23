import requests

ALL_US_EQUITIES = "https://raw.githubusercontent.com/JerBouma/FinanceDatabase/master/Database/Equities/Countries/United%20States/United%20States.json"


US_EQUITIES = requests.get(ALL_US_EQUITIES).text
EVAL_US_EQUITIES = eval(US_EQUITIES)
print(type(EVAL_US_EQUITIES))
