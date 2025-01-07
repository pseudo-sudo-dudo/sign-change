from sign_change import SignChanger  # Import the SignChanger class

def main():
    # Initialize SignChanger
    sc = SignChanger()

    # Intro & Get the messages
    print("Welcome to the church sign program. We will take both sign inputs and tell you what letters you need.")
    originalSign, newSign = sc.sign_inputs()

    # Process the message differences
    diffLetters, uselessLetters = sc.find_differences(originalSign, newSign)
    print(diffLetters)
    sc.print_output(diffLetters, uselessLetters)

# Using the special variable
# __name__
if __name__ == "__main__":
    main()
