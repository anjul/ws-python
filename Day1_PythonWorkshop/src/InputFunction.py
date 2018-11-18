# Learn about input function, allow user to ask a input and return a string

name = raw_input("How May I address you?")
weight = raw_input("Please input your weight")
height = raw_input("Please input your height")

weight = float(weight)
height = float(height)

bmi = weight / (height/100) **2

print("You are ", name, "and your BMI is ",bmi)