from fastapi import FastAPI
from app.routes import resume, match
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() #This is the FastAPI application. This object controls the backend

# Add this block — allows your Next.js frontend to talk to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume.router)
app.include_router(match.router)

@app.get("/") 
#This is a decorator. 
#It attaches special behavior to the function below
#.get() means this route accepts GET requests
# / is the route path
def root():
    return {"message": "AI Resume Matcher is running"} # The one inside braces is a dictionary

# The above block basically means when someone sends a GET request to '/', run the function below.


