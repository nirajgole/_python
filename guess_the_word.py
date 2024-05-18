# while loop

msg = input("Guess the word: ")

SECRET_WORD = "secret"

while msg != SECRET_WORD:
    print("Wrong!😔")
    msg = input("Guess 🤨 the word: ")

print("Correct!🤟")
