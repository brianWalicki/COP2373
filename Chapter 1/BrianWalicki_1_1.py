# Brian Walicki - Assignment 1
# The purchase_sys function takes the initial number of tickets then
# continuously asks how many tickets you would like and subtracts that until
# it reaches 0.

def purchase_sys(tickets):
    buyers=0

    # Loop forever, until tickets==0 (break on ln 15)
    while True:

        # Before asking for input, checks if tickets is zero
        if tickets==0:
            print(str(buyers),'buyers total')
            break

        #In case of non-integer input (exception on ln33)
        try:
            # Asks user for number of tickets and makes it an int
            request = int(input('How many tickets would you like? '))

            # Checks if requested tickets is legal, otherwise prints limits
            if request > 4 or request < 0:
                print('A Maximum of four tickets per person, also, non-refundable')
            elif request>tickets:
                print('Not enough tickets remaining.')

            # Subtracts from total tickets and adds 1 to amount of buyers
            else:
                tickets -= request
                buyers+=1

            print(tickets,'tickets remaining')

        #if user inputs anything but a number, catches exception
        except ValueError:
            print('Numbers only, please.')

purchase_sys(20)