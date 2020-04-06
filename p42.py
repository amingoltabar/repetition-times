my_list=[]
for i in range(5):
    a=float(input('Enter the integer '))
    while a!=int(a):
        a=float(input('You did not enter an integer.Enter the integer '))
    a=int(a)
    my_list.append(a)
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


    

    
        
        
        







    
        
