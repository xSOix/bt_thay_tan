#=========Bài 03: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cu============================================

list = ['phantu1', 'phantu2', 'phantu3'] 
s = input("nhap chuoi ban can them:\t")
for i in range(len(list)):
    a=[]
    a= s+" "+list[i]
    print(a)



    #========================Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.  
m=list([input('nhap chuoi ban muon them voi phan sau:\t')])
list = ['day la phan thu 2']
a =m+list
print(a)



#===============================Bài 05: Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list.

list = ['hung','hao','cuong','tam','nhung','tam','tam','cuong','phuong']
count={}
for i in list:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1
 
for i in sorted(count, key=count.get, reverse=False):
        print(i, count[i])




#==============Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn

list = ['hung','hao','cuong','tam','nhung','tam','tam','cuong','phuong']
count={}
for i in list:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1
 
for i in sorted(count, key=count.get, reverse=False):
    if(count[i]>=2):
        print(i, count[i])






#==============Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không.
list1= list(['hung','hao','cuong','tam','nhung','tam','tam','cuong','phuong'])
list2 = list(['hung'])
count={}
for i in list1:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1
for j in list2:
    if i in count:
        count[j] +=1
    else:
        count[j] = 1
for i in sorted(count, key=count.get, reverse=False):
    if(i==j):
        print('ki tu xuat hien trong ca 2 list là:\t ',i)




#=============Bài 09: Viết chương trình tính tích của 2 ma trận vuông cấp 3 

import numpy as np
mx_1 = [[1, 2, 3],
 [4, 5, 6],
 [1, 0, 0]]
mx_2 = [[2, 1, 0],
 [9, 0, 5],
 [0, 3, 7]]
a = np.array(mx_1) 
b = np.array(mx_2) 
print('mang1 * mang2', a*b)

