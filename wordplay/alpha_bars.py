from string import ascii_lowercase
from collections import defaultdict
import pprint as pp


def chart(text: str) -> dict:
    chart = defaultdict(lambda: [])
    for character in text:
        if character in ascii_lowercase:
            chart[character].append(character)
    # for letter in ascii_lowercase:
    #     chart[letter].extend(letter * text.count(letter))
    return chart


def input_loop(f):
    while True:
        text = input("Please enter input text (enter q to quit):")
        if text == 'q':
            break
        else:
            pp.pprint(f(text))


if __name__ == "__main__":
    print("Welcome to alpha bars.")
    print("Enter a sentence to get a bar chart with alpha bet counts.")
    input_loop(chart)
