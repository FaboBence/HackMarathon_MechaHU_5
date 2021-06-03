from quote import quote
import random

def random_quote(emotion):
    search=emotion
    result=quote(search, limit=50)
    return result[random.randint(0,len(result)-1)]