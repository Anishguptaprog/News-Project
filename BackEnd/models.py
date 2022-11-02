# from xml.dom.minidom import Document, Identified


from mongoengine import Document, StringField, IntField


class TestDB(Document):
    name = StringField()
    age = IntField()
    college = StringField()
