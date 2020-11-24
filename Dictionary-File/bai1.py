#Bài 01: Viết chương trình để đọc n dòng đầu trong 1 file text, với n được nhập từ người dùng
def docfile():
    n = int(input('nhap vao so dong ma ban muon doc:\t'))
    f = open('test1.txt','r')
    for i in range (1,n+1):
        print('dong',i,'cua file la:\t',f.readline())
if __name__ == "__main__":
    print(docfile())