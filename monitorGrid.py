from asyncore import read
import requests
from bs4 import BeautifulSoup
import randomheaders
from dhooks import Webhook, Embed


def monitorGrid():
    mainUrl = "https://www.grid.com.ar/calzado/Hombre?PS=24&map=c,specificationFilter_23&O=OrderByReleaseDateDESC"
    source = requests.get(mainUrl, headers=randomheaders.LoadHeader()).text
    mainSoup = BeautifulSoup(source, 'html.parser')
    discordWebhook = Webhook("https://discord.com/api/webhooks/975808860759666688/HAQ8iEEZkqMlytLZAhmLO5UODY92-EEjTA5NxUVmMTs6oQcwYsMsh9xCp9FmlDjsnz-J")
    embed = Embed(
        description="**GRID**",
        color= 0xF4AC12,
        timestamp='now'
    )

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

monitorGrid()