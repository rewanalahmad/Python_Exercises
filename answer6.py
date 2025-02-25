

def find_divisibels  (mylist , number):

    divisibles=[]
    for i in mylist :
        if i % number ==0 :
            #he will add the i that accepted in if condition to the empty list 
           divisibles.append(i)
    return divisibles

mylist=[10,20,33,46,55]
number = 5
print(find_divisibels(mylist,number))