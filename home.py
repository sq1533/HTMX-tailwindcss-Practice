import os
import datetime
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__),"templates"))

#homePage
@app.get("/",response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("samples.html",{"request":request})

@app.get("/now")
def nowTime():
    nowTime = datetime.datetime.now()
    result = f"<P>{nowTime}</p>"
    return HTMLResponse(content=result)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8501)