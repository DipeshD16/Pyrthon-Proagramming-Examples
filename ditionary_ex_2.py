''' For this problem, use the dictionary from the beginning of this chapter whose keys are month names and whose values are the number of days in the corresponding months. (a) Ask the user to enter a month name and use the dictionary to tell them how many days are in the month. (b) Print out all of the keys in alphabetical order. (c) Print out all of the months with 31 days. (d) Print out the (key-value) pairs sorted by the number of days in each month 11.5. EXERCISES 105 (e) Modify the program from part (a) and the dictionary so that the user does not have to know how to spell the month name exactly. That is, all they have to do is spell the first three letters of the month name correctly'''

month_days = {
    "January": 31,
    "February": 28,  # Not considering leap years here
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

# (a) Ask user to enter a month name (improved in part e)
user_input = input("Enter a month name or first three letters (e.g., Jan, February): ").capitalize()

# (e) Accept 3-letter input and handle spelling
month_found = None
for month in month_days:
    if month.lower().startswith(user_input.lower()):
        month_found = month
        break

if month_found:
    print(f"{month_found} has {month_days[month_found]} days.")
else:
    print("Month not recognized.")

print("\n(b) All months in alphabetical order:")
for month in sorted(month_days):
    print(month)

print("\n(c) Months with 31 days:")
for month, days in month_days.items():
    if days == 31:
        print(month)

print("\n(d) Months sorted by number of days:")
for month, days in sorted(month_days.items(), key=lambda item: item[1]):
    print(f"{month}: {days} days")