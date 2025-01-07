from collections import Counter

# fucntion to recieve both messages and return them
def sign_inputs():
    originalSign = input("ORIGINAL SIGN MESSAGE: ")
    newSign = input("NEW SIGN MESSAGE: ")

    return (originalSign, newSign)

# function to return the difference in characters between the two messages
# input : two strings
# output : dictionary of character differences
def find_differences(ogSign, newSign):
    # remove spaces
    ogSign = ogSign.replace(" ", "")
    newSign = newSign.replace(" ", "")

    # count character frequences in both strings
    ogCount = Counter(ogSign)
    newCount = Counter(newSign)

    # calc the difference
    differences = Counter(newCount) - Counter(ogCount)
    
    # Format the output
    if differences:
        print("Differences:")
        for char, count in sorted(differences.items()):
            print(f"{char} - {count}")
    else:
        print("The strings have no differences.")

# Main function
def main():
    # Intro & Get the messages
    print("Welcome to the church sign program. We will take both sign inputs and tell you what letters you need.")
    originalSign, newSign = sign_inputs()

    # Process the messages differences
    find_differences(originalSign, newSign)

    # Return the results
    # print(f"Testing original: {originalSign} \nTesting new: {newSign}")


# Using the special variable 
# __name__
if __name__=="__main__":
    main()