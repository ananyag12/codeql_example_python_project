def main():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit}")

    except ValueError:
        print("Invalid input! Please enter a string.")

if __name__ == "__main__":
    main()
