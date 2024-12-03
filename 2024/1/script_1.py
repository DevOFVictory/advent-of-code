with open('input.txt') as f:
    lines = f.read().splitlines()

    l1,l2 = [], []
    
    for line in lines:
        print(line)
        l1.append(int(line.split('   ')[0]))
        l2.append(int(line.split('   ')[1]))
        
        
    a = 0
        
    l1 = sorted(l1)
    l2 = sorted(l2)
    
    print(l1)
    
    for i in range(len(l1)):
        
        a += abs(l1[i] - l2[i])  

    print(a)