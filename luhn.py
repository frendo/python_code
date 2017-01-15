#!/usr/bin/python

def main():
	while True:
		CCnumbers = generateBaseNum() 
	
			##print("card",CCnumbers)
		checkDig = calcLastNum(CCnumbers)
		print(''.join(map(str, CCnumbers)) + str(checkDig))

def generateBaseNum():
## this generates the numbers for the credit card except the check digit 
	CCnumbers = [3,4] ## american express 15 length starts with 34/37
	for i in range(0, 12):	
		CCnumbers.append(random.randint(0, 9))
	return CCnumbers

def calcLastNum(CCnumbers):
## this calculates the check digit 
	base = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
	outcome = []
	total = 0 
	checksum = 0

	##print("base",base)
	
	## If the sum is greater than 9 add the two bases together  
	for x in range(0, 14):
		temp = CCnumbers[x] * base[x]
		if temp > 9:
			temp2 = map(int, str(temp))
			temp = temp2[0] + temp2[1]
		outcome.append(temp)

	##print("sum ",outcome)

	for i in range(0, 14):
		total = outcome[i] + total
	##print("total", total)	

	while total % 10 != 0:
		checksum = checksum + 1
		total = total + 1
	return(checksum)  

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
