def main():
    try:
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
        num = int(input("Enter a number: "))
        print(f"The factorial of {num} is {factorial(num)}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
