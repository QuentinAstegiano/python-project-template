import datetime

import service
from fastapi import FastAPI
from pydantic import BaseModel


class TemplateApp(FastAPI):
    """Template Application to show off a FastAPI implementation"""

    def __init__(self):
        super(TemplateApp, self).__init__(
            title="python-project-template", version="dev"
        )
        self.compute_service = service.ComputeService()


app = TemplateApp()


class ComputeResult(BaseModel):
    """Result of the compute function"""

    """Input of the function"""
    input: int
    """Output of the function"""
    output: int
    """Date when the function was called"""
    call_date: datetime.datetime


@app.get("/")
def get_app_version():
    """Get reference data about the app"""
    return {"app-name": app.title, "version": app.version}


@app.get("/compute")
def compute_data(input: int):
    """Compute a result for a given input to solve a critical business problem"""
    compute_result = app.compute_service.do_compute(input)
    return ComputeResult(
        input=input, output=compute_result, call_date=datetime.datetime.now()
    )
