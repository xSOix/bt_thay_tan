#Bài 08: Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.
def kitutrung(a):
    b=list(a)
    tmp=[]
    kitu=[] 
    for j in b: 
        if tmp.__contains__(j):
            kitu.append(j)
        else: 
            tmp.append(j)
    print('cac ki tu trung trong tuple cua ban la:\t',kitu)

if __name__ == "__main__":
    a=(1,5,7,1,4,5,9,2)
    kitutrung(a)