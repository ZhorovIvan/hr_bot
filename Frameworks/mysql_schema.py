from peewee import *
from Frameworks.base_model import *


class UserData(BaseModel):
    id = PrimaryKeyField(null = False)
    chat_id = CharField(null = False)
    bio = CharField(null = False)
    emp_title = CharField(null = False)
    emp_number = CharField(null = False)
    emp_email = CharField(null = False)
    job_interest = CharField(null = False)