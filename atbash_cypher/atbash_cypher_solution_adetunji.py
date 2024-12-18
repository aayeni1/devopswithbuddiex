alpha = list('abcdefghijklmnopqrstuvwxyz')
alphacaps= [x.upper() for x in alpha]

def atbash(word):
      result=""
      for x in range(len(word)):
            if word[x].isupper():
                  for y in range(26): #use str.index
                        new=""
                        if word[x] == alphacaps[y]:
                              new= alphacaps[25-y]
                              result= result+new  # can put this outside of condition
            elif word[x].islower():
                  for z in range(26): #use str.index
                        if word[x]== alpha[z]:
                              new = alpha[25-z]
                              result = result + new # can put this outside of condition
            else :
                  new = word[x]
                  result = result +new # can put this outside of condition
            # here is where you can put result+ 
      return result

print(atbash('zZabc!ABC'))
