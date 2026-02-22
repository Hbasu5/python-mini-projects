import random
attempts = 6
fruits = ["apple","banana","cherry","date","elderberry","fig","grape","honeydew","kiwi","lemon","mango","nectarine","orange","papaya","peach","pear","pineapple","plum","raspberry"]
animals = ["tiger","elephant","giraffe","zebra","lion","bear","monkey","panda","kangaroo","koala","hippopotamus","rhinoceros","crocodile","alligator","fox","wolf","deer","rabbit","squirrel"]
nations = ["canada","brazil","france","germany","italy","japan","india","china","australia","spain","mexico","russia","southafrica","egypt","argentina","sweden","norway","finland","denmark"]
cars = ["toyota","honda","ford","chevrolet","nissan","bmw","mercedes","audi","volkswagen","hyundai","tesla","subaru","mazda","volvo","jaguar","porsche","ferrari","lamborghini","bugatti","mclaren"]
colour = ["red","blue","green","yellow","purple","orange","pink","brown","black","white","gray","cyan","magenta","lime","maroon","navy","olive","teal","violet","indigo","gold","silver","bronze"]
companies = ["google","apple","microsoft","amazon","facebook","tesla","netflix","uber","airbnb","spotify","twitter","linkedin","adobe","salesforce","oracle","intel","ibm","nvidia","samsung","sony"]
language = ["english","spanish","french","german","italian","portuguese","russian","chinese","japanese","korean","bengali","hindi","arabic","turkish","vietnamese","persian","swedish","norwegian","danish","finnish"]
print(f"""
Welcome to Wordle!
You have {attempts} attempts.
You have to enter full words, not letters.

G - Correct position
Y - Wrong position
R - Not present
Bonus: Choose your category: fruits, animals, nations, cars, colour, companies, language
""")
categories = {
    "fruits": fruits,
    "animals": animals,
    "nations": nations,
    "cars": cars,
    "colour": colour,
    "companies": companies,
    "language": language
}
category_choice = input("Enter your category choice: ").lower()
if category_choice not in categories:
    print("Invalid category choice. Defaulting to fruits.")
    category_choice = "fruits"
secret_word = random.choice(categories[category_choice])
print("The secret word has been chosen. It has ", len(secret_word), " letters. Start guessing!")

while attempts > 0:
    guess = input("Enter your guess: ").lower()
    if len(guess) != len(secret_word):
        print(f"Word must be {len(secret_word)} letters!")
        continue
    if guess == secret_word:
        print("You guessed it correctly!")
        break
    feedback = ["R"] * len(secret_word)
    secret_temp = list(secret_word)
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            feedback[i] = "G"
            secret_temp[i] = None
    for i in range(len(secret_word)):
        if feedback[i] == "R" and guess[i] in secret_temp:
            feedback[i] = "Y"
            secret_temp[secret_temp.index(guess[i])] = None

    attempts -= 1
    print("Feedback:", " ".join(feedback)) #print(f"Feedback: {feedback}")
    print("Attempts left:", attempts, "\n")

if attempts == 0:
    print(f"Game Over! The word was: {secret_word}")