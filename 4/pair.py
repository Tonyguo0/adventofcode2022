

def pair():
    pairfile = open('input.txt', 'r')
    lines = pairfile.readlines()
    count = 0
    for line in lines:
        splitted = line.split(",")
        splitted1 = splitted[0].split('-')
        splitted2 = splitted[1].split('-')
        # splitted2 contain splitted 1:  splitted1[0] >= splitted2[0] and splitted1[1]<= splitted2[1]
        # splitted1 contain splitted 2:  splitted2[0] >= splitted1[0] and splitted2[1]<= splitted1[1]
        # 
        
        splitted1 = [ int(x) for x in splitted1]
        splitted2 = [ int(x) for x in splitted2]
        
        if splitted1[0] >= splitted2[0] and splitted1[1]<= splitted2[1]:
            count += 1
        elif splitted2[0] >= splitted1[0] and splitted2[1]<= splitted1[1]:
            count += 1
        else: continue
    
    print(count)
    

# pair()


def overlap():
    pairfile = open('input.txt', 'r')
    lines = pairfile.readlines()
    count = 0
    for line in lines:
        splitted = line.split(",")
        splitted1 = splitted[0].split('-')
        splitted2 = splitted[1].split('-')
        # splitted1 overlap splitted2: splitted1[1]>= splitted2[0] and splitted1[0] <= splitted2[0]
        # splitted2 overlap splitted1:  splitted2[1] >= splitted1[0] and splitted2[0]<= splitted1[0]
        # 
        
        splitted1 = [ int(x) for x in splitted1]
        splitted2 = [ int(x) for x in splitted2]
        
        if splitted1[1]>= splitted2[0] and splitted1[0] <= splitted2[0]:
            count += 1
        elif splitted2[1] >= splitted1[0] and splitted2[0]<= splitted1[0]:
            count += 1
        else: continue
    
    print(count)
    

overlap()