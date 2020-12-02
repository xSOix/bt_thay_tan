#Bài 06: Viết chương trình in ra phần tử thứ 4 và phần tử thứ 4 từ cuối lên trong một tuple.
def intupbe(a):
    b = list(a)
    print(b[0])
    print(b[len(b)-4])

if __name__ == "__main__":
    a=(1,5,9,7,'soi','shiho','python',198,222)
    intupbe(a)