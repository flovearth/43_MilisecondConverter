user_number = input('\nPlease enter: ')
int_user_number = int(user_number)
minut = 0
second = 0
minut_remain = 0
def converter(args):
    hour = int_user_number // 3600000
    hour_remain = int_user_number % 3600000
    if hour_remain > 60000:
        global minut
        global minut_remain
        minut = hour_remain // 60000
        minut_remain = hour_remain % 60000
        if minut_remain > 1000:
            global second
            second = minut_remain // 1000
        else:
            second = minut_remain // 1000
    elif 1000 > hour_remain > 60000:
        second = minut_remain % 1000
    else:
        minut = hour_remain // 60000
    print(hour, ' hours')
    print(minut, 'minutes')
    print(second, 'seconds')
    print('\nint_user_number: ', int_user_number)
    print('hour', hour)
    print('hour_remain:', hour_remain)
    print('minut', minut)
    print('minut_remain', minut_remain)
    print('second', second)

converter(int_user_number)

