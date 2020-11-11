#>>>>>>==============================================bai 1=====================================<<<<<<<<<<<<<<<<<< 
gach =(">>>===============================================================<<<<")
def input_data(n):
 arr=[]
 for i in range(n):
    x=int(input(f"Input item[{i}]: "))
    arr.append()
    return arr

def input_list(n):
 arr = []
 i = 0
 while True:
    x = input(f"Input item[{i}]: ")
    try:
        arr.append(int(x))
        i += 1
        if (i >= n):
            break
    except:
                 print("Chưa nhập đúng số nguyên. Nhập lại!")
 return arr

n = int(input('nhap vao chieu dai chuoi'))
m = input_list(n)
print(gach)
print("chieu dai chuoi la",m)

#a.tinh tong gia tri trong chuoi
print(gach)
print('tong cua chuoi ban nhap la',sum(m))

#b tinh tich gia trij trong mang

print(gach)
tich=0
k=len(m)
for i in range(1, k):
    tich+= i
    print('tich cua chuoi la',tich)

#c tim so lon nhat trong chuoi
print(gach)
print('so lon nhat trong chuoi la:\t',max(m))

#d tim so nho nhat trong chuoi
print(gach)
print('so nho nhat trong chuoi la:\t',min(m))

#e + f : in ra phan tu chan le co trong mang
print(gach)
arr_chan = []
arr_le = []
for i in range(len(m)):
    if m[i] % 2 == 0:
        arr_chan.append(m[i])
    else:
        arr_le.append(m[i])

print(arr_chan)
print(arr_le)



#>>>>>>>>>>>>>>>>>>>>>>>================================================>bai 2 ==============================<<<<<<<<<<<
# Lam viec voi mang 2 chieu

m = int(input("Nhap m = "))
n = int(input("Nhap n = "))

a = []

for i in range(0, m):
    a.append([])
    for j in range(0, n):
        x = float(input("Nhap phan tu thu a[%2d][%2d]: " % (i+1, j+1)))
        a[i].append(x)

print("mang vua nhap la: ")
for i in range(0, m):
    for j in range(0, n):
        print("%3d " % a[i][j], end='')
    print()


import random
def them_ngau_nhien_ele():
     result = []
     for i in range(5):
        if (i<=5):
            random.choice(a)
            result += random.random()
            print('mang ngau nhien la:\t',result)
print(them_ngau_nhien_ele())


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

