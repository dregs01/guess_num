import random

start = input ('輸入開始範圍:')
end = input ('輸入結束範圍')
start = int(start)
end=int(end)

x=random.randint (start,end)
count = 0
while True:
    count += 1
    num = input('請猜數字:')
    num = int(num)
    if num == x :
        print ('你猜中了!')
        print ('這是您猜的第',count,'次')
        break
    elif num > x :
        print ('比數字小')
    else :
        print ('比數字大')
    print ('這是您猜的第',count,'次')