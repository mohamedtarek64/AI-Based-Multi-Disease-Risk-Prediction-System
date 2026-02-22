from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import diabetes, heart, hypertension, kidney, cancer, digestive, respiratory

app = FastAPI(
    title="AI Multi-Disease Prediction API",
    description="Mega-Scale Machine Learning service for real-time risk assessment (Graduation Project Edition).",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(diabetes.router)
app.include_router(heart.router)
app.include_router(hypertension.router)
app.include_router(kidney.router)
app.include_router(cancer.router)
app.include_router(digestive.router)
app.include_router(respiratory.router)

@app.get("/")
async def root():
    return {"message": "Mega AI Service Online", "diseases": ["diabetes", "heart", "hypertension", "kidney", "cancer", "digestive", "respiratory"]}

@app.get("/health")
async def health():
    return {"status": "healthy"}
