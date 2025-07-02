# Weight Converter

# Input for weight variable. Converted to floating point number
weight = float(input("Enter weight: "))

# Input for user to choose either kilos or pounds
unit = input("kg or lbs?: ")

# If statement to check for valid unit entry
if unit == "kg":
    # the kg to lbs conversion
    weight = weight * 2.205
    # Update unit variable so it's passed to the converted weight f string properly
    unit = "lbs"
    # Print statement within if statement so stop output being shown if wrong unit is typed
    print(f"Converted weight is: {round(weight, 2)}{unit}")
elif unit == "lbs":
    weight = weight / 2.205
    unit = "kg"
    print(f"Converted weight is: {round(weight, 2)}{unit}")
else:
    print(f"{unit} is not either kg or lbs, please choose one of those.")
