hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
float(1.5)
if hours == int or rate == int:
    if float(hours) > 40.0:
        rate1 = float(hours) - 40.0
        rate4 = float(rate) * 1.5
        rate2 = rate1 * rate4
        rate3 = float(hours) * float(rate) + float(rate2)
        print(rate3)
    else:
        pay = float(hours) * float(rate)
        print(pay)
else:
    print('Please Input a Number')
