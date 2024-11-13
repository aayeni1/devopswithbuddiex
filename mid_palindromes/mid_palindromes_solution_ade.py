import os

os.system('reset')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'

def mid_palindromes():
    with open (path,'r') as file:
        for line in file:
            content = line.strip()
            word = content[1:-1]
            
            if word[::1] == word [::-1]:
                print(f'{content} is a  mid-palindrome ✅')
            else:
                print(f"{content} isn't mid-palindrome ❌")
        
mid_palindromes()