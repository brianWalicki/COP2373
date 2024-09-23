# Asks user for a list of monthly expenses,then displays the total expense
# and the highest/lowest expense


# This function gets data from the user and formats it as a dict
def get_data():
    expenses = {}

    # Tells the user how to stop adding to the dict
    print("press x to stop adding to the list")

    # Loop as long as the user wants and make dict of their expenses
    while True:

        # Asks for the key to dict and checks if stop was called
        try:
            key = str(input("What type of expense? "))
            if key == "x".lower():
                break

            # Asks for the value for the dict then adds it all to the dict
            data = float(input("Amount of the expense? "))
            expenses[key] = data

        # If the user input a value that was not a
        # number, resets that dict entry
        except ValueError:
            print("Only numbers for the amount, redo this expense")
    return expenses

# This function finds the highest, lowest, and total of a given dict
# as long as the dict is any(key) and float(value)
def analyze(expenses):

    # Initialize all the values that will be returned
    # Assigns lowest, low_key, highest, high_key to first dict entry
    total = 0.0
    lowest = next(iter(expenses.values()))
    highest = next(iter(expenses.values()))
    low_key = next(iter(expenses.keys()))
    high_key = next(iter(expenses.keys()))

    # Loops for every entry in the dict "expenses" and compares values
    for key, value in expenses.items():

        # Adds to the total value that will be returned later
        total += float(value)

        # If/elif to compare values, if a new high/low is found
        # it becomes the new high/low
        if value < lowest:
            low_key = key
            lowest = value
        elif value > highest:
            high_key = key
            highest = value

        # Prints out the analysis
    print("lowest expense:", low_key, "at a value of:", lowest,
          "| highest expense:", high_key, "at a value of:", highest,
          "| total expenses:", round(total,4))

analyze(get_data())