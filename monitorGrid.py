from asyncore import read
import requests
from bs4 import BeautifulSoup
import randomheaders
from dhooks import Webhook, Embed
import time

mainWH = "https://discord.com/api/webhooks/976611847056793600/sPcdalfPkw2t5mi4JE7WuYIh_RKXXt21cPpfdL-OlmkpCBuUT4JSEt91oeE6nFUbIFXh"
testWH = "https://discord.com/api/webhooks/975826935546515467/EcvnApPJslrFu5-nPYYsVYY2OgTAyZynxOtU7Gbs-JQ4_XtVjvkIsg5tkuPopbcuhOsv"

def monitorGrid():

    embed = Embed(
        description="**GRID**",
        color= 0xF4AC12,
        timestamp='now'
    )

    coreLinks = ["https://www.grid.com.ar/calzado/Hombre?PS=24&map=c,specificationFilter_23&O=OrderByReleaseDateDESC"]
    discordWebhook = Webhook(mainWH)
    
    for currentLink in coreLinks:

        source = requests.get(currentLink, headers=randomheaders.LoadHeader()).text
        mainSoup = BeautifulSoup(source, 'html.parser')

        for items in mainSoup.find_all('div', id='product'):

            pairLink  = items.a.get('href')        
            filename  = 'gridNewInLinks.txt'

            with open(filename, 'r') as rf:
                read = rf.read();
                with open(filename, 'a') as af:
                    if pairLink not in read:

                        pairTitle = items.a.get('title')
                        pairImg   = items.img.get('src')

                        pairPrice = items.find('span', class_="best-price").string.strip()

                        af.write('\n' + pairLink)

                        embed.set_title(title=pairTitle, url=pairLink)
                        embed.set_thumbnail(url=pairImg)
                        embed.add_field(name="Precio", value=pairPrice)
                        embed.add_field(name="-", value="everyone")


                        discordWebhook.send(embed=embed)
                        embed.del_field(0)
                        embed.del_field(0)

    
                    else:
                        print('No new links found')
while True:
    monitorGrid()
    time.sleep(60)