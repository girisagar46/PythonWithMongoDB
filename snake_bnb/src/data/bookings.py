import mongoengine


class Booking(mongoengine.EmbeddedDocument): # here EmbeddedDocument because Booking belongs to another document
    guest_owner_id = mongoengine.ObjectIdField() # this is a reference hece, the ObjectIdField
    guest_snake_id = mongoengine.ObjectIdField()

    booked_date = mongoengine.DateTimeField()
    check_in_date = mongoengine.DateTimeField(required=True)
    check_out_date = mongoengine.DateTimeField(required=True)

    review = mongoengine.StringField()
    rating = mongoengine.IntField(default=0)
