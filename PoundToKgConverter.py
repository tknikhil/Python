weight_In_Pound = input("What is your weight in lbs ? ")
print(type(weight_In_Pound))
weight_In_Kg = float(weight_In_Pound) / 2.2046
print(type(weight_In_Kg))
""" Here I was getting Error Every time because the value which we are getting was in float and Python don't understand
 how to concatenate float and String so we have to TypeCast the value to String to display"""
print("Your weight in Kg is :" + str(weight_In_Kg))
