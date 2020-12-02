def tinh(a):
    tong=0
    max=0
    for i in a:
        tong+=i
    print('tong cac so thuc trong tuple la:\t',tong)
    for j in a:
        if j> max:
            max = j
    print('so lon nhat trong tuple la:\t',max)

if __name__ == "__main__":
        a=(1,5,9,7,8,6.3,2)
        tinh(a)