def min_no(list1,m,n):
    new_list=[]
    for i in range(m,n):
        if i not in list1:
            new_list.append(i)
    x=min(new_list)
    print("Min:",x)
list1=[1,2,4,5,7,8,9,10,11,12,14,15,18,20]
c=min(list1)
q=max(list1)
print(list1)
min_no(list1,c,q)

