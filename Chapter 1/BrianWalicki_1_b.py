# Creates Creates a file "8ball_responses.txt" then reads from it and asks
# prompts user for yes/no question then prints a random phrase from questions

import random
questions = ['Yes, of course!', 'Without a doubt, yes.', 'You can count on it.', 'For sure!', 'Ask me later!', "I'm not sure.", "I can't tell you right now.", "I'll tell you after my nap.", 'No way!', "I don't think so.", 'Without a doubt, no.', 'The answer is clearly NO!']

# Creates a file "8ball_responses.txt" with contents from [questions]
def write_phrases():
    f = open("8ball_responses.txt","w")
    for i in questions:
        f.write(i+'\n')
        f.write('\n')

# Reads from "8ball_responses.txt" and answers the user with a random phrase
def questionnaire(file):

    # Read from a file and makes a list of its contents
    ls = []
    with open(f'{file}','r') as file:
        for line in file:
            ls.append(line.replace('\n','').rstrip())
        for index in ls:
            if index == '':
                ls.remove(index)

    # Asks user for a yes/no question then randomly answers from the list
    # loops forever until the user enters 'x'
    print('Press x to exit.')
    while True:
        resp = input("Ask a yes/no question. ")
        if resp == 'x':
            break
        print(random.choice(ls))

write_phrases()
questionnaire('8ball_responses.txt')