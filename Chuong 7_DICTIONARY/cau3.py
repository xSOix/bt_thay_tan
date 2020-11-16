#cau3: Viết chương trình xóa một phần tử với khóa cho trước khỏi từ điển. Xuất lại từ điển sau khi xóa
def xoakey():
    thongtin ={'a': 1,'b': 2,'c': 3.5,'d': 'hello'}
    del thongtin['c']
    print(thongtin)
if __name__ == '__main__':
    print(xoakey()) 
