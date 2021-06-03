from quote import quote
import random

def random_quote(emotion):
    search=emotion
    result=quote(search, limit=50)
    short_quotes=[]
    for item in result:
        if len(item["quote"])<150:
            short_quotes.append(item)
    if len(short_quotes)==0:
        print("No quote found, sry")
    else print("\n",short_quotes[random.randint(0,len(short_quotes)-1)]['quote'], "  (by ",short_quotes[random.randint(0,len(short_quotes)-1)]["author"],")\n")