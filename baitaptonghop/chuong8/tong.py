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




#Bài 2.  Viết đoạn lệnh để kiểm tra xem một khóa có nằm trong từ điển không. 
# Nếu có, xuất ra “Tồn tại giá trị trong từ điển với giá trị là v” với v là giá trị có trong từ điển.
#  Nếu không,  xuất ra là “Không có khóa k trong từ điển” với k là khóa đã nhập.
def check_dict(dict,key):
    if key in dict:
        return 1
    return -1

def nhap_dl():
    n = input("Nhập vào dữ liệu: ")
    if n.isnumeric():
        number = int(n)
    else:
        number = n
    return number

if __name__ == "__main__":
    dictionary = {'a': 1, 'b': 2}
    print("Nhập key cần tìm: ")
    key = nhap_dl()
    kq = check_dict(dictionary,key)
    if kq == 1:
        print(f"Phần tử key {key} cần tìm có trong từ điển là {dictionary[key]}")
    else:
        print(f"Không tìm thấy key {key} trong từ điển")



#Bài 3.  Viết chương trình xóa một phần tử với khóa cho trước khỏi từ điển.
#  Xuất lại từ điển sau khi xóa.
def check_dict(dict,key):
    if key in dict:
        del dict[key]
        return dict
    return -1

def nhap_dl():
    n = input("Nhập vào dữ liệu: ")
    if n.isnumeric():
        number = int(n)
    else:
        number = n
    return number
if __name__ == "__main__":
    dictionary = {'a': 1, 'b': 2, 'c': 3.5, 'd': 'hello'}
    print("Nhập key cần xóa: ")
    key = nhap_dl()
    kq = check_dict(dictionary,key)
    if kq:
        print(f"Phần tử key {key} vừa xóa trong từ điển {dictionary}")
    else:
        print(f"Không tìm thấy key {key} cần xóa trong từ điển")
