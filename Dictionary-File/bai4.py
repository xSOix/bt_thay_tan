 #bai4 viet ham get siza lay dung luong cua file:
def get_file_size(file):
        import os
        statinfo = os.stat(file)
        return statinfo.st_size
if __name__ == '__main__':
    print("kich thuoc file cua ban la: ",get_file_size("test1.txt"))
