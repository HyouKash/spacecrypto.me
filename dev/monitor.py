import requests 

crypto_list = ["LTC 0.606 3 147.05", "EGLD 0.6 2 319.520", "CHZ 388 2 0.37037", "MANA 18 3 3.3009"]

def actu_wallet(crypto_list):
	prout = []
	total_price = 0
	total_price_levarage = 0
	for k in crypto_list:
		crypto_wallet_allinfo = ""
		s = k.split(" ")
		crypto, amount, levarage, purchased_price = s[0],s[1], s[2], s[3]
		r = requests.get(f"https://api.coin360.com/coin/latest?coin={crypto}&convert=USD")
		price = (r.text).split(",")[3].split(":")[-1:][0]
		crypto_wallet = float(purchased_price) * (float(amount) / int(levarage))
		pourcentage_baisse = float(price) / float(purchased_price)
		if pourcentage_baisse > 1:
			if pourcentage_baisse > 2:
				pourcentage_baisse = str(pourcentage_baisse)[0:4].split(".")[0] + str(pourcentage_baisse)[0:4].split(".")[1]
			else:
				pourcentage_baisse = str(pourcentage_baisse)[2:4]
				if pourcentage_baisse[0] == "0":
					pourcentage_baisse = pourcentage_baisse[1]
				else:
					pass 
			pourcentage_baisse = "+" + pourcentage_baisse
		else:
			pourcentage_baisse = str(1 - float(pourcentage_baisse))[2:4]
			if pourcentage_baisse[0] == "0":
				pourcentage_baisse = pourcentage_baisse[1]
			else:
				pass
			crypto_wallet -= (crypto_wallet * int(pourcentage_baisse)) / 100
			pourcentage_baisse = "-" + pourcentage_baisse
		if levarage != 1:
			crypto_wallet *= (int(pourcentage_baisse) * int(levarage)) / 100 + 1
			pourcentage_baisse = int(pourcentage_baisse) * int(levarage)
		else:
			pass
		crypto_wallet_allinfo += crypto + " " + price + " " + amount + " " + levarage + " " + str(crypto_wallet) + " " + str(pourcentage_baisse) + " " + str(crypto_wallet * int(levarage)) 
		prout.append(crypto_wallet_allinfo)
	for final in prout:
		temp = final.split(" ")
		total_price += float(temp[4])
		total_price_levarage += float(temp[6])
		print(f"{temp[0]} | Price = {temp[1]} | Amount = {temp[2]} | with levarage of {temp[3]} | Sold = {temp[4]} | {temp[5][:4]} % | Sold with levarage = {temp[6]}") 
	print(f"Total sold without levarage : {total_price} $\nTotal sold with levarage : {total_price_levarage} $")
	

actu_wallet(crypto_list)