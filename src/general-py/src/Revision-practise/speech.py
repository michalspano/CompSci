import pyttsx3

"""
Using 'pyttsx3' to create speech-to-text recognition
Source: https://pypi.org/project/pyttsx3/
"""


def main():
    print("Convert text to speech!")

    # Get some user input
    user_input = input("Convert to speech: ")

    # Call the speech recognition function
    speech_recognition(user_input)


def speech_recognition(argument):

    # Initialise the speech recognition library and its instance
    engine = pyttsx3.init()

    # Execute the conversion
    engine.say(argument)
    engine.runAndWait()


if __name__ == '__main__':
    main()
