# for each line if is \n add all the numbers previously
import os
from depq import DEPQ as queue


def test():
    for i in range(5):
        q.insert(i, i)
    
    print(str(q))

# test()

def max():
    q = queue()
    answer = 0
    cal = 0
    input_file = open("input.txt",'r')
    lines = input_file.readlines()
    for line in lines:
        if '\n' == line or "" == line:
            if cal > answer:
                answer = cal
            q.insert(cal,cal)    
            cal = 0
        else:
            cal += int(line)
            
    return answer, q
        

# print(max()[0])

def topThree():
    pqueue2 = max()[1]
    answer = 0
    for i in range(3):
        
        answer += pqueue2.popfirst()[0]
    
    return answer  

print(topThree())