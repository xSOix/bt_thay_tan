#Bài 3. Viết chương trình ghi thêm nội dung vào một tập tin văn bản đang có trên hệ thống.
def doc_file(n):
    with open("f1.txt",mode='a',encoding='utf-8')as f:
        s = f.write(n)
        f.close()
    return s

if __name__ == "__main__":
    n = input("Nhâp đoạn chuỗi cần thêm: ")
    doc_file(n)
