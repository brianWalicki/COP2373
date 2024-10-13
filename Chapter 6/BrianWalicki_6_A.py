import re
#Brian Walicki - 6 A.
#This program asks a user for a phone number, SSN, and zip code...
#Then says whether that number is valid by using regular expressions.

#Determines if user's phone number is valid.
def valPhoneNum(phoneNum):
    #Regular expression to check for proper format. 3-3-4 digits.
    pat = r'^\d{3}-\d{3}-\d{4}$'
    if re.match(pat,phoneNum):
        print('Valid phone number.')
    else:
        print('Invalid phone number, try again.')

#Determines if user's social security number is valid.
def valSSN(SSN):
    # Regular expression to check for proper format. 3-2-4 digits.
    pat = r'^\d{3}-\d{2}-\d{4}$'
    if re.match(pat,SSN):
        print('Valid SSN.')
    else:
        print('Invalid SSN, try again.')

#Determines if user's zip code is valid.
def valZIP(zip):
    # Regular expression to check for proper format. 5-4 digits.
    pat = r'^\d{5}(-\d{4})?$'
    if re.match(pat,zip):
        print('Valid ZIP.')
    else:
        print('Invalid ZIP, try again.')

#Asks user for a phone number, SSN, and zip code.
#Then uses that data in the above functions to determine if it's valid.
def main():
    print('Please enter numbers with dashes.')
    phoneNum = str(input("Enter phone number: "))
    SSN = str(input("Enter social security: "))
    zip = str(input("Enter zip code: "))
    valPhoneNum(phoneNum)
    valSSN(SSN)
    valZIP(zip)
main()
