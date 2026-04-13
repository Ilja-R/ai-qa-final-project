from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import pipeline, masking, scenarios, code_gen, review, bug_report

app = FastAPI(title="QA Pipeline System")

# Include new granular routers
app.include_router(masking.router)
app.include_router(scenarios.router)
app.include_router(code_gen.router)
app.include_router(review.router)
app.include_router(bug_report.router)

# Include original pipeline router
app.include_router(pipeline.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
