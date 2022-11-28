
from flaskapp import db

class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(20), nullable=False)
    route = db.Column(db.String, nullable=True) # For example: "home#index"
    message_body = db.Column(db.String, nullable=False) # The primary message text, as a string
    level = db.Column(db.String(10), nullable=True) # The severity level. One of: "critical", "error", "warning", "info", "debug"

    context = db.Column(db.String(100), nullable=False) # For example, in a Rails app, this could be `controller#action`
    timestamp = db.Column(db.DateTime, nullable=True) # When this occurred, as a unix timestamp
    status = db.Column(db.String(10), nullable=True) # resolved, active, muted
    resolved_in_version = db.Column(db.String, nullable=True)
    title = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, nullable=True)

    uuid = db.Column(db.String(36), nullable=True)
    
    
    def __repr__(self):
        return f"Item('{self.uuid}','{self.message_body}')"

   
class Report():
    ...