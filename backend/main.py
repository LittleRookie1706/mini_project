# default
import uvicorn

# custom
from all_env import environ
# from base.routers import app
from base.event_handle import app

### START ###
if __name__ == '__main__':

  if environ in ["deploy", "docker"]:
    host = '0.0.0.0'
  else:
    host = '127.0.0.1'

  uvicorn.run("main:app",host=host, port=8080, reload=True, workers=4)
  