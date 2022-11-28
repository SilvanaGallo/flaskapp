from flask import Blueprint
from flaskapp import repository
from flaskapp.models import Report
from flaskblog.reports.utils import json_from_db, json_to_db

reports = Blueprint('reports', __name__)

def json_from_db():
    rep = Report.query.first()
    
    dict_report = {} # report to be returned
    dict_report["err"] = rep.error # puts the err field

    dict_result = [] # it is a list of items
    {k:v for k,v in params.items() if v is not ''}


@reports.route("/reports",  methods=['GET'])
def top_active_items():
    if Report.query.first():
        return json_from_db()
        #return Report.json_from_db()
    else:
        result = repository.top_active_items()
        #Report.json_to_db(result)

        #########################
    return result
    

@reports.route("/reports",  methods=['DELETE'])
def delete_reports():
    try:
        rep = Report.query.first()
        db.session.delete(rep)
        db.session.commit()
        result = {"data": {"err": 0, "message": "Report has been cleared."}}
    except:
        result = {"data": {"err": 1, "message": "Problems with report cleanup."}}
        
    return json.dumps(result, indent=2)