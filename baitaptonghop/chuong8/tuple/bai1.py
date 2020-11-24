#Bài 1: Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
  #  Sau đó, unpack các phần tử trong một tuple.
def nhap_tuple(n):
    arr = []
    for i in range(n):
        x = nhap_dl()
        arr.append(x)
    return tuple(arr)

def nhap_dl():
    n = input("Nhập vào dữ liệu: ")
    if n.isnumeric():
        number = int(n)
    else:
        number = n
    return number
if __name__ == "__main__":
    n = int(input("Nhập số lượng phần tử: "))
    kq = nhap_tuple(n)