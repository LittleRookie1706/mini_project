import sys  
from pathlib import Path  
file = Path(__file__). resolve()  
package_root_directory = file.parents[3] 
sys.path.append(str(package_root_directory))  

from  apps.authentication.models import Users

user=Users.get_or_none(email=sys.argv[1])
if user:
    Users.update(is_admin=True).where(Users.email==sys.argv[1]).execute()
    print(f"Added {sys.argv[1]} to superuser")
else:
    print("User not found")

