from asyncore import read
import requests
from bs4 import BeautifulSoup
import randomheaders
from dhooks import Webhook, Embed


def monitorDiony():
    mainUrl = f"https://www.digitalsport.com.ar/dionysos/prods/?sort=available_at%20desc&category[1]=1"
    source = requests.get(mainUrl, headers=randomheaders.LoadHeader()).text
    mainSoup = BeautifulSoup(source, 'html.parser')
    discordWebhook = Webhook("https://discord.com/api/webhooks/975808860759666688/HAQ8iEEZkqMlytLZAhmLO5UODY92-EEjTA5NxUVmMTs6oQcwYsMsh9xCp9FmlDjsnz-J")
    embed = Embed(
        description="**DIONYSOS**",
        color= 0xB61ABC,
        timestamp='now'
    )

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