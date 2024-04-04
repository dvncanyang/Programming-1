word_to_number = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",
    "eleven": "11",
    "twelve": "12",
    "thirteen": "13",
    "fourteen": "14",
    "fifteen": "15",
    "sixteen": "16",
    "seventeen": "17",
    "eighteen": "18",
    "nineteen": "19",
    "twenty" and "twenty-": "20",
    "thirty" and "thirty-": "30",
    "fourty" and "fourty-": "40",
    "fifty" and "fifty-": "50",
    "sixty" and "sixty-": "60",
    "seventy" and "seventy-": "70",
    "eighty" and "eighty-": "80",
    "ninety" and "ninety-": "90",
}

def words_to_numbers(text):
    words = text.lower().split()
    for i, word in enumerate(words):
        if word in word_to_number:
            words[i] = words_to_numbers[word]
    return ' '.join(words)

input_text = input("wtv prompt: ")
output_text = words_to_numbers(input_text)
print("Output: ", output_text)