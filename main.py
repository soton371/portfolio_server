import json

from bson import ObjectId
from fastapi import FastAPI
from mongoengine import connect

from models import Intro, IntroCrude, About, AboutCrude, Experience, ExperienceCrude

app = FastAPI()
connect(db='soton_portfolio', host='localhost', port=27017)


@app.get('/')
async def read_root():
    return {'Hello': 'World'}


# start for intro
@app.post('/add_intro')
async def add_intro(new_intro: IntroCrude):
    try:
        intro = Intro(
            introOfName=new_intro.introOfName,
            name=new_intro.name,
            whoAreYou=new_intro.whoAreYou,
            shortBio=new_intro.shortBio
        )
        intro.save()
        return {
            'status': True,
            'message': 'Intro add successfully'}
    except Exception as e:
        print(f'Failed to add intro: {e}')
        return {
            'status': False,
            'message': 'Failed to add intro'}


@app.get('/get_intro')
async def get_intro():
    try:
        intro_json = json.loads(Intro.objects.first().to_json())
        return {
            "status": True,
            "message": "Fetch intro successfully",
            "data": intro_json}
    except Exception as e:
        print(f"Failed to fetch into e: {e}")
        return {
            "status": False,
            "message": "Failed to fetch intro",
            "data": None}


@app.patch("/update_intro")
async def update_intro(intro_data: IntroCrude):
    try:
        intro = Intro.objects.first()
        intro.update(
            introOfName=intro_data.introOfName,
            name=intro_data.name,
            whoAreYou=intro_data.whoAreYou,
            shortBio=intro_data.shortBio,
        )
        intro.save()
        return {
            "status": True,
            "message": "Intro updated successfully",
        }
    except Exception as e:
        print(f"Failed to update intro: {e}")
        return {
            "status": False,
            "message": "Failed to update intro",
        }


# end for intro


# start for about
@app.post('/add_about')
async def add_about(new_about: AboutCrude):
    try:
        about = About(
            explain=new_about.explain,
            technologies=new_about.technologies
        )
        about.save()
        return {
            'status': True,
            'message': 'About add successfully'}
    except Exception as e:
        print(f'Failed to add about: {e}')
        return {
            'status': False,
            'message': 'Failed to add about'}


@app.get('/get_about')
async def get_about():
    try:
        about_json = json.loads(About.objects.first().to_json())
        return {
            "status": True,
            "message": "Fetch about successfully",
            "data": about_json}
    except Exception as e:
        print(f"Failed to fetch about e: {e}")
        return {
            "status": False,
            "message": "Failed to fetch about",
            "data": None}


@app.patch("/update_about")
async def update_about(about_data: AboutCrude):
    try:
        about = About.objects.first()
        about.update(
            explain=about_data.explain,
            technologies=about_data.technologies
        )
        about.save()
        return {
            "status": True,
            "message": "About updated successfully",
        }
    except Exception as e:
        print(f"Failed to update about: {e}")
        return {
            "status": False,
            "message": "Failed to update about",
        }


# end for about

# start for experience
@app.post('/add_experince')
async def add_experience(new_experience: ExperienceCrude):
    try:
        experience = Experience(
            organization=new_experience.organization,
            role=new_experience.role,
            joinDate=new_experience.joinDate,
            lastDate=new_experience.lastDate,
            notes=new_experience.notes
        )
        experience.save()
        return {
            'status': True,
            'message': 'Experience add successfully'}
    except Exception as e:
        print(f'Failed to add experience: {e}')
        return {
            'status': False,
            'message': 'Failed to add experience'}


@app.get('/get_experiences')
async def get_experiences():
    try:
        experiences_json = json.loads(Experience.objects().to_json())
        return {
            "status": True,
            "message": "Fetch experiences successfully",
            "data": experiences_json}
    except Exception as e:
        print(f"Failed to fetch experiences e: {e}")
        return {
            "status": False,
            "message": "Failed to fetch experiences",
            "data": None}


@app.put('/update_experience/{_id}')
async def update_experience(_id: str, updated_experience: ExperienceCrude):
    try:
        _id = ObjectId(_id)

        updated_fields = {
            key: value for key, value in updated_experience.model_dump().items() if value is not None
        }
        Experience.objects(_id=_id).update_one(**updated_fields)
        return {
            'status': True,
            'message': 'Experience updated successfully'
        }

    except Exception as e:
        print(f'Failed to update experience: {e}')
        return {
            'status': False,
            'message': 'Failed to update experience'
        }
# end for experience
