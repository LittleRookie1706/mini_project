import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents[1] 
sys.path.append(str(package_root_directory)) 
# 

import json
import datetime
from base.test_conf.models import Tags, News, TagGroups, Users

def create_sample_tag_groups():
    with open('database/postgres/peewee/sample_data/taggroups.json', encoding='utf-8') as f:
        data = json.loads(f.read())
    TagGroups.insert_many(data, fields=[TagGroups.name]).execute()

def create_sample_tags():
    with open('database/postgres/peewee/sample_data/tags.json', encoding='utf-8') as f:
        data = json.loads(f.read())
    Tags.insert_many(data).execute()

def create_sample_users():
    with open('database/postgres/peewee/sample_data/users.json', encoding='utf-8') as f:
        data = json.loads(f.read())
    Users.insert_many(data, fields=[Users.email, Users.username, Users.avatar, Users.is_admin, Users.discord_id]).execute()


def create_sample_comments():
    pass

def create_sample_news():
    from base.test_conf.clean_data import clean_title, clean_content

    with open('database/postgres/peewee/sample_data/news.json', encoding='utf-8') as f:
        data = json.loads(f.read())

    tags={}
    for dat in data:
        tags[dat["title"]] = dat["tags"]
        del dat["tags"]
        date = dat["created_at"].split("/")
        dat["created_at"] = datetime.datetime.strptime(f"{date[0]}/{date[1]}/{date[2][2::]}", '%d/%m/%y')

    News.insert_many(data).execute()

    for key, value in tags.items():
        news = News.get(title=key)
        news.tags.add([ Tags.get(Tags.id == x) for x in value ])
    
    clean_title()
    # clean_content()

def create_sample_search():
    from database.meilisearch.sync.news import add_news_meili
    
    news_list = list(News.select().dicts())
    for news in news_list:
        add_news_meili({
                "id": news["id"],
                "title" : news["title"],
                "description": news["description"],
                "thumbnail_img" : news["thumbnail_img"],
                "tags" : [key["id"] for key in News.get_tags(news["id"])],
            })

sample_data={
    "taggroup": create_sample_tag_groups,
    "tags": create_sample_tags,
    "users": create_sample_users,
    "comments": create_sample_comments,
    "news": create_sample_news,
    "search": create_sample_search,
}

def create_sample_data(data_tables: list):
    for data in data_tables:
        if data in sample_data.keys():
            sample_data[data]()

create_sample_data([
    "taggroup",
    "tags",
    "users",
    "news",
    "comments",
    "search"
])

