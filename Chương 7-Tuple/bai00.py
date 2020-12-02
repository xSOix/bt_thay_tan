#Bài 00: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
            #Sau đó, unpack các phần tử trong một tuple.
def taotuple(x):
    n = int(input('nhap vao so luong phan tu tuple:\t'))
    ls = []
    for i in range (0,n):
        x = input('nhap vao phan tu thu tuple{i} :\t')
        ls.append(x)
    x =tuple(ls)
    # => unpacking
    a, b, c, d = x
    print(f"a = {a}, b = {b}, c = {c}, d = {d}")

if __name__ == "__main__":
    tuple_a =()
    print (taotuple(tuple_a))