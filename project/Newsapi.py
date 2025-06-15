import requests
#from apikey import key 
api_add="https://newsapi.org/v2/top-headlines?country=us&apiKey=870229f292984ef5bbcb917de1054304"
json_data=requests.get(api_add).json()

ar=[]

def news():
    for i in range(3):
        article=json_data["articles"][i]
        author=article.get("author","unkonwn Author")
        title=article.get("title","No tittle")
        description=article.get("description","description")
        if not author or not title or description=="removed":
            continue
        ar.append(f"Number {len(ar)+1}:\nAuthor: {author}\nTitle: {title}\nDescription: {description}\n")
    return ar
arr=news()
for item in arr:
    # speak(item)
    print(item)