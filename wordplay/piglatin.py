VOWELS = 'aeiou'


def encode(text: str) -> str:
    words = text.lower().split(' ')
    output = []
    for word in words:
        if(word[0] in VOWELS):
            word = ''.join([word, 'way'])
        else:
            word = ''.join([word[1:], word[0], 'ay'])
        output.append(word)
    return ' '.join(output)


def decode():
    pass


def input_loop(f):
    while True:
        text = input("Please enter input text (enter q to quit):")
        if text == 'q':
            break
        else:
            print(f(text))


if __name__ == "__main__":
    print("Welcome to piglatin encoder.")
    input_loop(encode)
