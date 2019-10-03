import math

budget = float(input())
capital = float(input())
number_of_investors = int(input())

collection_money = 0

for number_of_investors in range(1, number_of_investors + 1):
    money_given = float(input())

    collection_money += money_given
    enough_money = capital + collection_money
    print(f"Investor {number_of_investors} gave us {money_given:.2f}.")

    if enough_money >= budget:
        extra_money = enough_money - budget
        print(f"We will manage to build it. Start now! Extra money - {extra_money:.2f}.")
        break

if enough_money < budget:
    money = abs(enough_money - budget)
    print(f"Project can not start. We need {money:.2f} more.")