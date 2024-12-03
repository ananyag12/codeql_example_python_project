def main():
    try:
        text = input("Enter a string: ").lower()
        if text == text[::-1]:
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")

    except ValueError:
        print("Invalid input! Please enter a string.")

if __name__ == "__main__":
    main()
