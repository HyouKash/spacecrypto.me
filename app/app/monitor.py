import requests

def actu_wallet(crypto_list):
        prout = []
        total_price = 0
        total_price_levarage = 0
        for k in crypto_list:
                crypto_wallet_allinfo = ""
                s = k.split("|")
                crypto, amount, levarage, purchased_price = s[0],s[1], s[2], s[3]
                r = requests.get(f"https://api.coin360.com/coin/latest?coin={crypto}&convert=USD")
                price = (r.text).split(",")[3].split(":")[-1:][0]
                crypto_wallet = float(purchased_price) * (float(amount) / int(levarage))
                pourcentage_baisse = float(price) / float(purchased_price)
                crypto_wallet *= pourcentage_baisse
                if levarage != 1:
                        crypto_wallet *= (int(pourcentage_baisse) * int(levarage)) / 100 + 1
                        pourcentage_baisse = int(pourcentage_baisse) * int(levarage)
                else:
                        pass
                crypto_wallet_allinfo += crypto + " " + price + " " + amount + " " + levarage + " " + str(crypto_wallet).split(".")[0] + " " + str(pourcentage_baisse) + " " + str(crypto_wallet * int(levarage)).split(".")[0] 
                prout.append(crypto_wallet_allinfo)
        repfinal = []
        for final in prout:
                temp = final.split(" ")
                total_price += float(temp[4])
                total_price_levarage += float(temp[6])
                repfinal.append(f"{temp[0]} | Price = {temp[1]} | Amount = {temp[2]} | with levarage of {temp[3]} | Sold = {temp[4]} | {temp[5][:4]} % | Sold with levarage = {temp[6]}")
        total_price = str(total_price).split(".")[0]
        total_price_levarage = str(total_price_levarage).split(".")[0]
        repfinal.append(f"Total sold without levarage : {total_price} $")
        repfinal.append(f"Total sold with levarage : {total_price_levarage} $")
        return repfinal
