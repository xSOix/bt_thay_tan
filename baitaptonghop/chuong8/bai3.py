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
