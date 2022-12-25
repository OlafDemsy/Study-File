from datetime import date
now = date.today()
date = now.strftime("%Y")
year = input("Take a guess which year is this: ")
if year == date:
    print("Wow,your memorry is strong")
else:
    print("Dumb,Are u seriously?")