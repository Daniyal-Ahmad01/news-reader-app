from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key="API_KEY")

def get_topic():
    return input("Enter topic: ")

def fetch_news(topic, lang="en", sort="relevancy"):
    return newsapi.get_everything(
    q=topic,
    language=lang,
    sort_by=sort
    )

def display_news(data):
    if not data["articles"]:
        print("No articles found.")
        return


    for index, article in enumerate(data["articles"], start=1):
        print(f"--- News Number {index} ---")
        print(f"Title: {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"Published date: {article['publishedAt']}")
        print(f"URL: {article['url']}")
        print("-" * 50)
        

topic = get_topic()
data = fetch_news(topic)
display_news(data)
