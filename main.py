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
    intro = Intro(
        introOfName=new_intro.introOfName,
        name=new_intro.name,
        whoAreYou=new_intro.whoAreYou,
        shortBio=new_intro.shortBio
    )
    intro.save()
    return {'message': 'Intro add successfully'}
# end for intro
