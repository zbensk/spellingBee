# The purpose of this program is to solve spelling bee in the NYT by providing a list of all the words that work

acceptable_words = []

with open("wordlist.txt") as file:
  word_list = file.read().splitlines()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

center_letter = input("Enter the central letter: ").lower()
alphabet.remove(center_letter)
for i in range(6):
  other_letters = input("Enter a non-central letter: ").lower()
  alphabet.remove(other_letters)

def checkWord(word):
  if center_letter in word and len(word) >= 4:
    for letter in alphabet:
      if letter in word:
        return False
    return True

for word in word_list:
  if(checkWord(word)):
    acceptable_words.append(word)

print(len(acceptable_words))
for w in acceptable_words:
  print(w)
