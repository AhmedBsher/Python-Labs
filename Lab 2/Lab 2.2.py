try:
 s = int (input('Enter your score: '))
except:
 print('Error: please Enter an integer')
 exit()
if s<0 or s>100: print('wrong score')
elif s >= 93: print ('Your grade is A')
elif s >= 89: print ('Your grade is A-')
elif s >= 84: print ('Your grade is B+')
elif s >= 80: print ('Your grade is B')
elif s >= 76: print ('Your grade is B-')
elif s >= 73: print ('Your grade is C+')
elif s >= 70: print ('Your grade is C')
elif s >= 67: print ('Your grade is C-')
elif s >= 64: print ('Your grade is D+')
elif s > 60: print ('Your grade is D')
else: print ('Your grade is F')