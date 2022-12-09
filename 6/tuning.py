
def tuning():
    openfile= open('input.txt', 'r')
    lines = openfile.readline()
    myset = set()
    mylist = list()
    result = 0
    for c,char in enumerate(lines):
        
        if c >= 14:
            
            mylist.pop(0)
        mylist.append(char)
        print(c, set(mylist), len(set(mylist)))
        
        if len(set(mylist)) == 14:
            result = c+1
            break
        
    print(result)

tuning()