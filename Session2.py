#ROHAN SAREEN
#SESSION 2
#EXERCISE 1-3
print("\n----------EXERCISE 1-3 ----------\n")
# Exercise 1: Communicating with users
print("\nEXERCISE 1:\n")
name = input("What is your name? ")
print(f"Hello, {name}!\n")
age = int(input("How old are you? "))
print(f"{age*12} months old.\n")


# Exercise 2: Nearby Friends
print("\nEXERCISE 2:\n")
nearby_people = {'Saurabh', 'Jen', 'Anna'}
user_friends = set()
appended_name = input("What is your friend's name? ")
user_friends.add(appended_name)
print(user_friends)
print(nearby_people.intersection(user_friends))

# Exercise 3: Dictionaries
print("\nEXERCISE 3:\n")
lottery_numbers = {13, 21, 22, 5, 8}

playerOne = {
    'name': 'Ro',
    'numbers': {11, 21, 13, 45, 5},
}

playerTwo = {
    'name': 'Han',
    'numbers': {5, 22, 31, 44, 8, 2, 3, 65, 1, 0}
}

print(f"{playerOne['name']}: {lottery_numbers.intersection(playerOne['numbers'])} are matching numbers!")
print(f"{playerTwo['name']}: {lottery_numbers.intersection(playerTwo['numbers'])} are matching numbers!")