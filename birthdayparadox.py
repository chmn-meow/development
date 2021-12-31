import datetime, random


def get_birthdays(num_of_bdays):
    birthdays = []
    for i in range(num_of_bdays):
        start_of_year = datetime.date(2001, 1, 1)

        random_number_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_days
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, bday_a in enumerate(birthdays):
        for b, bday_b in enumerate(birthdays[a + 1 :]):
            if bday_a == bday_b:
                return bday_a


print(
    """
***Translated from Python2***\n\r
Welcome to Birthday Paradox!!!

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random 
simulations) to explore this concept.

(It's not actually a paradox, just a really surprising result.)
"""
)

MONTHS = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)

while True:
    print("How many birthdays shall we generate? (Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        num_b_days = int(response)
        break

print()

print(f"Here are {str(num_b_days)} birthdays:")
birthdays = get_birthdays(num_b_days)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(", ", end="")
    month_name = MONTHS[birthday.month - 1]
    date_text = f"{month_name} {birthday.day}"
    print(date_text, end="")
print()
print()

match = get_match(birthdays)

print("In this simulation, ", end="")
if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = f"{month_name} {match.day}"
    print("multiple people have a birthday on", date_text)
else:
    print("there are no matching birthdays.")

print(f"Generating {str(num_b_days)} random birthdays 1,000,000 times...")
input("Press enter to begin...")

print("Let's run another 1,000,000 simulations.")
sim_match = 0  # how many simulations had matching birthdays in them
for i in range(1_000_000):
    # report on the progress every 10,000 sims:
    if i % 100_000 == 0:
        print(f"{i} simulations run so far...")
    birthdays = get_birthdays(num_b_days)
    if get_match(birthdays) != None:
        sim_match += 1
print("1,000,000 simulations have now been run.")

probability = round(sim_match / 1_000_000 * 100, 2)
print(f"Out of 1,000,000 simulations of {str(num_b_days)} people, there was a")
print(f"matching birthday in that group {sim_match} times. This means")
print(f"that {str(num_b_days)} people have a {str(probability)}% chance of")
print("having a matching birthday in their group.")
print("That's probably higher than what you'd assume!")
