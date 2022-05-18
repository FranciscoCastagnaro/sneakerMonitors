from asyncore import read
import requests
from bs4 import BeautifulSoup
import randomheaders
from dhooks import Webhook, Embed

mainWH = "https://discord.com/api/webhooks/976611966833524797/7U93EdmUQyUAPig2HMgcb078Yy9zDEgq1u3ReI26jb_HRC3UDCWZ18wi-8y6Pm5MSCFj"
testWH = "https://discord.com/api/webhooks/975826935546515467/EcvnApPJslrFu5-nPYYsVYY2OgTAyZynxOtU7Gbs-JQ4_XtVjvkIsg5tkuPopbcuhOsv"

def monitorDiony():
    
    embed = Embed(
        description="**DIONYSOS**",
        color= 0xB61ABC,
        timestamp='now'
    )

    coreLinks = [f"https://www.digitalsport.com.ar/dionysos/prods/?sort=available_at%20desc&category[1]=1", f"https://www.digitalsport.com.ar/dionysos/prods/?category[1]=1&category[2]=25&sort=available_at%20desc", f"https://www.digitalsport.com.ar/dionysos/prods/?category[1]=1&category[2]=103&sort=available_at%20desc", f"https://www.digitalsport.com.ar/search/?search=dunk&sort=available_at%20desc", f"https://www.digitalsport.com.ar/search/?search=jordan&category[1]=1&sort=available_at%20desc"]
    discordWebhook = Webhook(testWH)

    for currentLink in coreLinks:

        source = requests.get(currentLink, headers=randomheaders.LoadHeader()).text
        mainSoup = BeautifulSoup(source, 'html.parser')

        for items in mainSoup.find_all('a', class_='product'):

            pairLink  = 'https://www.digitalsport.com.ar' + items.get('href')        
            filename  = 'dionyNewInLinks.txt'

            with open(filename, 'r') as rf:
                read = rf.read();
                with open(filename, 'a') as af:
                    if pairLink not in read:

                        pairTitle = items.get('data-title')
                        pairImg   = 'https://www.digitalsport.com.ar' + items.find('img', class_='img').get('data-src')
                        pairPrice = items.find('div', class_="precio").string

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

monitorDiony()