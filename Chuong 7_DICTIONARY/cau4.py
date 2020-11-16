def sum():
    tinhtong={'a': 1,'b': 2,'c': 3.5,'d': 'hello'}
    tong = 0
    for i in tinhtong:
        if type(tinhtong[i]) == float or type(tinhtong[i]) == int:
            tong+= tinhtong[i]
    print(tong)
if __name__ == '__main__':
    print(sum())
    

