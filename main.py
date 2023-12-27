import json

from bson import ObjectId
from fastapi import FastAPI
from mongoengine import connect

from models import Intro, IntroCrude, About, AboutCrude, Experience, ExperienceCrude, Work, WorkCrude, Contact, \
    ContactCrude, Footer, FooterCrude

app = FastAPI()
connect(db='soton_portfolio', host='localhost', port=27017)


@app.get('/')
async def read_root():
    return {'Hello': 'World'}


# start for intro
@app.post('/add_intro')
async def add_intro(new_intro: IntroCrude):
    try:
        intro = Intro(**new_intro.model_dump())
        intro.save()
        return {
            'isSuccess': True,
            'message': 'Intro add successfully'}
    except Exception as e:
        print(f'Failed to add intro: {e}')
        return {
            'isSuccess': False,
            'message': 'Failed to add intro'}


@app.get('/get_intro')
async def get_intro():
    try:
        intro_json = json.loads(Intro.objects.first().to_json())
        return {
            "isSuccess": True,
            "message": "Fetch intro successfully",
            "data": intro_json}
    except Exception as e:
        print(f"Failed to fetch into e: {e}")
        return {
            "isSuccess": False,
            "message": "Failed to fetch intro",
            "data": None}


@app.patch("/update_intro")
async def update_intro(intro_data: IntroCrude):
    try:
        intro = Intro.objects.first()
        intro.update(**intro_data.model_dump())
        intro.save()
        return {
            "isSuccess": True,
            "message": "Intro updated successfully",
        }
    except Exception as e:
        print(f"Failed to update intro: {e}")
        return {
            "isSuccess": False,
            "message": "Failed to update intro",
        }


@app.delete("/delete_intro")
async def delete_intro():
    try:
        Intro.objects.all().delete()
        return {
            "isSuccess": True,
            "message": "Intro delete successfully",
        }
    except Exception as e:
        print(f"Failed to delete intro: {e}")
        return {
            "isSuccess": False,
            "message": "Failed to delete intro",
        }


# end for intro


# start for about
@app.post('/add_about')
async def add_about(new_about: AboutCrude):
    try:
        about = About(**new_about.model_dump())
        about.save()
        return {
            'isSuccess': True,
            'message': 'About add successfully'}
    except Exception as e:
        print(f'Failed to add about: {e}')
        return {
            'isSuccess': False,
            'message': 'Failed to add about'}


@app.get('/get_about')
async def get_about():
    try:
        about_json = json.loads(About.objects.first().to_json())
        return {
            "isSuccess": True,
            "message": "Fetch about successfully",
            "data": about_json}
    except Exception as e:
        print(f"Failed to fetch about e: {e}")
        return {
            "isSuccess": False,
            "message": "Failed to fetch about",
            "data": None}


@app.patch("/update_about")
async def update_about(about_data: AboutCrude):
    try:
        about = About.objects.first()
        about.update(**about_data.model_dump())
        about.save()
        return {
            "isSuccess": True,
            "message": "About updated successfully",
        }
    except Exception as e:
        print(f"Failed to update about: {e}")
        return {
            "isSuccess": False,
            "message": "Failed to update about",
        }


@app.delete("/delete_about")
async def delete_about():
    try:
        About.objects.all().delete()
        return {
            "isSuccess": True,
            "message": "About delete successfully",
        }
    except Exception as e:
        print(f"Failed to delete about: {e}")
        return {
            "isSuccess": False,
            "message": "Failed to delete about",
        }


# end for about

# start for experience
@app.post('/add_experience')
async def add_experience(new_experience: ExperienceCrude):
    try:
        experience = Experience(**new_experience.model_dump())
        experience.save()
        return {
            'isSuccess': True,
            'message': 'Experience add successfully'}
    except Exception as e:
        print(f'Failed to add experience: {e}')
        return {
            'isSuccess': False,
            'message': 'Failed to add experience'}


@app.get('/get_experiences')
async def get_experiences():
    try:
        experiences_json = json.loads(Experience.objects().to_json())
        return {
            "isSuccess": True,
            "message": "Fetch experiences successfully",
            "data": experiences_json}
    except Exception as e:
        print(f"Failed to fetch experiences e: {e}")
        return {
            "isSuccess": False,
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
            'isSuccess': True,
            'message': 'Experience updated successfully'
        }

    except Exception as e:
        print(f'Failed to update experience: {e}')
        return {
            'isSuccess': False,
            'message': 'Failed to update experience'
        }


# end for experience


# start work

@app.post('/add_work')
async def add_work(new_work: WorkCrude):
    try:
        work = Work(**new_work.model_dump())
        work.save()
        return {
            'isSuccess': True,
            'message': 'Work add successfully'}
    except Exception as e:
        print(f'Failed to add Work: {e}')
        return {
            'isSuccess': False,
            'message': 'Failed to add Work'}


@app.get('/get_work')
async def get_work():
    try:
        work_json = json.loads(Work.objects().to_json())
        return {
            "isSuccess": True,
            "message": "Fetch work successfully",
            "data": work_json}
    except Exception as e:
        print(f"Failed to fetch work e: {e}")
        return {
            "isSuccess": False,
            "message": "Failed to fetch work",
            "data": None}


@app.put('/update_work/{_id}')
async def update_work(_id: str, updated_work: WorkCrude):
    try:
        _id = ObjectId(_id)

        updated_fields = {
            key: value for key, value in updated_work.model_dump().items() if value is not None
        }
        Work.objects(_id=_id).update_one(**updated_fields)
        return {
            'isSuccess': True,
            'message': 'Work updated successfully'
        }

    except Exception as e:
        print(f'Failed to update work: {e}')
        return {
            'isSuccess': False,
            'message': 'Failed to update work'
        }


# end work


# start contact

@app.post('/add_contact')
async def add_contact(new_contact: ContactCrude):
    try:
        contact = Contact(**new_contact.model_dump())
        contact.save()
        return {
            'isSuccess': True,
            'message': 'Contact add successfully'}
    except Exception as e:
        print(f'Failed to add contact: {e}')
        return {
            'isSuccess': False,
            'message': 'Failed to add contact'}


@app.get('/get_contact')
async def get_contact():
    try:
        contact_json = json.loads(Contact.objects.first().to_json())
        return {
            "isSuccess": True,
            "message": "Fetch contact successfully",
            "data": contact_json}
    except Exception as e:
        print(f"Failed to fetch contact e: {e}")
        return {
            "isSuccess": False,
            "message": "Failed to fetch contact",
            "data": None}


@app.patch("/update_contact")
async def update_contact(about_contact: ContactCrude):
    try:
        contact = Contact.objects.first()
        contact.update(**about_contact.model_dump())
        contact.save()
        return {
            "isSuccess": True,
            "message": "Contact updated successfully",
        }
    except Exception as e:
        print(f"Failed to update contact: {e}")
        return {
            "isSuccess": False,
            "message": "Failed to update contact",
        }


@app.delete("/delete_contact")
async def delete_contact():
    try:
        Contact.objects.all().delete()
        return {
            "isSuccess": True,
            "message": "Contact delete successfully",
        }
    except Exception as e:
        print(f"Failed to delete contact: {e}")
        return {
            "isSuccess": False,
            "message": "Failed to delete contact",
        }


# end contact

# start footer

@app.post('/add_footer')
async def add_footer(new_footer: FooterCrude):
    try:
        footer = Footer(**new_footer.model_dump())
        footer.save()
        return {
            'isSuccess': True,
            'message': 'Footer add successfully'}
    except Exception as e:
        print(f'Failed to add footer: {e}')
        return {
            'isSuccess': False,
            'message': 'Failed to add footer'}


@app.get('/get_footer')
async def get_footer():
    try:
        footer_json = json.loads(Footer.objects.first().to_json())
        return {
            "isSuccess": True,
            "message": "Fetch footer successfully",
            "data": footer_json}
    except Exception as e:
        print(f"Failed to fetch footer e: {e}")
        return {
            "isSuccess": False,
            "message": "Failed to fetch footer",
            "data": None}


@app.patch("/update_footer")
async def update_footer(new_footer: FooterCrude):
    try:
        footer = Footer.objects.first()
        footer.update(**new_footer.model_dump())
        footer.save()
        return {
            "isSuccess": True,
            "message": "Footer updated successfully",
        }
    except Exception as e:
        print(f"Failed to update footer: {e}")
        return {
            "isSuccess": False,
            "message": "Failed to update footer",
        }


@app.delete("/delete_footer")
async def delete_footer():
    try:
        Footer.objects.all().delete()
        return {
            "isSuccess": True,
            "message": "Footer delete successfully",
        }
    except Exception as e:
        print(f"Failed to delete footer: {e}")
        return {
            "isSuccess": False,
            "message": "Failed to delete footer",
        }
# end footer
