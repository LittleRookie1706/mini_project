#
import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents[2] 
sys.path.append(str(package_root_directory)) 
print(package_root_directory)

#
from database.mongodb.base import dtbs

db1=dtbs['news_data']

data = db1.find({})

result = []
for dat in data:
    del dat["_id"]
    result.append(dat)

#
import json
with open('news_sample_data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)