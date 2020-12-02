#Bài 01: Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple

def tuplesanglist():
    a= (1,'shiho',12,'trungtinh','soi',1998)
    chuyenlist = list(a)
    print('day la tuple nguyen mau:\t',a)
    print('day la tuple sau khi chuyen sang list',chuyenlist)

def listsangtuple():
    b=[1,'shiho',12,'trungtinh','soi',1998]
    chuyentuple= tuple(b)
    print('day la list luc dau:\t', b)
    print('day la tuple sau khi chuyen tu list',chuyentuple)

if __name__ == "__main__":
        gach ='__________________________________________________'
        while 1:
            n= int(input('nhap vao: \n 1. khi tuple=>list \n 2. khi list =>tuple \n =>>>:\t'))
            if n ==1:
                print(tuplesanglist())
                print(gach)
            elif n==2:
                print(listsangtuple())
                print(gach)
                continue
            else:
                break    
