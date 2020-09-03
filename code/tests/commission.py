admit = input("What's the profit this year?\n:")
while admit.isdigit() == 0:
    admit = input("Please input digit.\n:")
profit = float(admit)
if profit <= 100000:
    profit = profit * 0.1
elif 200000 >= profit > 100000:
    profit = 10000 + (profit - 100000) * 0.075
elif 400000 >= profit > 200000:
    profit = 17500 + (profit - 200000) * 0.05
elif 600000 >= profit > 400000:
    profit = 27500 + (profit - 400000) * 0.03
elif 1000000 >= profit > 600000:
    profit = 33500 + (profit - 600000) * 0.015
else:
    profit = 39500 + (profit - 1000000) * 0.01
print("You can get", profit, "Yuan's bonus")
