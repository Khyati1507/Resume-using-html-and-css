amount=int(input('Enter the purchased amount'))
if amount >=10000:
    discount=amount*0.10
else :
    discount=amount*0.05
netamount=amount-discount
print('Discount=', discount)
print('Amount to be paid', netamount)