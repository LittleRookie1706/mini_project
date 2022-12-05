from . import news_index

def add_news_meili(news_element):
    documents = [
        {
            "id": news_element["id"],
            "title" : news_element["title"],
            "description": news_element["description"],
            "thumbnail_img" : news_element["thumbnail_img"],
            "tags" : news_element["tags"],
    }
    ]
    news_index.add_documents(documents)