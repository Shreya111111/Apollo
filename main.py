from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# Define a model for the input data
class ScrapeInput(BaseModel):
    name: str
    organization_name: str

# Dictionary to store job status and results
jobs = {}

class JobStatus(BaseModel):
    status: str
    results: dict

@app.post("/scrape")
def scrape(scrape_input: 'ScrapeInput'):
    # Return the job_id
    return {"job_id": 'job_id'}

@app.get("/scrape_results")
def scrape_results(job_id: int):
    return JobStatus(status='status', results='results')

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
