from string import ascii_lowercase, ascii_uppercase


def convert_(x: str, ascii_case: str) -> str:
    location = ascii_case.index(x)
    return ascii_case[25-location]

def atbash(word: str) -> str:
    converted = ''
    for letter in word:
        if letter.isupper():
            val = convert_(letter, ascii_uppercase)
        elif letter.islower():
            val = convert_(letter, ascii_lowercase)
        else:
            val = letter
        converted += val
    return converted

print(atbash('AbC zyx!!'))