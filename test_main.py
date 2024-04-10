import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_scrape_endpoint():
    # Test POST /scrape endpoint
    response = client.post("/scrape", json={"name": "John", "organization_name": "ABC Inc."})
    assert response.status_code == 200
    assert "job_id" in response.json()

def test_scrape_results_endpoint():
    # Test GET /scrape_results endpoint
    job_id = "dummy_job_id"
    response = client.get(f"/scrape_results?job_id={job_id}")
    assert response.status_code == 200
    assert response.json()["status"] == "status"
    assert response.json()["results"] == "results"

if __name__ == "__main__":
    pytest.main()
