#This is an alphabet to Morse code converter
#This file uses error handling if the input is NOT in the dictionary

#This is the Morse code dictionary
morse_dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": '-----', "1": ".----", '2': "..---", "3": "...--",
    "4": '....-', "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    " ": " "  # Space
}


def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in morse_dict:
            morse_code.append(morse_dict[char])
        elif char == " ":
            morse_code.append(morse_dict[char])
        else:
            raise ValueError(f"Invalid character: {char}")
    return " ".join(morse_code)

try:
    message = input("Enter your Morse conversion, A-Z and 0-9 only:").upper()
    morse_code = text_to_morse(message)
    print(f"The Morse code for '{message}' is: {morse_code}")
except ValueError as e:
    print(f"Error: {e}")
    

#Executes the main function
if __name__ == "main":
    main() # type: ignore