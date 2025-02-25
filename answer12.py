

def exponent (base , exp ):
 # we check if the exp number is zero 
    if exp>0 :
     
        return base**exp
        #if you dont write this line if the exp number was 0 then it will print none
        
    elif exp ==0 :
         return 1
        #e^0 =1
base = int (input(" enter the base number : " ))
exp = int (input ( " enter the exp number : " ))

print("{} raises to the power of {} =".format(base,exp), exponent(base,exp))