from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/index", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/ocr", response_class=HTMLResponse)
def ocr(request: Request):
    return templates.TemplateResponse("ocr.html", {"request": request})

@app.get("/ner", response_class=HTMLResponse)
def ner(request: Request):
    return templates.TemplateResponse("ner.html", {"request": request})

@app.get("/summerization", response_class=HTMLResponse)
def summerization(request: Request):
    return templates.TemplateResponse("summerization.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.post("/generate_wordcloud")
async def generate_wordcloud(request: Request):
    form_data = await request.form()
    text_input = form_data["text_input"]

    processed_text = processed_text(text_input)
    generate_wordcloud(processed_text)
    return {"message": "word cloud generated successfully!"}