# fastapi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#local
from all_env import docs_url

### base setting ###
app = FastAPI(docs_url=f"/{docs_url}", redoc_url=None)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### temaple response ###
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates

# templates = Jinja2Templates(directory="templates")
# TemplateResponse = templates.TemplateResponse
# app.mount("/static", StaticFiles(directory="./static"), name="static")


    
