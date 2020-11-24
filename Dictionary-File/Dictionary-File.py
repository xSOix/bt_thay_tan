#Bài 01: Viết chương trình để đọc n dòng đầu trong 1 file text, với n được nhập từ người dùng
def docfile():
    n = int(input('nhap vao so dong ma ban muon doc:\t'))
    f = open('test1.txt','r')
    for i in range (1,n+1):
        print('dong',i,'cua file la:\t',f.readline())
if __name__ == "__main__":
    print(docfile())



#bai2 viet chuong trinh them 1 chuoi nao do vao cuoi file:
def vietfile():
    n = str(input('nhap vao noi dung ma ban muon them vao:\t'))
    f = open('test1.txt','a')
    f.write(n +'\n')
if __name__ == "__main__":
    print(vietfile())




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



    #bai4 viet ham get siza lay dung luong cua file:
def get_file_size(file):
        import os
        statinfo = os.stat(file)
        return statinfo.st_size
if __name__ == '__main__':
    print("kich thuoc file cua ban la: ",get_file_size("test1.txt"))




    #bai5 viet ham tra tap ki tu trong cac file:
def extract_characters(*file):
   import glob
   chuoi = []
   files_list = glob.glob("test1.txt")
   for f in files_list:
      with open(f, "r") as f:
         chuoi.append(f.read())
   print('cac ki tu trong file cua ban la:\t',chuoi)
if __name__ == '__main__':
    print(extract_characters())




#bai6: viet chuong trinh tao ra 26 file co ten tu a->z.txt
def taofile(): 
      import string, os
      if not os.path.exists("letters"):
         os.makedirs("letters")
      for letter in string.ascii_uppercase:
         with open(letter + ".txt", "w") as f:
            f.writelines(letter)
if __name__ == '__main__':
    print(taofile())




#Bài 07: Đoạn chương trình sau in ra gì?
 #   number = 5.0
 #   try:
 #       r = 10/number
  #      print(r)
  #  except:
  #      print("Oops! Error occurred.")
  =>>>2.0



#Bài 08: Đoạn chương trình sau thực viện việc gì?
#    try:
        # đoạn code có thể gây ra lỗi
#    except (TypeError, ZeroDivisionError):
#        print("Python Quiz")
khi gán giạ trị hay thục hiện nhiêm vụ sai sẽ thực hiện typeerror




#Bài 09: Kết quả output của đoạn chương trình sau là gì?
#    def hoan_function():
 #       try:
 #           print('Monday')
 #       finally:
  #          print('Sunday')
in ra : Monday
        Sunday
        None




#Bài 10: Kết quả của đoạn chương trình sau là gì?
  #  try:
  #      print("throw")
  #  except:
  #      print("except")
 #   finally:
#        print("finally")
in ra:
     throw
     finally

