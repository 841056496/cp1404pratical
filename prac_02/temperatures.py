def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius_input = float(input("Enter temperature in Celsius: "))
fahrenheit_output = celsius_to_fahrenheit(celsius_input)
print(f"{celsius_input} degrees Celsius is equal to {fahrenheit_output} degrees Fahrenheit.")

fahrenheit_input = float(input("\nEnter temperature in Fahrenheit: "))
celsius_output = fahrenheit_to_celsius(fahrenheit_input)
print(f"{fahrenheit_input} degrees Fahrenheit is equal to {celsius_output} degrees Celsius.")
