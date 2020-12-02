def kiemtra(a,b):
    k=0
    for i in b:
        if i in a:
            k+=1
    if k == len(b):
        print('phan tu b co trong a')
    else:
        print('phan tu b khong co trong a')
if __name__ == "__main__":
    a = (1,5,6,8,7,9)
    b=(5,7,9)
    kiemtra(a,b)