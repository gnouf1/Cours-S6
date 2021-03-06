from fastapi import FastAPI
from mySearchEngine import main as mse
from myBankImage import main as mbi


app = FastAPI()
app_mse = FastAPI()
app_mbi = FastAPI()
app_mie = FastAPI()

app_mse.include_router(mse.app)
app.mount("/mse", app_mse)

app_mbi.include_router(mbi.app)
app.mount("/mbi", app_mbi)
