
#the multiplication include to side of numbers and doing exactly on operation
# so we will create tow for both of them start with 1 and end in 11
# we want from 1 to table 10 but i but in a range(11), bec range donsnt include
#the last number of iteration 
#so as easy as it is i multi loop one with loop tow in same range 
#and i fromat them so you can undersatnd how the operation works 
 
for i in range (1,11):
    
    for j in range (1,11):
       
        multi= i *j 
        print("{} * {} = ".format(i,j), multi )
    
 
        