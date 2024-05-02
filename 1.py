def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    except TypeError:
        print("Invalid input! Please enter a numerical value.")
        raise  # Re-raise the exception to propagate it back to the caller

while True:
    try:
        fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
       
    except Exception as e:
        print("An error occurred:", e)
    else:
        print("Conversion successful! The temperature in Celsius is " + str(celsius))
    finally:
        print("Thank you for using the weather forecast application.")