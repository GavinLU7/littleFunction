num = 0
count = 0
symbol = ''
sum1 = 0
while num != '':
        num = float(num)
        count += 1
        if count % 10 > 3 or count //10 == 1 or count % 10 == 0:
                symbol = 'th'
        elif count % 10 == 1:
                symbol = 'st'
        elif count % 10 == 2:
                symbol = 'nd'
        else:
                symbol = 'rd'
        num = input('Please input the '+ str(count) + symbol + ' number: ')
        isnum = False
        while not isnum  and num != '':
                preventError = num
                
                if preventError.find('-') == 0 :
                        preventError = list(preventError)
                        preventError.remove('-')
                        preventError = ''.join(preventError)
                if preventError.find('.') > 0 :
                        preventError = list(preventError)
                        preventError.remove('.')
                        preventError = ''.join(preventError)
                isnum = preventError.isnumeric()
		
                if not isnum:
                        num = input('You enter wrong number form!\nPlease input the '+ str(count) + symbol + ' number: ')
        if num != '':
                sum1 += float(num)
		
print('Your input', count - 1, 'numbers')
#print(list1)
print('sum of numbers:%.3f'%sum1)
print('Average of numbers:%.3f'%(sum1/(count - 1)))
