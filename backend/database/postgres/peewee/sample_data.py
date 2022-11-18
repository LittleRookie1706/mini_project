import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents[3] 
sys.path.append(str(package_root_directory)) 
print(package_root_directory)

def create_sample_tags():
    from apps.news.models import Tags

    list_tags=[
        ("Khoa học",), ("Lịch sử",), ("Địa lí",), ("Sinh học",),
        ("10 vạn cau hỏi vì sao",), ("Sự thật thú vị",), ("1001 bí ẩn",), ("Danh nhân thế  giới",), ("thế giới động vật",),
        ("Y học-sức khỏe",), ("Kiến trúc độc đáo",)
    ]
    Tags.insert_many(list_tags, fields=[Tags.name]).execute()

def create_sample_tag_groups():
    pass

def create_sample_users():
    from apps.authentication.models import Users

    list_users=[
        ("bettermie2303@gmail.com", "A Tăng kỳ kiếp", "https://cdn.discordapp.com/avatars/880359404036317215/8eb19838fc3152a7d799870849e4b542.png", True, "880359404036317215")
    ]
    Users.insert_many(list_users, fields=[Users.email, Users.username, Users.avatar, Users.is_admin, Users.discord_id]).execute()


def create_sample_comments():
    pass

def create_sample_news():
    pass

sample_data=[
    ("tags", create_sample_tags()),
    ("taggroup", create_sample_tag_groups()),
    ("users", create_sample_users()),
    ("comments", create_sample_comments()),
    ("news", create_sample_news()),
]

def create_sample_data(data_tables: list):
    for data in sample_data:
        if data[0] in data_tables:
            data[1]


create_sample_data([
    # "tags",
    # "taggroup",
    # "users",
    # "comments",
    "news",
])

