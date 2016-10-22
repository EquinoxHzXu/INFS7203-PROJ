from mongoengine import *

connect("twitter")

class ListMembersHS(Document):
    screen_name = StringField(primary_key=True)
    id_str = StringField(required=True)
    friends_count = IntField(required=True)
