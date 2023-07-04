import sys                                         
                                                   
n, m = map(int, sys.stdin.readline().split())      
                                                   
array = [0]*n                                      
                                                   
for j in range(n):                                 
    array [j] = j+1                                
                                                   
for s in range(m) :                                
    i, j = map(int, sys.stdin.readline().split())  
    temp = array[i-1:j]                            
    temp.reverse()                                 
    array[i-1:j] = temp                            
                                                   
print (*array)                                     
                                                   
                                                   