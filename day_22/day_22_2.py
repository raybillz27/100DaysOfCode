import pandas

nato_csv = pandas.read_csv("Nato.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_csv.iterrows()}
nato_word = input("Enter a word: ").upper()
finale = [nato_dict[letter] for letter in nato_word]
print(finale)


