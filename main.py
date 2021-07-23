from fastapi import FastAPI, Path
from typing import Optional
"""
~ Author = Faroxx
~ Git =
~ uvicorn main:app --reload
"""
app = FastAPI()

testruns = {
	1: {
		"name": "Run",
		"status": "passed"
	},
	2: {
		"name": "Valid",
		"status": "failed"
	}
}

@app.get("/runs")
def runs():
	return testruns

@app.get("/runs/{item_id}")
def get_run(item_id: int = Path(None, description="The ID of the test run", gt=0, lt=2)):
	return testruns[item_id]

@app.get("/run")
def get_run(name: Optional[str] = None):
	for id in testruns:
		if testruns[id]["name"] == name:
			return testruns[id]
	return {"Data": "Not found"}
