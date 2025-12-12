# TODO:
#  Rollercoaster Qualification & Charges
#     1. Check height
#        Verify if the person meets the minimum height requirement to qualify for the rollercoaster.
#     2. Check age and determine charge
#         If older than 18 → charge $12
#         If 18 or younger → charge $7
#     3. Check military service
#        Apply discount if the person serves in the military.


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

#services = input("have you serve or currently active military? ")


if height > 120:
    age = int(input("How old are you? "))
    if age > 18:
        print("Welcome, You pay $12")
    else:
        print("Welcome, You pay $7")
else:
    print("Sorry, You are not qualify")

