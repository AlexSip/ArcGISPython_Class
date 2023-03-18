letter_scores = {
    "aeioulnrst": 1,
    "dg": 2,
    "bcmp": 3,
    "fhvwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10
}

word = input("Enter a word: ").lower()

score = 0
for letter in word:
    for key in letter_scores:
        if letter in key:
            score += letter_scores[key]

print("The score for the word", word, "is", score)