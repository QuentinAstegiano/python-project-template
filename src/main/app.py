import service
from fastapi import FastAPI
from pydantic import BaseModel


class TemplateApp(FastAPI):
    """Template Application to show off a FastAPI implementation"""

    def __init__(self, haiku_service: service.HaikuService):
        super(TemplateApp, self).__init__(
            title="python-project-template", version="dev"
        )
        self.haiku_service = haiku_service


remote_source = service.MistralHaikuSource()
app = TemplateApp(service.HaikuService(remote_source))


class Haiku(BaseModel):
    """A Haiku poem"""

    """Lines of the poem"""
    poem: list[str]


@app.get("/")
def get_app_version():
    """Get reference data about the app"""
    return {"app-name": app.title, "version": app.version}


@app.get("/haiku")
def get_haiku():
    """Tell a new haiku"""
    return Haiku(poem=app.haiku_service.get())
