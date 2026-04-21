from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from reviewer import review_code

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/review", response_class=HTMLResponse)
async def review(request: Request, code: str = Form(...)):

    print("USER INPUT:", code)  # DEBUG

    result = review_code(code)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "review": result
    })
print("working")