# bai1: Viết một đoạn lệnh cho phép người dùng thêm một khóa vào từ điển. Trong đó khóa và giá trị do người dùng chỉ định:
def them():
    n = str(input('nhap sao key ma ban muon them:\t'))
    k = str(input('nhap vao noi dung cua key ban muon them:\t'))
    my_dict = {
    'name': 'Duck',
    'age': 2
    }
    my_dict[n] = k # cập nhật, tăng giá trị của age lên 1 => age = 3
    print(my_dict)
if __name__ == '__main__':
    print(them())
