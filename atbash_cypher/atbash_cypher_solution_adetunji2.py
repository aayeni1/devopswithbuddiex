import os 


def atbash(word):
    reversed_list=[]
    for items in word:
        reversed_char= reverse(items)
        reversed_list.append(reversed_char)
    
    reversed_string =''.join(reversed_list)
    return reversed_string

"""def reverse(char):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    alpha_count=len(alpha) 
    if char.isupper():
        char = char.lower()
        for x in range (alpha_count):
            if char == alpha[x]:
                reverse_char=alpha[alpha_count-x-1].upper()
                #reverse_char=reverse_char.upper()
        return reverse_char 
    if char.islower() and char in alpha:
        for x in range (alpha_count):
            if char == alpha[x]:
               reverse_char=alpha[alpha_count-x-1]
               
    else : 
        reverse_char = char
        
    return reverse_char"""

def reverse(char):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    alpha_count=len(alpha) 
    if char.isupper():
        char = char.lower()
        position = alpha_count - alpha.index(char)-1
        reverse_char=alpha[position].upper()
        return reverse_char
    if char.islower() and char in alpha:
        position = alpha_count-alpha.index(char)-1
        reverse_char=alpha[position]
               
    else : 
        reverse_char = char
        
    return reverse_char




def main():
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    test1='HellO , The Team has Alot(I mean plenty-) of QUEStions?'
    test2='svool , gsv gvzn szh zolg(r nvzm kovmgb-) lu jfvhgrlmh?'
    test3='A'
    print(atbash(test1))
    print(atbash(test3))
    #print(reverse('A'))

if __name__ == '__main__':
    main()