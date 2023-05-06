import math

menu = {
    "Americano S": 1.49,
    "Americano M": 1.99,
    "Americano L": 2.49,
    "Americano XL": 2.99,
    "Caffe Latte S": 2.49,
    "Caffe Latte M": 2.99,
    "Caffe Latte L": 3.49,
    "Caffe Latte XL": 3.99,
    "Cappuccino S": 2.59,
    "Cappuccino M": 3.09,
    "Cappuccino X": 3.59,
    "Cappuccino XL": 4.09,
    "Latte Caramel S": 2.99,
    "Latte Caramel M": 3.49,
    "Latte Caramel L": 3.99,
    "Latte Caramel XL": 4.49
}

receipt = {

}

print("*** COFFEE SHOP ****")
print("~~~*** Hello in our Coffee Shop ***~~~")
print("Let's order your coffee")

while True:
	menutypes = []
	for r in menu:
		menutype = r.split(" ")
		coffeename = menutype[0]
		ml = len(menutype)
		mi = 1
		while mi < ml-1:
			coffeename = coffeename + " " + menutype[mi]
			mi += 1
		if coffeename not in menutypes:
			menutypes.append(coffeename)
		#print(coffeename)
	print(menutypes)
		

			


	i = 0
	for r in menutypes:
		print(i, ": ", menutypes[i])
		i += 1

	selectedcoffee = ""
	selectedsize = ""

	while True:

		coffeetype = input(f"Select the number of your coffee type from 0 to {len(menutypes)-1}:")
		coffeetypeint = ""

		try:
			coffeetypeint = int(coffeetype)
			if coffeetypeint > len(menutypes)-1:
				print("you picked the wrong number if the coffee - Try again")
			else:
				print("Success")
				print(coffeetypeint)
				selectedcoffee = menutypes[coffeetypeint]
				print(f"You picked: {menutypes[coffeetypeint]}")
				break
		except ValueError:
			print("Please pick a number")

	while True:
		productsizes = []
		for r in menu:
			if selectedcoffee in r:
				splr = r.split(" ")
				productsizes.append(splr[-1])
				print(splr[-1])
			

		coffeesize = input(f"Select the size of your coffee: {str(productsizes)}")

		#try:
		if coffeesize in productsizes:
			selectedsize = coffeesize
			break
		else:
			print("You selected incorrect coffee size - try again")
		#except



	selectedproduct = f"{selectedcoffee} {selectedsize}"
	print(selectedproduct)
	getprice = menu[selectedproduct]

	print(f"This is your selected product: {selectedproduct}")
	print(f"Price for {selectedproduct} is {getprice}")

	receipt[selectedproduct] = getprice

	addanotherprod = ""
	while True:
		addanotherprod = input("""Do you want to order something else? 
				- Click "Y" for Yes
				- Click "N" for No
				""")
		print(addanotherprod)
		if addanotherprod != "Y" and addanotherprod != "N":
			print("Wrong value was selected. Please type Y or N for this question")
		else:
			break

	if addanotherprod == "Y":
		print("Ok, let's order something else :")
	else:
		i = 1
		print("-------------------------------------------------------")
		print("Thank you! These are your selected products:")
		print("-------------------------------------------------------")
		for name, price in receipt.items():
			print(f"{i} - {name} - {price}")
			i += 1
		totalprice = sum(receipt.values())
		print("-------------------------------------------------------")
		print(f"TOTAL TO PAY: {totalprice}")
		print("-------------------------------------------------------")
		break

