# 8. Input temperature in Celsius and display the equivalent Fahrenheit and Kelvin values.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")
print(f"Temperature in Kelvin: {kelvin:.2f}K") 