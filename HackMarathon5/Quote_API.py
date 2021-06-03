from quote import quote
import random

def random_quote(emotion):
    search=emotion
    result=quote(search, limit=50)
    short_quotes=[]
    for item in result:
        if len(item["quote"])<100:
            short_quotes.append(item)
    return short_quotes[random.randint(0,len(short_quotes)-1)]
print(random_quote("anger"))