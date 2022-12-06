# put stack in 9 lists and go from there


def stacking():
    input_file = open('input.txt','r')
    lines = input_file.readlines()
    flag = False
    for line in lines:
        if line == '\n':
            flag = True
        if flag is True:
            print(line)
        
        

stacking()