# TODO:
#     BMI Calculator
#     The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight.
#     This is the formula used to calculate it:
#     bmi is equal to the person's weight divided by the person's height squared.
from math import floor

height = float(input("What is your height? "))
weight = int(input("what is your weight? "))
bmi = weight /height**2

print(round(bmi,2))
print(floor(bmi))  # is round the nearest nimber