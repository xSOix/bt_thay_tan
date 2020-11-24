#bai2 viet chuong trinh them 1 chuoi nao do vao cuoi file:
def vietfile():
    n = str(input('nhap vao noi dung ma ban muon them vao:\t'))
    f = open('test1.txt','a')
    f.write(n +'\n')
if __name__ == "__main__":
    print(vietfile())