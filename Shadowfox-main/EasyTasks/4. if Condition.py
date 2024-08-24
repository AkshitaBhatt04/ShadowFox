# 1. Calculate BMI Category
# BMI = weight (in kg) / height (in meters) squared
def calc_bmi(weight, height):
    bmi = weight / (height ** 2)

    if bmi >= 30:
        return "Obesity"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Underweight"


try:
    height = float(input("Enter height in meters (e.g., 1.75):\n"))
    weight = float(input("Enter weight in kilograms (e.g., 70):\n"))
    result = calc_bmi(weight, height)
    print(result)
except ValueError:
    print("Please enter valid numeric values for height and weight.")

# 2. Determine which country a city belongs to

countries_dict = {"Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
                  "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
                  "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]}

city = input("Enter a city name: \n")


def find_city(city):
    for country, cities in countries_dict.items():
        if city in cities:
            return country
    return


country = find_city(city)
if country:
    print(f"{city} is in {country}.")
else:
    print(f"{city} not found.")


# 3. Check if two cities belong to the same country

def find_country(city):
    for country, cities in countries_dict.items():
        if city in cities:
            return country
    return


city1 = input("Enter the first city: \n")
city2 = input("Enter the second city: \n")

country1 = find_country(city1)
country2 = find_country(city2)

if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities not found.")
