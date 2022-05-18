from asyncore import read
from cgi import test
import requests
from bs4 import BeautifulSoup
import randomheaders
from dhooks import Webhook, Embed

mainWH = "https://discord.com/api/webhooks/976612176213213194/2g5u5jtUu-TGM9UsKQFZk6yPGj3spdX1DUBMO4N5GspITM77liZ0f5MXafblvVNEBJOC"
testWH = "https://discord.com/api/webhooks/975826935546515467/EcvnApPJslrFu5-nPYYsVYY2OgTAyZynxOtU7Gbs-JQ4_XtVjvkIsg5tkuPopbcuhOsv"

def monitorMoov():

    embed = Embed(
        description="**MOOV**",
        color= 0x000000,
        timestamp='now'
    )

    coreLinks = ["https://www.moov.com.ar/hombre/calzado?srule=newest-products&start=0&sz=12", "https://www.moov.com.ar/marcas/nike?srule=newest-products&start=0&sz=12", "https://www.moov.com.ar/marcas/nike/nike?srule=newest-products&start=0&sz=12", "https://www.moov.com.ar/buscar?q=dunk&srule=newest-products&start=0&sz=12"]
    discordWebhook = Webhook(testWH)
    
    for currentLink in coreLinks:

        source = requests.get(currentLink, headers=randomheaders.LoadHeader()).text
        mainSoup = BeautifulSoup(source, 'html.parser')

        for items in mainSoup.find_all('div', class_='product'):

            pairLink  = 'https://www.moov.com.ar'+items.a.get('href')
            filename  = 'moovNewInLinks.txt'
            
            with open(filename, 'r') as rf:
                read = rf.read();
                with open(filename, 'a') as af:
                    if pairLink not in read:

                        pairTitle = items.find('a', class_="link").string
                        pairImg   = items.img.get('src')
                        pairPrice = items.find('span', class_="value").string.strip()

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

monitorMoov()