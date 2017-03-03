def fizzbuzz(number):
	for x in range(1, number + 1):
		if x % 3 == 0 and x % 5 == 0:
			print "fizzbuzz"

		elif x % 5 == 0:
			print "buzz"

		elif x % 3 == 0:
			print "fizz"

		else:
			print x

def fizzbuzz(number):
	"""
	function description
	"""
	for x in range(1, number + 1):
		output = ""
		if x % 3 == 0:
			output += "fizz"

		if x % 5 == 0:
			output += "buzz"

		if not output:
			output = x

		print output

if __name__ == "__main__":
	fizzbuzz(16)