import copy, json
from models import News

many_news = News.select(News.id, News.content)

def type_check(content_type: str, content: str) -> str:
    if content_type == 'p' and content.find('<img') != -1:
        return 'img'
    elif content_type == '<div class="responsive"':
        return 'video'
    return content_type

def id_check(content: str):
    if content.find('id') != -1:
        content_id = take_value(content, 'id=\"', '">')
        content = take_value(content, '>', '')
    else:
        content_id = None

    return {
        'id': content_id,
        'content': content
    }

def special_mark(content) -> str:
    if type(content) == str:
        return  (content     
                    # special style    
                    .replace('<strong>','**').replace('</strong>','**')
                    .replace('<em>','*').replace('</em>','*')
                    # exclude
                    .replace('<span style="line-height:1.5em">','')
                )
    elif type(content) == list:
        result = []
        for con in content:
            result.append(special_mark(con))
        return result

def remove_errand(content: str):
    while content.startswith('<') or content.find('">') != -1:
        content = take_value(content, '>', '')
    return content

def take_value(content:str, start_str: str, end_str: str):
    result = []
    start_pos = 0
    end_pos = -1
    if end_str == '':
        start_pos = content.find(start_str, start_pos)
        if start_pos != -1: 
            result.append(content[start_pos+len(start_str):])
    else:
        while start_pos != -1:
            start_pos = content.find(start_str, start_pos)
            if start_pos != -1:
                end_pos = content.find(end_str, start_pos+len(start_str))
            if -1 in [start_pos, end_pos] or start_pos==end_pos: 
                break
            else:
                result.append(content[start_pos+len(start_str):end_pos])
                start_pos= copy.deepcopy(end_pos)

    if len(result) == 0:
        return None
    elif len(result) == 1:
        return result[0]
    return result


def content_check(data: dict) -> dict:
    content_type = data['content_type']
    content = data['content']

    if content_type == 'p':
        content = take_value(content, '>', '</p>')
        content = special_mark(content)

    elif content_type == 'h2':
        content = take_value(content, '>', '</h2>')
        content = id_check(content)

    elif content_type == 'ul':
        ul_list = take_value(content, '<li', '</li>')
        content = []
        for child_content in ul_list:
            href = take_value(child_content, 'href=\"', '"')
            tempo_content = take_value(child_content, '">', '</a>')
            if tempo_content:
                child_content = tempo_content
            child_content = special_mark(child_content)
            if type(href) == list:
                for i in range(len(href)):
                    child_content[i] = remove_errand(child_content[i])
                    content.append({
                        'href': href[i],
                        'content': child_content[i]
                    })
            else:
                child_content = remove_errand(child_content)
                content.append({
                    'href': href,
                    'content': child_content
                })

    elif content_type == 'table':
        table_list = take_value(content, '<p>', '</p>')
        for i in range(len(table_list)):
            table_list[i] = special_mark(table_list[i])
        content = table_list
    
    elif content_type == 'img':
        content = take_value(content, '>', '</p>')
        src = take_value(content, ' src="', '"')
        alt = take_value(content, 'alt="', '"')
        img_text = take_value(content, '<br/>', '')
        content = {
            'src': src,
            'alt': alt,
            'img_text': img_text
        }
        
    elif content_type == 'video':
        src = take_value(content, 'src=\"', '"')
        content = src

    data['content'] = content

    return data

def content_rewrite(content: str):
    if content.startswith('<div class="content-detail textview">'):
        content = content[37:-6]

    result = []

    startpoint = content.find(f'<div class="responsive"')
    while startpoint != -1:
        startpoint = content.find(f'<div class="responsive"', startpoint)
        endpoint = content.find(f'</div>', startpoint)
        endpoint = endpoint + 6
        data = {
            'start': startpoint,
            'end': endpoint,
            'content_type': 'video',
            'content': content[startpoint:endpoint]
        }
        if startpoint == -1:
            break
        startpoint = copy.deepcopy(endpoint)
        data = content_check(data)
        result.append(data)

    content_types = ['p', 'ul', 'table', 'h2']
    for content_type in content_types:
        startpoint = 0
        while startpoint != -1:
            startpoint = content.find(f'<{content_type}', startpoint)
            if startpoint != -1:
                endpoint = content.find(f'</{content_type}', startpoint)
                endpoint = endpoint + 3 + len(content_type)
                data = {
                    'start': startpoint,
                    'end': endpoint,
                    'content_type': content_type,
                    'content': content[startpoint:endpoint]
                }
                data['content_type'] = type_check(data['content_type'], data['content'])
                data = content_check(data)
                startpoint = copy.deepcopy(endpoint)
                result.append(data)


    newlist = sorted(result, key=lambda d: d['start'])
    for val in newlist:
        del val['start']
        del val['end']
    return newlist

#  start 
def clean_title(content: str, news_id):
        start_pos = content.find('</h1>')
        content = content[start_pos+5:]
        print(content)
        News.update(
            content = content
        ).where(News.id==news_id).execute()

def clean_content():
    many_data = {}
    for news in many_news:
        content = news.content
        many_data[str(news.id)] = content_rewrite(content)

    for key, value in many_data.items():
        News.update(
            content = value
        ).where(News.id==int(key)).execute()

