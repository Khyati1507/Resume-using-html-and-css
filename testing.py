a='y'
while a=='y':
    print('Big Billion Days SALE')
    pa=float(input('enter purchase amount'))
    ad=0
    if pa>20000:
        dis=2000
    elif pa>10000:
        dis=1000
    elif pa>5000:
        dis=800
    elif pa>450:
        dis=400
    else:
        print('enter correct data')
    if pa>20000:
        ad=pa*3/100
    td=dis+ad
    na=pa-td
    print('======================')
    print('purchase amt is:%8.2f'%pa)
    print('discount amt is:%6.2f'%dis)
    print('additional discount on %8.2f is:%6.2f'%(pa,ad))
    print('net payable amt is:%9.2f'%na)
    a=input('want to calculate again(y/n)').lower
    
