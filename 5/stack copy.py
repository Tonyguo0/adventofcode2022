# put stack in 9 lists and go from there
import numpy as np

def stacking():
    # [col (up to down)][row (left to right)]
    array = np.zeros([9,8], dtype=str)
    print(array)
    input_file = open('input.txt','r')
    lines = input_file.readlines()
    row = 0
    flag = False
    for line in lines:
        if line == '\n':
            flag = True
            print(array)
            a = []    
          
            for i in range(len(array)):
                a.append(np.delete(array[i],np.where(array[i]==' ')))
                # np.concatenate((newarray,np.delete(array[i],np.where(array[i]==' ')))) 
                
                
              
            # index = np.argwhere(array==' ')
            # y = np.delete(array,' ')
            
            # print(np.delete(array,np.where(array==' ')))
            # b = array[:,np.where(array != ' ', axis=1)]
            # print( b )
            # print(array)
            # a = np.char.strip(array, chars=' ')
            # a = np.char.strip(a, chars='')
            # print(a)
            # newarray = np.empty((0,4),str)
            print(a)
                # arraystripped = np.char.strip(array[i], chars = ' ')
                # print(arraystripped)
                
        if flag is True:
            # print(line)
            continue
        else: 
            # print(line)
            if line[1].isalpha():
                col = 0
                for i in range (1,len(line),4):
                        array[col][row] = line[i]
                        col+=1
        row += 1
        
    

        #
        

stacking()