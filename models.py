from mongoengine import Document, StringField, ListField
from pydantic import BaseModel


# start for intro
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


# end for intro

# start for about
class About(Document):
    explain = StringField()
    technologies = ListField()


class AboutCrude(BaseModel):
    explain: str
    technologies: list
# end for about
