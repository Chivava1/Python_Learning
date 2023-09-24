curr_UAH_to_USD = 0.027
curr_USD_to_UAH = 36.56
curr_UAH_to_EUR = 0.025
curr_EUR_to_UAH = 39.28

usd_amount = float(input("US to sell: "))
uah_equivalent = usd_amount * curr_USD_to_UAH
print(f"You sold {usd_amount} USD. You got {uah_equivalent} UAH.")

uah_amount = float(input("UAH to sell: "))
us_equivalent = uah_amount * curr_UAH_to_USD
print(f"You sold {uah_amount} UAH. You got {us_equivalent} USD")

eur_amount = float(input("EUR to sell: "))
eur_equivalent = eur_amount * curr_EUR_to_UAH
print(f"You sold {eur_amount} EUR. You got {eur_equivalent} UAH")

uah_amount = float(input("UAH to sell: "))
UA_to_EUR_equivalent = uah_amount * curr_UAH_to_EUR
print(f"You sold {uah_amount} UAH. You got {UA_to_EUR_equivalent} EUR.")

