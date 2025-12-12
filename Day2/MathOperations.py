
addition = 1 +1
substruction = 2-1
multiplication = 2*2
division = 4/2  # this always gives us a floating number to remove floating number use double //
power = 2**2

print(addition)
print(substruction)
print(multiplication)
print(division)  # this will print 2.0
print(4//2)  # this will print only 2 but this is also not suitable for any reminders so we have to careful when we use divisions
print(power)
print(3**2)

# PEMDAS
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

# 1. What is the output of this code?
print(3 * 3 + 3 / 3 - 3)

#PAUSE 2. Change the code so it outputs 3?
print(3 * (3 + 3 / 3 - 3))


#Assignment Operators
score = 0

score +=1   # increment by 1
score -=1   # decrement  by 1
score *=1   # multiply by 1
score /=1  # divide by 1

#f string : is a way to add multiple values when you print multiple values

print(f"your score is {score}, addition value is {addition}")

