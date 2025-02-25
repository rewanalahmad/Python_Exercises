
for i in range(11)  :
    
    print("the index : " , i)
    sum = i + (i-1)    #here the number + the index befor not the sum befor 
    '''
          0 + (0-1)-1 = -1
          1 + (1-1)0 = 1
          2 + (2-1)1 = 3
          3 + (3-1)2 = 5
          4 + (4-1)3 = 7 
          5 + (5-1)4 = 9
          6 + (6-1)5 = 11
          7 + (7-1)6 = 13
          8 + (8-1)7 = 15
          9 + (9-1)8 = 17  
          '''
    print(sum)
 