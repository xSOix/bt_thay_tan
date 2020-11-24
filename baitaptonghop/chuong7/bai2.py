#bai2:Viết chương trình đọc một danh sách các số được ghi trong một tập tin văn bản, 
# với mỗi số cách nhau bằng dấu khoảng trắng. Hiển thị danh sách ra màn hình và 
# tính tổng các số đó.
def doc_file():
    with open("so.txt",mode='r',encoding='utf-8')as f:
        s = f.read()
        f.close()
    return s
def tong():
    tong = 0
    string = doc_file()
    a = string.split(" ")
    for i in a:
        tong = tong + float(i)
    return tong
if __name__ == "__main__":
    doc_file()
    print("tong cua cac so trong file la: \n",tong())
