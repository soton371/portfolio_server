from mongoengine import Document, StringField
from pydantic import BaseModel


class Intro(Document):
    introOfName = StringField()
    name = StringField()
    whoAreYou = StringField()
    shortBio = StringField()


class IntroCrude(BaseModel):
    introOfName: str
    name: str
    whoAreYou: str
    shortBio: str
