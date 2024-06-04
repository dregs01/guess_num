import random
x=random.randint (1,100)
while True:
    num = input('請猜數字:')
    num = int(num)
    if num == x :
        print ('你猜中了!')
        break
    elif num > x :
        print ('比數字小')
    else :
        print ('比數字大')
