from models import News

many_news = News.select(News.id, News.content)

def clean_title():
    for news in many_news:
        content = news.content
        start_pos = content.find('</h1>')
        content = content[start_pos+5:]
        print(content)
        News.update(
            content = content
        ).where(News.id==news.id).execute()
