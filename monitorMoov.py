from asyncore import read
import requests
from bs4 import BeautifulSoup
import randomheaders
from dhooks import Webhook, Embed


def monitorMoov():
    mainUrl = "https://www.moov.com.ar/hombre/calzado?srule=newest-products&start=0&sz=12"
    source = requests.get(mainUrl, headers=randomheaders.LoadHeader()).text
    mainSoup = BeautifulSoup(source, 'html.parser')
    discordWebhook = Webhook("https://discord.com/api/webhooks/975826935546515467/EcvnApPJslrFu5-nPYYsVYY2OgTAyZynxOtU7Gbs-JQ4_XtVjvkIsg5tkuPopbcuhOsv")
    embed = Embed(
        description="**MOOV**",
        color= 0x000000,
        timestamp='now'
    )

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