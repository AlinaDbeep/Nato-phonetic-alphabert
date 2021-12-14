import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

dict = {
    row.letter:row.code for (index, row) in df.iterrows()
}

#print(dict)

word = input("Enter a word: ").upper()
word_list = [dict[letter] for letter in word]
print(" ")
index = 0
for letter in word_list:
    print(f"{word[index]} as in {word_list[index]}")        
    index +=1
        


