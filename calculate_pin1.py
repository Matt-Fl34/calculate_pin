start_pin = '000'

def calc_pin():
    x = 0
    while x == 0:
        usr_pin = input('Please enter 3 digit pin: ')
        if usr_pin.isdigit() and len(usr_pin) == 3:
            test = usr_pin
            x = 1
        else:
            print('Incorrect. Try again.')
   
    
    global start_pin
    answ_one = ''
    up_one = '1st digit: up '
    down_one = '1st digit: down '
    start = int(start_pin[0:1])
    test_digit = int(test[0:1])
    up_ct = 0
    y = 0  
    
    while y == 0:
        if test_digit == start:
            up_one += str(up_ct)
            y = 1
        elif start == 9:
            start = 0
            up_ct += 1
        else:
            start += 1
            up_ct += 1
            
    
    start = int(start_pin[0:1])
    down_ct = 0
    z = 0
    
    while z == 0:
        if test_digit == start:
            down_one += str(down_ct)
            z = 1
        elif int(start) == 0:
            start = 9
            down_ct += 1
        else:
            start -= 1
            down_ct += 1
            
    if down_ct > up_ct:
        answ_one = up_one
    elif down_ct < up_ct:
        answ_one = down_one
    elif down_ct == 0:
        answ_one = '1st digit: No Adjustment Needed.'
    else:
        answ_one = '1st digit: Five Adjustments Either Way'
        
        
    answ_two = ''
    up_two = '2nd digit: up '
    down_two = '2nd digit: down '
    start = int(start_pin[1:2])
    test_digit = int(test[1:2])
    up_ct = 0
    y = 0  
    
    while y == 0:
        if test_digit == start:
            up_two += str(up_ct)
            y = 1
        elif start == 9:
            start = 0
            up_ct += 1
        else:
            start += 1
            up_ct += 1
            
    
    start = int(start_pin[1:2])
    down_ct = 0
    z = 0
    
    while z == 0:
        if test_digit == start:
            down_two += str(down_ct)
            z = 1
        elif int(start) == 0:
            start = 9
            down_ct += 1
        else:
            start -= 1
            down_ct += 1
            
    if down_ct > up_ct:
        answ_two = up_two
    elif down_ct < up_ct:
        answ_two = down_two
    elif down_ct == 0:
        answ_two = '2nd digit: No Adjustment Needed.'
    else:
        answ_two = '2nd digit: Five Adjustments Either Way'
        
        
    answ_three = ''
    up_three = '3rd digit: up '
    down_three = '3rd digit: down '
    start = int(start_pin[2:3])
    test_digit = int(test[2:3])
    up_ct = 0
    y = 0  
    
    while y == 0:
        if test_digit == start:
            up_three += str(up_ct)
            y = 1
        elif start == 9:
            start = 0
            up_ct += 1
        else:
            start += 1
            up_ct += 1
            
    
    start = int(start_pin[2:3])
    down_ct = 0
    z = 0
    
    while z == 0:
        if test_digit == start:
            down_three += str(down_ct)
            z = 1
        elif int(start) == 0:
            start = 9
            down_ct += 1
        else:
            start -= 1
            down_ct += 1
            
    if down_ct > up_ct:
        answ_three = up_three
    elif down_ct < up_ct:
        answ_three = down_three
    elif down_ct == 0:
        answ_three = '3rd digit: No Adjustment Needed.'
    else:
        answ_three = '3rd digit: Five Adjustments Either Way'
    
    print()
    print('Starting Postition is:', start_pin)
    print('Your PIN is:', test)
    print()
    print('The Quickest Way to Rotate in Order to Achieve Your PIN is:')
    print()
    print(answ_one)
    print(answ_two)
    print(answ_three)
    print()
    
    start_pin = test
        

    
    
