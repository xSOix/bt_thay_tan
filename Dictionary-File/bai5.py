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
