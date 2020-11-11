                                                    #BAI TAP TREN LOP ====>>>>
#3.1
Hello
 giai thich: do chỉ có mỗi câu lệnh  print đầu là ngoại hàm def trong hàm def nhưng chưa cho hàm in ra hàm đó nên không hiển thị

#3.2
print ('tinh tuoi cua ban')
namsinh = int(input('nhap vao nam sinh cua ban \t'))
namnay = int(input('nhap nam hien tai \t'))
print ('nam sinh cua ban %d' %namsinh)
print ('tuoi cua ban là \t', namnay - namsinh)

#3.3

print ('chuyen doi nhiet do')
dof = int(input('nhap nhiet do F  \t'))
print ('nhietdof %d' %dof)
print ('nhiet do C hom nay la \t', 5*(dof-32)/9)

#3.4

print ("tinh mua trong nam")
gach="----------------------------------------------"
print (gach)


thang=float(input("Nhap vao thang: "))
if (thang <1):
    print ("CHU Y ... thang nhap khong hop le")
    exit (0)
else:
    if (thang <= 3):
        xl = "MUA XUAN"
    elif (thang <= 6):
        xl = "MUA HA"
    elif (thang <= 9):
        xl = "MUA THU"
    else:
        xl="MUA DONG"
print ("hien tai dang la mua: ",xl)


#3.5 
print ("TÌM SỐ LỚN NHẤT TRONG 3 SỐ")
gach="----------------------------------------------"
print (gach)

def max3(a, b, c):
    if a > b and a > c:
        return a
    return b if b > c else c


a = int(input('nhap vao so a:\t'))
b = int(input('nhap vao so b:\t'))
c = int(input('nhap vao so c:\t'))

print('so lon nhat can tim la:',max3(a, b, c))

#3.6
print ("TÍNH DIỆN TÍCH HÌNH TRÒN")
gach="----------------------------------------------"
print (gach)
import math
r = int(input('nhập vào bán kính  \t'))
print ('bankinh %d' %r)
print ('diện tích của hình tròn là: S= \t', math.pi *r*r)


                                                  #-----------BAI TAP TRONG HÌNH  
#1 TIM SO ĐẢO CỦA SỐ N
print ("TÌM SỐ ĐẢO CỦA SÔ N")
gach="----------------------------------------------"
print (gach)
s = input('nhap vao so tu nhien duong:\t')
s = s[::-1] 
print (s) 

#2 TÍNH N!
print ("TÌM GIAI THỪA CỦA N ")
gach="----------------------------------------------"
n = int(input("Nhập số cần tính giai thừa: "))
def giaiThua(n):
    if n == 0:
       
    return n * giaiThua(n - 1)
print ("GIAI THUA CUA SO CAN TIM LA  :  ",giaiThua(n))

#3 TÍNH TỔNG 1^3+2^3 -> N^3
print ("TÍNH TỔNG 1^3+2^3 -> N^3")
gach="====>----------------------------------<======"
print (gach)
tong = 0
n = int(input('moi ban nhap so nguyen duong: \t'))
while not n>0:
    n=int(input('moi ban nhap lai so n duong : \t'))
for i in range (1,n+1):
    tong+= i*i*i
    print ('tổng các số từ 1->n lập phương có kết quả là : \t',tong)

#4 tính tổng các sổ lẻ từ 0 đến n
    print ("tinh tong cac so le tu 1 den n")
gach="----------------------------------------------"
print (gach)
n = int(input('nhap so tu nhien de tinh tong so le;\t'))
tong = 0
for i in range(1, n+1):
    if (i%2!=0) :
        tong += i     
print ('tong của các số lẻ từ 0->n là:',tong)

#5 tính tổng các sổ chẵn từ 0 đến n
    print ("tinh tong cac so le tu 1 den n")
gach="----------------------------------------------"
print (gach)
n = int(input('nhap so tu nhien de tinh tong so chan tu 0 đến sô cần tìm:\t'))
tong = 0
for i in range(1, n+1):
    if (i%2==0) :
        tong += i     
print (tong)

#6 xem n có phải số nguyên tố hay không
print ("kiểm tra n có là số nguyên tố hay không")
gach="----------------------------------------------"
print (gach)
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return print('đây là số nguyên tố')
    return print('đây không phải là số nguyên tố')
n = int(input('nhập số cần kiểm tra: \t'))
print(is_prime(n))


#7 xem n có phải số chính phương hay không
print ("kiểm tra n có là số chính phương hay không")
gach="----------------------------------------------"
print (gach)
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if i*i == n:
            count += 1
    if count == 1:
        return print('đây là số chính phương')
    return print('đây không phải là số chính phương')
n = int(input('nhập số cần kiểm tra: \t'))
print(is_prime(n))

#9 BANG CUU CHUONG VOI N
print ("TAO BANG CUU CHUONG")
gach="----------------------------------------------"
print (gach)
n= int(input('nhap so de hien thi bang cuu chuong:==>\t'))
print ('bang cuu chuong ',n)
print (n,'x 1 =',n)
print (n,'x 2 =',n*2)
print (n,'x 3 =',n*3)
print (n,'x 4 =',n*4)
print (n,'x 5 =',n*5)
print (n,'x 6 =',n*6)
print (n,'x 7 =',n*7)
print (n,'x 8 =',n*8)
print (n,'x 9 =',n*9)
print (n,'x 10 =',n*10)
print('==>-------------------------------<==')


#=========================> ----------------------------BAI TAP GIAO THAG 10---------------------------------<==============

#BAI 01 HAM MAX MIN
print ("ham max min ")
gach="----------------------------------------------"
print (gach)
def max_min(data):
  l = data[0]
  s = data[0]
  for num in data:
    if num> l:
      l = num
    elif num< s:
        s = num
  return l, s

print(max_min([0, 10, 15, 40, -5, 42, 17, 28, 75]))


#BAI 02 TAO CHUOI DAO NGUOC
print ("TÌM CHUOI DAO NGUOC")
gach="----------------------------------------------"
print (gach)
s = input('nhap vao CHUOI BAT KY:\t')
s = s[::-1] 
print ('CHUOI DAO NGUOC KHI NHAP VAO LA:==>\t',s) 


#bai 03 tim so hoan hao
print ("TÌM SO HOAN HAO")
gach="----------------------------------------------"
print (gach)
n = int(input("Nhap vao mot so: "))
def is_perfect(n):
    if n <= 1:
        print(n, " khong phai la so hoan hao")
    else:
        sumDivision = 0
        for i in range(1, n):
        
            if n % i == 0:
                sumDivision += i   
    
        if sumDivision == n:
        
            print(n, " la so hoan hao ==> TRUE")
        else:
        
            print(n, " khong phai la so hoan hao ==>  FAIL")

print(is_perfect(n))


#bai 04 kiem tra so n co phai so nguyen to hay ko
print ("kiểm tra n có là số nguyên tố hay không")
gach="----------------------------------------------"
print (gach)
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return print('đây là số nguyên tố')
    return print('đây không phải là số nguyên tố')
n = int(input('nhập số cần kiểm tra: \t'))
print(is_prime(n))


#bai 05 dem so chu viet thuong va hoa trong chuoi
print ("DEM KY TU VIET THUONG VA VIET HOA TRONG 1 CHUOI")
gach="----------------------------------------------"
print (gach)
def upperlower(string): 
    hoa = 0
    thuong = 0 
    for i in range(len(string)): 
        if (ord(string[i]) >= 97 and
            ord(string[i]) <= 122): 
            thuong += 1
        elif (ord(string[i]) >= 65 and
              ord(string[i]) <= 90): 
            hoa += 1
  
    print('so luong chu viet thuong la:  %s' %thuong)
    print( 'so luong chu viet hoa la:  %s' %hoa) 
string = input('nhap vao CHUOI BAT KY:\t')
upperlower(string)




#bai 06 kiem tra chuoi pangram

import string
def is_pangram (gram):
       gram = gram.lower()
       gram_list_old = sorted([c for c in gram if c != ' '])
       gram_list = []
       for c in gram_list_old:
           if c not in gram_list:
               gram_list.append(c)
       if gram_list == list(string.ascii_lowercase): return True
       else: return False
n= input('nhap chuoi can tim :\t')
print(is_pangram(n))



#bai 07 tao ma tran nhap vao tu ban phim
n = int(input('nhap so hang cua ma tran = '))
m = int(input('nhap so cot cua ma tran = '))
matran = []; cot = []
for i in range(0,n):
  matran += [0]
for j in range (0,m):
  cot += [0]
for i in range (0,n):
  matran[i] = cot
for i in range (0,n):
  for j in range (0,m):
    print ('entry in row: ',i+1,' column: ',j+1)
    matran[i][j] = int(input())
print (matran)



#bai 08 tinh tinh trang BMI cua 1 nguoi
m = int(input('nhap vao can nang:\t'))
h = int(input('nhap vao chieu cao =>don vi cm<= :\t'))
def body_mass_index(m,h):
    k = (h*h)/10000
    tong = m/k
    if tong > 40:
        print('bao phi cap 3')
    if tong >35:
        print('bao phi cap 2')
    if tong >30:
        print('bao phi cap 1')
    if tong >25:
        print('thua can')
    if tong < 24.9:
        print('binh thuong')
    else:
         print('thap gay')

print(body_mass_index(m,h))




#bai09 thay doi ki tu thuong thanh hoa va hoa thanh thuong
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



#bai 10 dem so le trong chuoi

def change_upper_lower(string):
        tong= 0
        i = 0
        while i < len(string):
            if(string[i]%2!=0):
                tong+= 1
                print (tong)

m =input('nhap chuoi can thay doi: \t')
change_upper_lower(m)

