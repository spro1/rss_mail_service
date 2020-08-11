import requests
import datetime
import xml.etree.ElementTree as elemTree
import sys
sys.path.append("..")

from database.db import mongo_connect

client = mongo_connect()
collection = client.rss_mail_service.site
pcollection = client.rss_mail_service.post

def get_xml(url, author, pcollection):
    print(url, author)
    xdate = datetime.datetime(2020, 1, 1, 1, 1, 1)
    html = requests.get(url)
    try:
        tree = elemTree.fromstring(html.text)
        for child in tree.iter("item"):
            try:
                data = {}
                title = child.find("title").text
                link = child.find("link").text
                date = child.find("pubDate").text
                date_sp = " ".join(date.split(" ")[:-1])
                try:
                    date_obj = datetime.datetime.strptime(date_sp, "%a, %d %b %Y %H:%M:%S")
                except:
                    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
                if date_obj > xdate:
                    print(date)
                    data["author"] = author
                    data["title"] = title
                    data["link"] = link
                    data["date"] = date_obj
                    data["update"] = datetime.datetime.now()
                    pcollection.update(data, data, upsert=True)
            except Exception as e:
                print(e)
                pass
    except Exception as e:
        print(e, "not xml")


for i in collection.find():
    get_xml(i["src"], i["author"], pcollection)
client.close()
