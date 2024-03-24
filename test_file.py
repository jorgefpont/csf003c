def doubleDigits1(num):
   if num < 0:
      return - doubleDigits1(-num)
   elif num == 0:
      return 0
   else:
      digit = num % 10
      rest = num // 10
      return doubleDigits1(rest)

def doubleDigits2(num):
   if num < 0:
      return - doubleDigits2(-num)
   elif num == 0:
      return 0
   else:
      digit = num % 10
      rest = num // 10
      return digit + 10 * digit + 100 * doubleDigits2(rest)

def doubleDigits3(num):
   if num == 0:
      return 1
   elif num < 0:
      return - doubleDigits3(-num)
   else:
      digit = num % 10
      rest = num // 10
      return digit + 10 * digit + 100 * doubleDigits3(rest)

def doubleDigits4(num):
   if num < 0:
      return - doubleDigits4(-num)
   elif num == 0:
      return 1
   else:
      rest = num % 10
      digit = num // 10
      return digit + 10 * digit + 100 * doubleDigits4(rest)

n=-321
print('1:', doubleDigits1(n))
print('2:',doubleDigits2(n))
print('3:',doubleDigits3(n))
print('4:',doubleDigits4(n))