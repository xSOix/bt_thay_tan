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
