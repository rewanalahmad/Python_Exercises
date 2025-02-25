

def incomtx ( salary) :
    if salary <= 10000 :
        return 0 
    elif salary <= 20000 :
        remining  = salary  - 10000 
        tax= remining * 0.1 
        return tax 
    if salary > 20000 :
        remining = salary - 20000 
        tax1= 10000 * 0.1
        tax2 = remining * 0.2
        return tax1 + tax2 
        
print (incomtx(45000),"$")
        
        
        
        
        
     
        