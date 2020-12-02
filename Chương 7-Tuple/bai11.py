#Bài 11: Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.
def inrakitudainhat(n):
    a = n.split()
    lonnhat=[]
    t=0
    for i in a:
        if t < len(i):
            t=len(i)
            lonnhat.append(i)
    print(lonnhat[-1])

if __name__ == "__main__":
    n = str(input('nhap cau ma ban muon tim tu dai nhat:\t'))
    inrakitudainhat(n)

    