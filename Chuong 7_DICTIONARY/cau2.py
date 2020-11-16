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
