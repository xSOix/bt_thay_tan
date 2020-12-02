def timphantu():    
    k=[(1,5,6),(5,2,7),(8,0,1),(1,6,8),(7,8,1,2),(1,3,8,9)]
    a=list(k)
    b=[]
    c=[]
    for i in a:
        for j in i:
            if j<i[1]:
                b.append(i)
    for i in a:
        if i not in b:
            print('list co phan tu thu 2 nho nhat la:\t',i)

if __name__ == "__main__":
    timphantu()            

            
