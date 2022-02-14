import time
import sqlite3
from discord_webhook import DiscordWebhook, DiscordEmbed

while True:
    try:
        con = sqlite3.connect('/home/web/spacecypto/app/app/dashboardV1.db')
        cur = con.cursor()
        cur.execute(f'''SELECT * from Cryptos where webhook != ""''')
        data = cur.fetchall()
        con.close()
        web = []
        for k in data:
            temp = ""
            for x in range(len(k)):
                if k[x] != "" :
                    temp += k[x] + "|"
            web.append(temp)
        for k in web:
            info = k.split("|")[1:-1]
            info2 = []
            count = 0
            temp2 = ""
            for x in info[:-1]:
                temp2 += x + " "
                count += 1
                if count >= 4:
                    info2.append(temp2)
                    temp2 = ""
                    count = 0
            try:
                webhook_PersonInfo = DiscordWebhook(url=f'{info[-1:][0]}', content=None)
                embed = DiscordEmbed(title="Crypto Wallet", description=None, color=000000)
                embed.set_author(name='HyouKa#0007', url='https://github.com/hyoukash', icon_url = "https://cdn.discordapp.com/avatars/777220625747148830/4d5628dc59b9c93b4f15ca45d5c5f56e.png?size=4096")
                embed.set_thumbnail(url='https://bitcoin.org/img/icons/opengraph.png?1641218872')
                for x in range(0, len(info2)):
                    embed.add_embed_field(name = "Name Amount Levarage Purchased", value=f"{info2[x]}", inline=False)
                webhook_PersonInfo.add_embed(embed)
                response = webhook_PersonInfo.execute()
            except :
                pass
    except :
        pass
    time.sleep(300)
