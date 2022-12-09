# put stack in 9 lists and go from there
import numpy as np

def stacking():
    # [col (up to down)][row (left to right)]
    array = np.zeros([9,8], dtype=str)
    # print(array)
    input_file = open('input.txt','r')
    lines = input_file.readlines()
    row = 0
    flag = False
    
    a = []    
    for line in lines:
        
                
        if flag is True:
            line = line.split(" ")
            from1 = int(line[3])
            move1 = int(line[1])
            to1 = int(line[5])
            for i in range(move1):
                
                last = a[from1-1][0]
                
                a[from1-1] = a[from1-1][1:]
                a[to1-1]=np.append(last,a[to1-1])
        else: 
            if line == '\n':
                flag = True
                # print(array)
            
                for i in range(len(array)):
                    a.append(np.delete(array[i],np.where(array[i]==' ')))
                    
                    
                # print(a)
                continue
            if line[1].isalpha():
                col = 0
                for i in range (1,len(line),4):
                        array[col][row] = line[i]
                        col+=1
        row += 1
    # print(a)
    result=""
    for i in a:
        result+=i[0]
        
    print(result)
stacking()


def stacking2():
    # [col (up to down)][row (left to right)]
    array = np.zeros([9,8], dtype=str)
    print(array)
    input_file = open('input.txt','r')
    lines = input_file.readlines()
    row = 0
    flag = False
    
    a = []    
    for line in lines:
        
                
        if flag is True:
            line = line.split(" ")
            from1 = int(line[3])
            move1 = int(line[1])
            to1 = int(line[5])
            # for i in range(move1):
                
            last = a[from1-1][0:move1]
            
            a[from1-1] = a[from1-1][move1:]
            a[to1-1]=np.append(last,a[to1-1])
        else: 
            if line == '\n':
                flag = True
                print(array)
            
                for i in range(len(array)):
                    a.append(np.delete(array[i],np.where(array[i]==' ')))
                    
                    
                print(a)
                continue
            if line[1].isalpha():
                col = 0
                for i in range (1,len(line),4):
                        array[col][row] = line[i]
                        col+=1
        row += 1
        
    print(a)
    
    result=""
    for i in a:
        result+=i[0]
        
    print(result)
        

stacking2()
# hello = ["w","a","s"]
# yo = ['m']
# k = hello + yo
# print(k[0])
# yo = np.append(k, hello[1:])
# print(yo)