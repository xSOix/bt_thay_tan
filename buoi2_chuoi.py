                                    #-----phan bai tap trong hinh ------------------
#Bài 01: Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $.
a = input('nhap chuoi : \t')
print(a.replace(a[0],'$')) 


#Bài 02: Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
a = input('nhap chuoi : \t')
m=int(input('nhap vi tri chuoi ban muon xoa: \t'))
print(a.replace(a[m],'')) 


#Bài 03: Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi
a= input('nhap chuoi: \t')
m=len(a)
for i in range(1,m+1):
      if (i%2!=0) :
        print('chuoi da dc thay doi thanh:\t',a.replace(a[i],'')) 


#Bài 04: Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào,  nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.
a=input('nhap vao chuoi: \t')
if(len(a)<=2):
    print('chuoi qua ngan vui long nhap lai')
    exit()
else:
    b= len(a)
    print('2 ki tu dau la=>>:',a[0],a[1],'  hai ki tu cuoi la=>>:',a[-2:])
    


#Bài 05: Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.
a=input('nhap vao chuoi: \t')
print('ki tu lon nhat la=>>:  ',a[-1:], ' ki tu nho nhat la=>>:  ',a[0])



#Bài 06: Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.
def change_upper_lower(string):
        i = 0
        while i < len(string):
            if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] =='u':
                print(string[i].upper())
                i = i + 1
            else:
                print(string[i].lower())
                i = i + 1

m =input('nhap chuoi can thay doi: \t')
change_upper_lower(m)