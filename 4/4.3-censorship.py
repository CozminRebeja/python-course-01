"""
Create a function called censor that takes a string
and replaces words over four characters with *.

- Don't censor words with exactly four characters.
- If all words have four characters or less, return the original string.
- The number of * is the same as the length of the word.
"""
def convertWord(stringInput):
    inputList = list(stringInput)
    i = 0
    while i < len(inputList): 
        inputList[i] = "*"
        i += 1
        
    return "".join(inputList)

def check4(stirngInput):
    if len(stirngInput) > 4:
        return True
        

def censor(x):
    listX = list(x.split(' '))
    
    for item in listX:
         if check4(item):
            index = listX.index(item)
            listX[index] = convertWord(listX[index])
            
    
    return " ".join(listX)
            

def main():

    print(censor("the code is fourty"))
    print (censor("suge pulalaul mai mihailuta"))
    #censor("the code is fourty") -> The code is ******

if __name__ == "__main__":
    main()
