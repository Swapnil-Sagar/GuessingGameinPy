import random
#Get guess
def get_guess():
    return list(input("What is your guess: "))


#Generate computer guess
def generate_code():
    digits = [str(num) for num in range(10)]

    #Shuffle the digits
    random.shuffle(digits)
    #Then grab first 3
    return digits[:3]

#Generate the clues
def generate_clues(code,user_guess):
    if user_guess==code:
        return "CRACKED!"

    clues = []

    for ind,num in enumerate(user_guess):  #enumerate increases index location after every iteration
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("Close")

    if clues == []:
        return ["Nope"]
    else:
        return clues


#Run game logic

print("Welcome Code Breaker!")

secret_code = generate_code()

clue_report =[]

while clue_report != "CRACKED!":
    guess = get_guess()

    clue_report = generate_clues(guess,secret_code)
    print("Here is the result of your guess: ")
    for clue in clue_report:
        print (clue)
