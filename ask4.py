


number = raw_input("Give a number")
while type(number) <> int and number > 1000000 and number< 1 : 
		number = raw_input("Please input an integer between 1 and 1000000")
roman = 0
if number == 1000000 :
		roman = 1000 * 'M'
elif number > 99999 : 
		first = number / 100000
		second = (number%100000)/ 10000
		third =  ((number%100000)%10000)/ 1000
		fourth = (((number%100000)%10000)%1000)/ 100
		fifth = ((((number%100000)%10000)%1000)%100)/ 10
		sixth = (((((number$100000)%10000)%1000)%100)%10)
		roman = ('M' * 100 * first) + ('M' * 10 * second) + ('M' * third)
		if fourth == 9 :
					roman = roman + 'CM'
			elif fourth == 8  or fourth == 4 : 
					roman = roman + ((fourth/4) * 'CD')
			elif fourth == 7 :
					roman = roman + 'D' + (2 * 'C')
			elif fourth == 6 :
					roman = roman + 'D' + 'C'
			elif fourth == 5 :
					roman = roman + 'D'
			else :
				roman = roman + (fourth * 'C') 
			
		if  fifth == 9 :
				roman = roman + 'XC'
			elif fifth == 8  or fifth == 4 : 
					roman = roman + ((fifth/4) * 'XL')
			elif fifth == 7 :
					roman = roman + 'L' + (2 * 'X')
			elif fifth == 6 :
					roman = roman + 'L' + 'X'
			elif fifth == 5 :
					roman = roman + 'L'
			else :
				roman = roman + (fifth * 'X')
				
		if  sixth == 9 :
				roman = roman + 'IX'
			elif sixth == 8  or sixth == 4 : 
					roman = roman + ((sixth/4) * 'IV')
			elif sixth == 7 :
					roman = roman + 'V' + (2 * 'I')
			elif sixth == 6 :
					roman = roman + 'V' + 'I'
			elif sixth == 5 :
					roman = roman + 'V'
			else :
				roman = roman + (sixth * 'I')	
elif number > 9999 : 	
		first = number / 10000
		second = (number%10000)/ 1000
		third =  ((number%10000)%1000)/ 100
		fourth = (((number%10000)%1000)%100)/ 10
		fifth = ((((number%10000)%1000)%100)%10)
		roman = (first * 10 * 'M') + (second * 'M')
			if third == 9 :
					roman = roman + 'CM'
			elif third == 8  or third == 4 : 
					roman = roman + ((third/4) * 'CD')
			elif third == 7 :
					roman = roman + 'D' + (2 * 'C')
			elif third == 6 :
					roman = roman + 'D' + 'C'
			elif third == 5 :
					roman = roman + 'D'
			else :
				roman = roman + (third * 'C') 
			
		if  fourth == 9 :
				roman = roman + 'XC'
			elif fourth == 8  or fourth == 4 : 
					roman = roman + ((fourth/4) * 'XL')
			elif fourth == 7 :
					roman = roman + 'L' + (2 * 'X')
			elif fourth == 6 :
					roman = roman + 'L' + 'X'
			elif fourth == 5 :
					roman = roman + 'L'
			else :
				roman = roman + (fourth * 'X')
				
		if  fifth == 9 :
				roman = roman + 'IX'
			elif fifth == 8  or fifth == 4 : 
					roman = roman + ((fifth/4) * 'IV')
			elif fifth == 7 :
					roman = roman + 'V' + (2 * 'I')
			elif fifth == 6 :
					roman = roman + 'V' + 'I'
			elif fifth == 5 :
					roman = roman + 'V'
			else :
				roman = roman + (fifth * 'I')	
elif number > 999 : 
		first = number / 1000
		second = (number%1000)/ 100
		third =  ((number%1000)%100)/ 10
		fourth = (((number%1000)%100)%10)
		roman = first * 'M'
			if second == 9 :
					roman = roman + 'CM'
			elif second == 8  or second == 4 : 
					roman = roman + ((second/4) * 'CD')
			elif second == 7 :
					roman = roman + 'D' + (2 * 'C')
			elif second == 6 :
					roman = roman + 'D' + 'C'
			elif second == 5 :
					roman = roman + 'D'
			else :
				roman = roman + (second * 'C') 
			
		if  third == 9 :
				roman = roman + 'XC'
			elif third == 8  or third == 4 : 
					roman = roman + ((third/4) * 'XL')
			elif third == 7 :
					roman = roman + 'L' + (2 * 'X')
			elif third == 6 :
					roman = roman + 'L' + 'X'
			elif third == 5 :
					roman = roman + 'L'
			else :
				roman = roman + (third * 'X')
				
		if  fourth == 9 :
				roman = roman + 'IX'
			elif fourth == 8  or fourth == 4 : 
					roman = roman + ((fourth/4) * 'IV')
			elif fourth == 7 :
					roman = roman + 'V' + (2 * 'I')
			elif fourth == 6 :
					roman = roman + 'V' + 'I'
			elif fourth == 5 :
					roman = roman + 'V'
			else :
				roman = roman + (fourth * 'I')
elif number > 99 :
		first = number / 100
		second = (number%100)/ 10
		third =  ((number%100)%10)
		if first == 9 :
					roman = roman + 'CM'
			elif first == 8  or first == 4 : 
					roman = roman + ((first/4) * 'CD')
			elif first == 7 :
					roman = roman + 'D' + (2 * 'C')
			elif first == 6 :
					roman = roman + 'D' + 'C'
			elif first == 5 :
					roman = roman + 'D'
			else :
				roman = roman + (first * 'C') 
			
		if  second == 9 :
				roman = roman + 'XC'
			elif second == 8  or second == 4 : 
					roman = roman + ((second/4) * 'XL')
			elif second == 7 :
					roman = roman + 'L' + (2 * 'X')
			elif second == 6 :
					roman = roman + 'L' + 'X'
			elif second == 5 :
					roman = roman + 'L'
			else :
				roman = roman + (second * 'X')
				
		if  third == 9 :
				roman = roman + 'IX'
			elif third == 8  or third == 4 : 
					roman = roman + ((third/4) * 'IV')
			elif third == 7 :
					roman = roman + 'V' + (2 * 'I')
			elif third == 6 :
					roman = roman + 'V' + 'I'
			elif third == 5 :
					roman = roman + 'V'
			else :
				roman = roman + (third * 'I')
elif number > 9 :
		first = number / 10
		second = (number%10)
		if  first == 9 :
				roman = roman + 'XC'
			elif first == 8  or first == 4 : 
					roman = roman + ((first/4) * 'XL')
			elif first == 7 :
					roman = roman + 'L' + (2 * 'X')
			elif first == 6 :
					roman = roman + 'L' + 'X'
			elif first == 5 :
					roman = roman + 'L'
			else :
				roman = roman + (first * 'X')
				
		if  second == 9 :
				roman = roman + 'IX'
			elif second == 8  or second == 4 : 
					roman = roman + ((second/4) * 'IV')
			elif second == 7 :
					roman = roman + 'V' + (2 * 'I')
			elif second == 6 :
					roman = roman + 'V' + 'I'
			elif second == 5 :
					roman = roman + 'V'
			else :
				roman = roman + (second * 'I')
else : 
	if  number == 9 :
				roman = roman + 'IX'
			elif number == 8  or number == 4 : 
					roman = roman + ((number/4) * 'IV')
			elif number == 7 :
					roman = roman + 'V' + (2 * 'I')
			elif number == 6 :
					roman = roman + 'V' + 'I'
			elif number == 5 :
					roman = roman + 'V'
			else :
				roman = roman + (number * 'I')	
				
print (roman) 
	
			
			
		
				