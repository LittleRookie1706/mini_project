import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents[3] 
sys.path.append(str(package_root_directory)) 

import json
import datetime
from apps.news.models import Tags, News, TagGroups
from apps.authentication.models import Users

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


sample_data={
    "taggroup": create_sample_tag_groups(),
    "tags": create_sample_tags(),
    "users": create_sample_users(),
    # "comments": create_sample_comments(),
    "news": create_sample_news(),
}


# def create_sample_data(data_tables: list):
#     for data in data_tables:
#         sample_data[data]

# create_sample_data([
#     # "tags",
#     # "taggroup",
#     # "users",
#     # "comments",
#     "news",
# ])

