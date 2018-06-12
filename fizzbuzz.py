# correct logic but many booleans = slow
def fizzbuzz(x):
	fb_range = []

	for i in range(1, x+1):
		if i%3 == 0 and i%5 == 0:
			fb_range.append('fizzbuzz')
		elif i%3 == 0 and i%5 != 0:
			fb_range.append('fizz')
		elif i%5 == 0 and i%3 != 0:
			fb_range.append('buzz')
		else:
			fb_range.append(i)

	print (str(fb_range))

fizzbuzz(15)

# faster due to less booleans to run - no extra boolean for 'fizzbuzz' condition

def fizzbuzz(x):
	fb_range = []

	for i in range(1, x+1):
		val = ''
		if i%3 == 0:
			val += 'fizz'
		if i%5 == 0:
			val += 'buzz'
		if val == '':
			val
		fb_range.append(val)

	print (str(fb_range))

fizzbuzz(15)

