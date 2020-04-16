my_list=[]
while len(my_list)<5: #inputting integers
    a=(input('Enter the integer: '))
    try:
        val=int(a)
        my_list.append(val)
    except ValueError:
        try:
            val=float(a)
            print('You entered a float. ')
            pass
        except ValueError:
            print('Your did not enter a number. ')
            pass
def findmaxvalue(array):
    count_list=[0,0,0,0,0]#List for counting the repetition times for each integer
    for i in range(5):
        count_list[i]=0
        for j in range(5):
            if array[j]==array[i]:
                count_list[i]+=1
    max_count=count_list[0] #max_count:most repetition of an integer in the list
    max_value=array[0] #max_value:an integer with the most repetition times in the list
    for i in range(5):
        if count_list[i] > max_count:
            max_count=count_list[i]
            max_value=array[i]
    return('Most repetition times:',max_count,'An integer with the most repetition times ',max_value)
print(findmaxvalue(my_list))


    

    
        
        
        







    
        
