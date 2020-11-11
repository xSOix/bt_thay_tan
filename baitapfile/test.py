#Bài 01: Viết chương trình để đọc n dòng đầu trong 1 file text, với n được nhập từ người dùng\
def doc_file():
     b=[]
     n = int(input('nhap so dong ma ban muon doc:\t'))
     f = open("abc.txt",'r', encoding='utf8')
     b = f.readlines()
     print(b[n-1])
     f.close()
if __name__ == '__main__':
    print(doc_file())


#Bài 02: Viết chương trình thêm một chuỗi nào đó vào cuối file
def themfile():
     n = str(input('nhap so dong ma ban muon doc:\t'))
     with open("abc.txt",'a', encoding='utf8') as f:
        f.write(n+'\n')
     f.close()
if __name__ == '__main__':
    print(themfile())



#Bài 03: Viết chương trình trộn 2 file thành file mới
def doc_file():
     b=[]
     f = open("abc.txt",'r', encoding='utf8')
     b = f.readlines()
     f.close()
     c=[]
     k = open("file1.txt",'r', encoding='utf8')
     c = k.readlines()
     f.close()
     t= str
     t = b + c
     m = open("filetong.txt",'a', encoding='utf8') 
     m.write(t)
     m.close()
if __name__ == '__main__':
    print(doc_file())



#Bài 04: Viết hàm   def get_file_size(file)   để lấy và trả về dung lượng của file
def get_file_size(file):
        import os
        statinfo = os.stat(file)
        return statinfo.st_size
if __name__ == '__main__':
    print("kich thuoc file cua ban la: ",get_file_size("file1.txt"))


#Bài 05: Viết hàm    def extract_characters(*file)   trả lại tập các ký tự trong các file
def extract_characters(*file):
   import glob
   chuoi = []
   files_list = glob.glob("abc.txt")
   for f in files_list:
      with open(f, "r") as f:
         chuoi.append(f.read())
   print('cac ki tu trong file cua ban la:\t',chuoi)
if __name__ == '__main__':
    print(extract_characters())



#Bài 06: Viết chương trình tạp ra 26 file text có tên lần lượt từ A.txt, B.txt đến Z.txt
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








