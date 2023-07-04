import sys                                        
                                                  
n =int(sys.stdin.readline())                      
                                                  
grade = sys.stdin.readline().split()              
grade = list(map(int,grade))                      
                                                  
highest = max(grade)                              
new_grade = []                                    
                                                  
for i in range(n) :                               
    new_one = grade[i] / highest*100              
    new_grade.append(new_one)                     
                                                  
mean = 0                                          
                                                  
for j in range(len(new_grade)) :                  
    mean += new_grade[j]                          
                                                  
result = mean/n                                   
                                                  
print (result)                                    
                                                  
                                                  
                                                  