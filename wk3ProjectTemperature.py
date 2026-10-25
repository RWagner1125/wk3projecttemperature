
from datetime import datetime

# Converts a Fahrenheit temperature (float) to Celsius (float).
def convertData(value):
    return (value - 32) * 5 / 9


def getInput():
    print("How many entries are you inputting?")
    entryCount = int(input())

    for entryNumber in range(entryCount):
        print("Enter a date:")
        entryDate = input()
        print("Enter the highest temp for the inputted date:")
        value = float(input())

        # convertData takes a Fahrenheit temperature (float) and returns Celsius (float).
        convertedValue = convertData(value)
        print(f"The following was saved at {datetime.now()} :")
        print(f"{entryDate},{value:g},{convertedValue}")


menuOptions = ["Input Data", "View Current Data", "Generate Report"]

print("Raywag8025's Spreadsheet Automation Menu")
print("Choose a number from the following options")

for optionNumber, optionText in enumerate(menuOptions, start=1):
    print(f"{optionNumber} {optionText}")

selection = input()

if selection == "1":
    print(f"You selected {selection} at {datetime.now()}")
    getInput()
else:
    print("Error: The chosen functionality is not implemented yet")
