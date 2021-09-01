import mongoengine as me


class Book(me.Document):
    author = me.StringField(required=True)
    title = me.StringField(required=True)


