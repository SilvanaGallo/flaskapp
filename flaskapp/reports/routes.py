from flask import Blueprint
from flaskapp import repository
from flaskapp.models import Report
from flaskapp.reports.utils import report_from_db, report_to_db

reports = Blueprint('reports', __name__)

@reports.route("/reports",  methods=['GET'])
def top_active_items():
    rep = Report.query.first()
    if rep is None:
        result = repository.top_active_items()
        report_to_db(result)
    return report_from_db()
    

@reports.route("/reports",  methods=['DELETE'])
def delete_reports():
    rep = Report.query.first()
    if rep:
        try:
            for i in Item.query.all():
                db.session.delete(i)
            db.session.delete(rep)
            db.session.commit()
            result = {"data": {"err": 0, "message": "Report has been cleared."}}
        except:
            result = {"data": {"err": 1, "message": "Problems during report cleanup."}}
    else:
        result = {"data": {"err": 0, "message": "Database is empty."}}
    return result