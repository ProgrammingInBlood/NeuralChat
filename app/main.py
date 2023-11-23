from fastapi import FastAPI;
from typing import Union;

# import routes here
from app.routes import router as routes;



# create app instance
app = FastAPI(
    title="Chatbot API",
    description="Chatbot API for the chatbot app created by Eklavya Raj",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None
);

# include routes
app.include_router(routes);















