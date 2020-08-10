from pathlib import Path
from pprint import pprint

WORDS_FILE = '/usr/share/dict/words'


def get_words(file_name=WORDS_FILE):
    try:
        text = Path(WORDS_FILE).read_text()
    except FileNotFoundError:
        print(f'File {file_name} not found.')
        return None
    words = text.strip().split('\n')
    words = [word.lower() for word in words]
    return words


def find_palindrome(words):
    palindrome = [
        word for word in words if word == word[::-1] and len(word) > 1
    ]
    return palindrome


if __name__ == "__main__":
    words = get_words()
    palindrome = find_palindrome(words)
    pprint(palindrome)
