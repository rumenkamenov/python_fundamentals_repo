n = int(input())
salary = int(input())

price_facebook = 150
price_instagram = 100
price_redit = 50
current_website = None

for i in range(n):
    current_website = input()
    if current_website == "Facebook":
        salary -= price_facebook
    elif current_website == "Instagram":
        salary -= price_instagram
    elif current_website == "Reddit":
        salary -= price_redit
    if salary <= 0:
        print('You have lost your salary.')
        break
else:
    print(salary)