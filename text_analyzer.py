print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("▌Welcome from Text Analyzer Program▐")
print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
print("That analyzer will be calculate your inserted text's words count, spaces count and vowels count.\n")

vowels = "AEIOU"
space_count = 0
vowels_count = 0
words_count = 0

input_txt = input("Enter do you wanna analyz sentence or paragraph : ").upper()

for char in input_txt:
    if char == " ":
        space_count += 1
    elif char in vowels:
        vowels_count += 1

words_count = len(input_txt.split())

#Result
print("\nAnalysis of you inserted text :")
print(f"\tCount of words\t: {words_count}")
print(f"\tCount of vowels\t: {vowels_count}")
print(f"\tCount of spaces\t: {space_count}")