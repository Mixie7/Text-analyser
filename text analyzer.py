# Use the input function to allow the user to enter the text
# store the text in the variable 'text'
# make the text output in lowercase
text = input("Enter a piece of text: ").lower()

# create variables to store each letter in
# make output in lowercase
# use f-strings and print a sentence that tells us what the letter is and how many times it appears
# use count() method to find the specific letter
print("\nHOW MANY TIMES A CERTAIN LETTER APPEARS")
letter1 = input("Enter a letter: ").lower()
letter2 = input("Enter a letter: ").lower()
letter3 = input("Enter a letter: ").lower()
print(f"Letter '{letter1}' appears {text.count(letter1)} times")
print(f"Letter '{letter2}' appears {text.count(letter2)} times")
print(f"Letter '{letter3}' appears {text.count(letter3)} times")

print("\nHOW MANY WORDS ARE IN THE WHOLE TEXT:")
# create a list and use the split() method to separate the words by spaces
# use the len function to count the elements (words) from the list
text_list = list(text.split(" "))
print(f"There are {len(text_list)} words in the text")

print("\nFIRST AND LAST LETTERS OF THE TEXT:")
# use string indexing
print(f"The first letter is '{text[0]}'")
print(f"The last letter is '{text[-1]}'")

print("\nTHE TEXT IN INVERTED ORDER:")
# use the reverse() method on the list
text_list.reverse()
inverted = " ".join(text_list)
print(f"The text backwards is '{inverted}'")


print("\nIS 'PYTHON' INSIDE THE TEXT:")
# use an if statement to check if the word python is in the text
if "python".lower() in text:
    print("The word 'python' is in the text")
else:
    print("The word 'python' is not in the text")