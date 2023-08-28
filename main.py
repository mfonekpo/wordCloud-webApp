from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from cloudMe import process_text, generate_wordcloud
from ocr import perform_ocr_on_image

app = FastAPI(debug = True)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/index", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.get("/ocr", response_class=HTMLResponse)
async def ocr(request: Request, image_file: UploadFile = File(...)):
    image_data = await image_file.read()
    extracted_text = perform_ocr_on_image(image_data)
    return templates.TemplateResponse("ocr.html", {"request": request, "results": extracted_text})


@app.get("/ner", response_class=HTMLResponse)
def ner(request: Request):
    return templates.TemplateResponse("ner.html", {"request": request})

@app.get("/summerization", response_class=HTMLResponse)
def summerization(request: Request):
    return templates.TemplateResponse("summerization.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.post("/GenerateWordCloud")
async def GenerateWordCloud(request: Request):
    form_data = await request.form()
    text_input = form_data["text_input"]

    processed_text = process_text(text_input)
    generate_wordcloud(text_input)
    return {"message": "word cloud generated successfully!"}