from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import pipeline, masking, scenarios, code_gen, review, bug_report

app = FastAPI(title="AI-Powered QA Automation Pipeline")

# Include routers from api package
app.include_router(masking.router)
app.include_router(scenarios.router)
app.include_router(code_gen.router)
app.include_router(review.router)
app.include_router(bug_report.router)
app.include_router(pipeline.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "AI QA Pipeline API is running"}
