import json
from fastapi import FastAPI
from models import Intro, IntroCrude
from mongoengine import connect

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
            'status': True,
            'message': 'Intro add successfully'}


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
