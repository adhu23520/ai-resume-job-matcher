from fastapi import FastAPI
from app.routes import resume

app = FastAPI() #This is the FastAPI application. This object controls the backend
app.include_router(resume.router)

@app.get("/") 
#This is a decorator. 
#It attaches special behavior to the function below
#.get() means this route accepts GET requests
# / is the route path
def root():
    return {"message": "AI Resume Matcher is running"} # The one inside braces is a dictionary

# The above block basically means when someone sends a GET request to '/', run the function below.


