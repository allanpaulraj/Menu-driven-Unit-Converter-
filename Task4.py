
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

CONVERSIONS = {
    "1": {
        "name": "Temperature",
        "options": {
            "1": ("Celsius to Fahrenheit", "°C", "°F", celsius_to_fahrenheit),
            "2": ("Fahrenheit to Celsius", "°F", "°C", fahrenheit_to_celsius),
        },
    },
    "2": {
        "name": "Distance",
        "options": {
            "1": ("Meters to Feet", "m", "ft", meters_to_feet),
            "2": ("Feet to Meters", "ft", "m", feet_to_meters),
        },
    },
    "3": {
        "name": "Weight",
        "options": {
            "1": ("Kilograms to Pounds", "kg", "lbs", kg_to_pounds),
            "2": ("Pounds to Kilograms", "lbs", "kg", pounds_to_kg),
        },
    },
}

def get_validated_float(prompt):

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(" Invalid input. Please enter a numeric value.")

def run_conversion(category):
    
    while True:
        print(f"\n--- {category['name']} Conversion ---")
        for key, value in category['options'].items():
            print(f"{key}. {value[0]}")
        print("b. Back to main menu")

        choice = input("Choose a conversion: ")

        if choice.lower() == 'b':
            break

        if choice in category['options']:
            name, unit_from, unit_to, func = category['options'][choice]
            value = get_validated_float(f"Enter value in {unit_from}: ")
            result = func(value)
            
            # 4. Display results using formatted strings.
            print("\n" + "="*20)
            print(f"Result: {value:.2f}{unit_from} is {result:.2f}{unit_to}")
            print("="*20)
            input("Press Enter to continue...")
        else:
            print(" Invalid choice. Please try again.")

def main():
    """Main function to run the menu-driven program."""
    
    while True:
        print("\n========== Unit Converter ==========")
        for key, value in CONVERSIONS.items():
            print(f"{key}. Convert {value['name']}")
        print("q. Quit")
        print("====================================")
        
        main_choice = input("Select a category: ")

        if main_choice.lower() == 'q':
            print("Goodbye! ")
            break

        if main_choice in CONVERSIONS:
            run_conversion(CONVERSIONS[main_choice])
        else:
            print(" Invalid category. Please select a valid option.")

if __name__ == "__main__":
    main()
