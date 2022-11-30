
from flaskapp import db

class Report(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    error = db.Column(db.Integer)

    items = db.relationship('Item', backref='origin', lazy=True)

    def __repr__(self):
        return f"Report('{self.id}','{self.error}')"


class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, nullable=True)    
    counter = db.Column(db.Integer, nullable=True)    
    environment = db.Column(db.String(20), nullable=False)
    framework = db.Column(db.String(20), nullable=True) # For example: "pyramid"
    title = db.Column(db.String, nullable=False) # The primary message text, as a string
    level = db.Column(db.String(10), nullable=True) # The severity level. One of: "critical", "error", "warning", "info", "debug"
    ocurrences = db.Column(db.Integer, nullable=True)    
    project_id = db.Column(db.Integer, nullable=True)
    unique_ocurrences = db.Column(db.Integer, nullable=True)
    timestamp = db.Column(db.DateTime, nullable=True) # When this occurred, as a unix timestamp
    
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'), nullable=False)
    
    def __repr__(self):
        return f"Item('{self.id}','{self.title}')"