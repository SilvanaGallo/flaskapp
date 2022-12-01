from flask import Blueprint
from flaskapp import repository, db
from flaskapp.models import Report


reports = Blueprint('reports', __name__)

@reports.route("/reports",  methods=['GET'])
def top_active_items():
    rep = Report.query.first()
    if rep is None:
        result = repository.top_active_items()
        rep = Report(content=result)
        try:
            db.session.add(rep)
            db.session.commit()
            return rep.content
        except:
            result = {"data": {"err": 1, "message": "Problems during report storing."}}
            return result    
    else:
        return rep.content
    

@reports.route("/reports",  methods=['DELETE'])
def delete_reports():
    rep = Report.query.first()
    if rep:
        try:
            db.session.delete(rep)
            db.session.commit()
            result = {"data": {"err": 0, "message": "Report has been cleared."}}
        except:
            result = {"data": {"err": 1, "message": "Problems during report cleanup."}}
    else:
        result = {"data": {"err": 0, "message": "Database is empty."}}
    return result