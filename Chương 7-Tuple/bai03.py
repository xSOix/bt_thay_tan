#Bài 03: Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple.
a=[['soi'],['15'],(2,6),['2'],(2,1)]
print(a)
k=0
for i in a:
    if type(i!= tuple):
        k+=1
print('so luong phan tu trong list khong phai tuple la:\t',k)