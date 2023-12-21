from typing import Optional

from mongoengine import Document, StringField, ListField, ObjectIdField
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

# start for experience
class Experience(Document):
    _id = ObjectIdField()
    organization = StringField()
    role = StringField()
    joinDate = StringField()
    lastDate = StringField()
    notes = StringField()


class ExperienceCrude(BaseModel):
    organization: str
    role: str
    joinDate: str
    lastDate: str
    notes: str


# end for experience

# start for work
class Work(Document):
    _id = ObjectIdField()
    softwareName = StringField()
    summary = StringField()
    websiteUrl = StringField(default=None)
    appStore = StringField(default=None)
    playStore = StringField(default=None)
    imgUrl = StringField(default=None)


class WorkCrude(BaseModel):
    softwareName: str
    summary: str
    websiteUrl: Optional[str] = None
    appStore: Optional[str] = None
    playStore: Optional[str] = None
    imgUrl: Optional[str] = None
# end for work


# end for contact

class Contact(Document):
    explain = StringField()
    email = StringField()
    github = StringField(default=None)
    linkedIn = StringField(default=None)
    stackoverflow = StringField(default=None)
    facebook = StringField(default=None)
    instagram = StringField(default=None)


class ContactCrude(BaseModel):
    explain: str
    email: str
    github: Optional[str] = None
    linkedIn: Optional[str] = None
    stackoverflow: Optional[str] = None
    facebook: Optional[str] = None
    instagram: Optional[str] = None

# end for contact
