#bai1: nhap vao 2 chuoi s1 , s2 gop 2 chuoi in ra man hinh
def gopchuoi():
    s1 = str(input('nhap vao chuoi thu 1:\t'))
    s2 = str(input('nhap vao chuoi thu 2:\t'))
    gach='__________________________________________'
    print(gach)
    print('chuoi thu nhat la:\t',s1)
    print(gach)
    print('chuoi thu 2 la:\t',s2)
    print(gach)
    print('chuoi cua ban sau khi ghep la:\t',s1+' '+s2)
if __name__ == "__main__":
    print(gopchuoi())