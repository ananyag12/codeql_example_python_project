def main():
    try:
        text = input("Enter a string: ").lower()
        vowels = "aeiou"
        count = sum(1 for char in text if char in vowels)
        print("Number of vowels:", count)
        
    except ValueError:
        print("Invalid input! Please enter a string.")

if __name__ == "__main__":
    main()
