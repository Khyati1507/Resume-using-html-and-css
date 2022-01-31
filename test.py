members = ['swapnil', 'aryan', 'ut', 'pankaj', 'shivam', 'harsh', 'umesh']
members = list(map(str.lower, members))

def calculate_discount(amount, name):
	total_discount = 0

	if name in members:
		total_discount += 5

	if amount >= 2000:
		total_discount += 10
	elif amount >= 1000:
		total_discount += 8
	elif amount >= 500:
		total_discount += 5

	return total_discount

#main
member_name = input("Enter your name: ").lower()
amount = int(input("Enter shopping amount: "))
total_discount = calculate_discount(amount, member_name)

if total_discount > 0:
	print("You are eligible for", total_discount, "\b% discount and your total amount is", amount - (total_discount/100)*amount)
else:
	print("Sorry, you're not eligible for any discount, therefore your total amount is", amount)
