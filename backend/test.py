import copy


def take_value(content:str, start_str: str, end_str: str):
    result = []
    start_pos = 0
    end_pos = -1
    if end_str == '':
        start_pos = content.find(start_str)
        if start_pos != -1: 
            print(start_pos)
            print(content[start_pos+len(start_str):])
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

content = '<p style=\"text-align: center;\"><img alt=\"Có một số loại thuốc không thể mua bán hợp pháp tại Nga.\" class=\"lazy\" data-src=\"https://i.ibb.co/Cv7WmzJ/image.jpg\" height=\"468\" src=\"https://i.ibb.co/Cv7WmzJ/image.jpg\" width=\"700\"/><br/>Có một số loại thuốc không thể mua bán hợp pháp tại Nga.</p>'
img_text = take_value(content, '<br/>', '')
print(img_text)

