#bai3 viet chuong trinh tron 2 file thanh file moi
def doc_file():
     b=[]
     f = open("test1.txt",'r', encoding='utf8')
     b = f.readlines()
     f.close()
     c=[]
     k = open("test2.txt",'r', encoding='utf8')
     c = k.readlines()
     f.close()
     t= str
     t = b + c
     m = open("filetong.txt",'a', encoding='utf8') 
     m.write(t)
     m.close()
if __name__ == '__main__':
    print(doc_file())
