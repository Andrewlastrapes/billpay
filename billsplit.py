
def check_question():
	return float(input("How much is the check?: "))

def service_question():
	return input("How good was the service? (Good, Fair, Poor: ")

def split_question():	
	return int(input("Split how many ways?: "))





def lower(x):
	return x.lower()


def if_statements_for_bill(service, check, split):
	if service == "good":
		goods = (check * .2) + check
		final1 = round(goods/split, 2)
		print("Each person owes $" + str(final1))
	elif service == "fair":
		fairs = (check * .15) + check
		final2 = round(fairs/split, 2)
		print("Each person owes $" + str(final2))
	elif service == "poor":
		poors = (check * .10) + check
		final3 = round(poors/split, 2)
		print("Each person owes $" + str(final3))
	else:
		print("Invalid response")







def final_bill():
	check = check_question()
	service = service_question()
	split = split_question()
	lower(service)

	if_statements_for_bill(service, check, split)
	

final_bill()






