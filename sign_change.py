from collections import Counter

class SignChanger:
    # fucntion to recieve both messages and return them
    def sign_inputs(self):
        originalSign = input("ORIGINAL SIGN MESSAGE: ")
        newSign = input("NEW SIGN MESSAGE: ")

        return (originalSign, newSign)

    # function to return the difference in characters between the two messages
    # input : two strings
    # output : dictionary of character differences
    def find_differences(self, ogSign, newSign):
        # remove spaces
        ogSign = ogSign.replace(" ", "").upper()
        newSign = newSign.replace(" ", "").upper()

        # count character frequences in both strings
        ogCount = Counter(ogSign)
        newCount = Counter(newSign)

        # calc the difference & old letters
        differences = Counter(newCount) - Counter(ogCount)
        notNeededLetters = Counter(ogCount) - Counter(newCount)

        return (dict(differences), dict(notNeededLetters))
    
    # method to print and format the output for the visual comparison
    def print_output(self, differences, notNeeded):
        print()
        if differences:
            print("Differences:")
            for char, count in sorted(differences.items()):
                print(f"{char} - {count}")
        else:
            print("The strings have no differences.")

        # Format the output
        if notNeeded:
            print("Letters you no longer need from the original:")
            for char, count in sorted(notNeeded.items()):
                print(f"{char} - {count}")