# Brian Walicki - 2 A.
# This program reads from a list of scam phrases/words,
# compares it to an inputted message, and outputs the
# likelihood of the message being a scam along with extra information

filterlist = ['#1', '100% more', '100% free', 'Best price', 'Cash bonus',
              'Billion', 'Giveaway', 'Act now', 'Urgent', 'Winner',
              'You have been selected', 'Cures', 'Congratulations', 'No gimmick',
              'Not junk', 'Obligation', 'Unsolicited', 'Ad', 'Cash',
              'Credit card offer', 'Offer', 'Debt',
              'Join millions', 'Loans', 'Luxury', 'Opt in', 'Score', 'Trial',
              'Unlimited', 'terms and conditions', 'Discount']


# This function reads the input from the user and outputs the spam score.
# This depends on how many words it finds in filterlist that are in the
# user's input, compared via a loop.

def reader():
    count = 0
    hitlist = []

    # Asks for input, then reads the length
    email = input('Please paste email.')
    print(email.split())
    length = len(email.split())

    # Compares the words in email to those in the filterlist
    for spam in filterlist:
        if spam.lower() in email.lower():

            # adds to a count and appends detected word to hitlist
            count += 1
            hitlist.append(spam)

            # Adds to count if the detected phrase is two words or more
            if ' ' in spam:
                count += 1

    # prints score, scam percent, and the list of detected words
    print('\nSpam score:', count, '| scam percentage', round(count / length, 2
        ), '| Words/phrases contributing to spam score:', hitlist)

    # returns count and length as tuple to be used in the future
    return count, length


# While this could all be one function, two is more fun.
# This function accepts values from reader() and grades
# the user's input as a scam or not via if statements
def grader(count, length):

    # calculates percent chance of scam
    chance = count / length

    # determines likelihood of input being a scam and prints the determination
    if chance >= .25:
        print("Scam, percentage of spam words at or above 25%")
    elif chance >= .1:
        print("Possible scam, percentage of spam words at or above 10%")
    elif chance >= .01:
        print("Safe.")


# grader accepts the tuple from reader by unpacking
grader(*reader())
