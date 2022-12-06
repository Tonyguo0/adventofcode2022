
# split the line some how
    # get the string from the line 
    # get the length of string and cut in half
    # get and compare the two strings to find the common letter how?
    
    
# have map of letter to number to get sum of the numbers from the line

def priority():
    txt = open("input.txt","r")
    lines = txt.readlines()
    dictionary = {}
    letter = "a"
    
    for i in range(1,27):
        dictionary[letter] = i
        letter = chr(ord(letter) +1)
    
    letter = "A"
    for i in range(27,53):
        dictionary[letter] = i
        letter = chr(ord(letter) +1)    
        
    print(dictionary)
    total = 0
    for line in lines:
        first,second = line[:len(line)//2], line[len(line)//2:]
        common_char = ''.join(set(first).intersection(second))
        total += dictionary[common_char]
    
    print( total)
    
# priority()    


def priority3():
    txt = open("input.txt","r")
    lines = txt.readlines()
    dictionary = {}
    letter = "a"
    
    for i in range(1,27):
        dictionary[letter] = i
        letter = chr(ord(letter) +1)
    
    letter = "A"
    for i in range(27,53):
        dictionary[letter] = i
        letter = chr(ord(letter) +1)    
        
    # print(dictionary)
    total = 0
    intersectiona = []
    count = 0
    for line in lines:
        count += 1
        intersectiona.append(line.strip())
        if count ==3:
            count = 0
            common_char1 = ''.join(set(intersectiona[0]).intersection(intersectiona[1]))
            print(common_char1)
            common_char2 = ''.join(set(intersectiona[2]).intersection(common_char1))
            print(common_char2)
            
            total += dictionary[common_char2]
            intersectiona = []
    
    print(total)
    
priority3()