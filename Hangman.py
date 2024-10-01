count=0


word = input("What word would you like to use: ").lower()

print("The word is", len(word), "letters")

print("Counter:",count)
print("don't let count get to", len(word))
guesses = input("take your guesses: ")


for guess in range(len(word)-1):
    guesses = input("take your guesses: ")
    for guess in guesses:
        if guesses == word[0:len(word)]:
            print("Correct")
        else:
            count = count +1
            print("Counter", count)









    
