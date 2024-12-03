def main():
    try:
        text = input("Enter a string: ")
        reversed_text = text[::-1]
        print("Reversed string:", reversed_text)

    except ValueError:
        print("Invalid input! Please enter a string.")

if __name__ == "__main__":
    main()
