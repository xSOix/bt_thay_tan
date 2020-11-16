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



#Câu 2. Viết đoạn lệnh để kiểm tra xem một khóa có nằm trong từ điển không. 
# Nếu có, xuất ra “Tồn tại giá trị trong từ điển với giá trị là v” với v là giá trị có trong từ điển. Nếu không, xuất ra là “Không có khóa k trong từ điển” với k là khóa đã nhập.
#Câu 2. Viết đoạn lệnh để kiểm tra xem một khóa có nằm trong từ điển không. 
#cau2 Nếu có, xuất ra “Tồn tại giá trị trong từ điển với giá trị là v” với v là giá trị có trong từ điển. Nếu không, xuất ra là “Không có khóa k trong từ điển” với k là khóa đã nhập.
def timkey():
    my_dict = {
        'name': 'Duck',
        'age': 2,
        
        }
    n = str(input('nhap vao key ban muon tim:\t'))
    if n in my_dict:
        print('key ban muon tim co trong my_dict:\t',n)
    else:
        print('key ban muon tim khong co trong my_dict:\t',n)
if __name__ == '__main__':
    print(timkey())





#cau3: Viết chương trình xóa một phần tử với khóa cho trước khỏi từ điển. Xuất lại từ điển sau khi xóa
 def xoakey():
    thongtin ={'a': 1,'b': 2,'c': 3.5,'d': 'hello'}
    del thongtin['c']
    print(thongtin)
if __name__ == '__main__':
    print(xoakey()) 




#Câu 4. Viết chương trình tính tổng các giá trị là số nguyên có trong từ điển
def sum():
    tinhtong={'a': 1,'b': 2,'c': 3.5,'d': 'hello'}
    tong = 0
    for i in tinhtong:
        if type(tinhtong[i]) == float or type(tinhtong[i]) == int:
            tong+= tinhtong[i]
    print(tong)
if __name__ == '__main__':
    print(sum())
    


       