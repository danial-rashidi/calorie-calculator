def calculate_calories(gender, age, height, weight):
      """
    Calculate the daily calorie intake based on gender, age, height, and weight.
    Args:
        gender (str): Gender of the person ('m' for male, 'f' for female).
        age (int): Age of the person.
        height (int): Height of the person in centimeters.
        weight (int): Weight of the person in kilograms.
    Returns:
        int: Calculated calories needed per day.
        str: Error message if the gender is invalid.
    """
    if gender == "m" or gender == "male":
        calories_needed = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
    elif gender == "f" or gender == "female":
        calories_needed = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)
    else:
        return "Please try again..." # Invalid gender input
    return int(calories_needed)

print("Welcome to Calorie Calculator\n")

gender_input = input("Gender (m/f): ").lower()
print()

try:
    age_input = int(input("Age: "))
    height_input = int(input("Height (cm): "))
    weight_input = int(input("Weight (kg): "))
except ValueError:
    print("Please enter an integer for age, height, and weight.")

print("----------")
result = calculate_calories(gender_input, age_input, height_input, weight_input)
print(f"You need {result} calories per day")
