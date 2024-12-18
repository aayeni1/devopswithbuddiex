from string import ascii_lowercase, ascii_uppercase


def upper_(x: str) -> str:
    location = ascii_uppercase.index(x)
    val = ascii_uppercase[25-location]
    return val

def lower_(x: str) -> str:
    location = ascii_lowercase.index(x)
    val = ascii_lowercase[25-location]
    return val

def atbash(word: str) -> str:
    lst = []
    for letter in word:
        if letter.isupper():
            val = upper_(letter)
        elif letter.islower():
            val = lower_(letter)
        else:
            val = letter
        lst.append(val)
    return ''.join(lst)

print(atbash('AbC zyx!!'))