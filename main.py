from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from services import get_bearer_token, get_usage_data

app = FastAPI(title="DPDC Usage API")

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/api/usage")
def usage_api(customer_number: str = Form(...)):
    try:
        token = get_bearer_token()
        data = get_usage_data(customer_number, token)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
