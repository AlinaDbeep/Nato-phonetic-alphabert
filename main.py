import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

dict = {
    row.letter:row.code for (index, row) in df.iterrows()
}

#print(dict)

def app():
    app_off = False
    while not app_off:
        word = input("Enter a word: ").upper()
        try:
            word_list = [dict[letter] for letter in word]
            print(" ")
            index = 0
            for letter in word_list:
                print(f"{word[index]} as in {word_list[index]}")
                index +=1
            print("")
            again = input("Do you want to use the app one more time?\nType 'y' to continue or 'no' to exit: ")
            if again == 'y':
                app()
            else:
                print("\nSee you! Have a nice day!")
                quit()
        except KeyError:
            print("Sorry, only letters in the alphabet, please")
            app()


app()

