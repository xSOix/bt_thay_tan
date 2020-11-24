#Bài 1. Viết một đoạn lệnh cho phép người dùng thêm một khóa vào từ điển. 
# Trong đó khóa và giá trị do người dùng chỉ định:
def nhap_dl():
    n = input("Nhập vào dữ liệu: ")
    if n.isnumeric():
        number = int(n)
    else:
        number = n
    return number

def them_pt(dict,key,value):
    dict[key] = value
    return dict

if __name__ == "__main__":
    dictionary = {0: 10, 1: 20}
    print("nhap key:")
    key = nhap_dl()
    print("nhap value:")
    value = nhap_dl()
    kq = them_pt(dictionary,key,value)
    print(f"Phần tử sau khi thêm {dictionary}")

