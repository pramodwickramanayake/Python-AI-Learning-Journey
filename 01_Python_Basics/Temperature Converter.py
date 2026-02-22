# Simple Celsius to Fahrenheit Converter

# Functions to handle calculations
def multiply_values(val1, val2):
    return val1 * val2

def add_values(val1, val2):
    return val1 + val2

def main():
    # User input
    celsius = float(input("Enter the temperature in Celsius: "))
    
    # Formula logic: (Celsius * 9/5) + 32
    factor = 9/5
    intermediate_val = multiply_values(celsius, factor)
    
    fahrenheit = add_values(intermediate_val, 32)
    
    # Output result
    print(f"{celsius}°C is equal to {fahrenheit}°F")

if __name__ == "__main__":
    main()