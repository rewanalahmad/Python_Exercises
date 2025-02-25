


def lismethod (lis1,lis2 ) :
 #you have to create empty list so you can add elements you want to it 
    result=[]
    for x in lis1 :
 # condition here is for odd number
        if x % 2 !=0 :
 #any elements will be true it will be add to the result list 
           result.append(x)
    for i in lis2 :
 #condition here is for even number 
        if i % 2 == 0 :
   #any elemnts will be true it will be add to the result list 
           result.append(i)
    return result
    
    
lis1=[10,20,25,30,35]
lis2=[40,45,60,75,90]
print (lismethod(lis1,lis2))