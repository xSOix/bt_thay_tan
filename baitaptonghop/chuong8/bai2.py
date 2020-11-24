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