#Bài 10: Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
#Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên.

def timkitucuoi():
    hammau = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
    for i in hammau:
        b=len(i)-1
        c=[]
        while i[b] !='.':
            c.append(i[b])
            b= b-1
            d = list(reversed(c))
        print('ki tu cuoi cua phan tu : ',i,'  la:\n',d)
        print('------------------------------------')
if __name__ == "__main__":
    timkitucuoi()