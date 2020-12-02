#Bài 04: Cho 1 list chứa các tuple không rỗng.
#Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
#Ví dụ: [(2, 5), (4, 1), (0, 0)] => [(0, 0), (4, 1), (2, 5)]

def sapxeplaitype():
    typemau=[(2, 5), (4, 1), (0, 0)]
    list1 = list(typemau)
    lst=[]
    for i in list1:
        a = len(i)
        lst.append(i[a-1])
    for i in range (len(lst)):
        for j in range (i):
            if lst[i] < lst[j]:
                tmp = lst[i]
                lst[i] = lst[j]
                lst[j] = tmp
    listsapxep=[]
    for i in lst:
        for j in list1:
            k= len(j)
            if i == j[k-1]:
                listsapxep.append(j)
    print('list sau khi da duoc sap xep lai theo thu tu tang dan cua pha tu cuoi \n',listsapxep)
if __name__ == "__main__":
    print(sapxeplaitype())