import os
## function input with range
def rich_num(sentec, max):
    ## initialization num1
    num1 = 0
    ## if < or > (range)
    while num1 < 1 or num1 > max:
        num1 = round(int(input(sentec)),0)
        if num1 < 1 or num1 > max:
            print("invalid number (1-{})".format(max))
    return num1


choose = 0
current_path = '/'.join(os.path.realpath(__file__).split('/')[:-1]) + '/'
while choose != 4:
    choose = rich_num('1) force like\n2) force reblog\n3) force post\n4) exit',4)
    with open('{}./Data/Conv.data'.format(current_path),'w') as f:
        f.write(str(choose))