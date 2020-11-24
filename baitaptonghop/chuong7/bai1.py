def doc_file():
    with open("f1.txt",mode='r',encoding='utf-8')as f:
        s = f.read()
        f.close()
    return s

if __name__ == "__main__":
    a = doc_file()
    print(f"noi dung cua file la:\n",a)
