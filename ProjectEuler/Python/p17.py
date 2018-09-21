#author agis daniels
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

#globals for the word lengths
ones     = [0,3,3,5,4,4,3,5,5,4]
teens    = [3,6,6,8,8,7,7,9,8,8]
tens     = [0,3,6,6,5,5,5,7,6,6]
hundreds = [0,10,10,12,11,11,10,12,12,11]

#letter_sum(x):
#this function calcs the length of a number in the word form
#param x is the number
#return the len
def letter_sum(x):
    word=str(x)
    if 1==len(word):
        return ones[int(word[0])]
    elif 2==len(word):
        if '1'==word[0]:
            return teens[int(word[1])]
        else:
            return tens[int(word[0])]+ones[int(word[1])]
    else:
        if '0'==word[2] and '0'==word[1]:
            return hundreds[int(word[0])]
        elif '1'==word[1]:
            return hundreds[int(word[0])]+3+teens[int(word[2])]
        else:
            return hundreds[int(word[0])]+3+tens[int(word[1])]+ones[int(word[2])]

def main():
    lettersum=11
    for i in range(1,1000):
        lettersum+=letter_sum(i)
    print(lettersum)

if __name__=='__main__':
    main()
