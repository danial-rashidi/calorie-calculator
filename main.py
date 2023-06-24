def calculate_calories(gender, age, height, weight):
    if gender == "m" or gender == "male":
        calories_needed = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
    elif gender == "f" or gender == "female":
        calories_needed = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)
    else:
        return "Please try again..."
    return int(calories_needed)

print("Welcome to Calorie Calculator\n")

gender_input = input("Gender (m/f): ").lower()
print()

try:
    age_input = int(input("Age: "))
    height_input = int(input("Height (cm): "))
    weight_input = int(input("Weight (kg): "))
    print("----------")
    result = calculate_calories(gender_input, age_input, height_input, weight_input)
    if isinstance(result, int):
        print(f"You need {result} calories per day")
    else:
        print(result)
except ValueError:
    print("Please enter an integer for age, height, and weight.")