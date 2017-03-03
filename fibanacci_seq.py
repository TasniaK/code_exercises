def fibanacci_seq(u):
	count = []
	count.append(1)
	count.append(1)
	for x in range(2, u):
		count.append(count[x-1] + count[x-2])

	print count


if __name__ == "__main__":
	fibanacci_seq(11)

		