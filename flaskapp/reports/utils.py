from flaskapp import db
from flaskapp.models import Report, Item

def item_from_db(it : Item)-> dict:

    dict_item: dict = {} # to be returned
    dict_item["id"] = it.item_id
    dict_item["counter"] = it.counter
    dict_item["environment"] = it.environment
    dict_item["framework"] = it.framework
    dict_item["title"] = it.title
    dict_item["level"] = it.level
    dict_item["ocurrences"] = it.ocurrences
    dict_item["project_id"] = it.project_id
    dict_item["unique_ocurrences"] = it.unique_ocurrences
    dict_item["last_occurrence_timestamp"] = it.timestamp 

    return { "item": dict_item }


def item_to_db(dict_item: dict, ri: int)-> Item:
    
    it: Item = Item(item_id=dict_item["id"], counter=dict_item["counter"],
                environment=dict_item["environment"], framework=dict_item["framework"],
                title=dict_item["title"], level=dict_item["level"],
                ocurrences=dict_item["ocurrences"],
                project_id=dict_item["project_id"],
                unique_ocurrences=dict_item["unique_ocurrences"],
                timestamp=dict_item["last_occurrence_timestamp"],
                report_id=ri)
    db.session.add(it)
    db.session.commit()
    return it


def report_from_db()-> dict:
    rep: Report = Report.query.first()
    
    dict_report: dict = {} # report to be returned
    dict_report["err"] = rep.error # puts the err field

    result_list: list[Item] = [] # it is a list of items
    for item in rep.items:
        result_list.append(item_from_db(item))

    dict_report["result"] = result_list # puts the list into the dictionary

    return dict_report


def report_to_db(r: dict)-> None:
    print(r)
    #try:
    rep: Report = Report(error=r["err"])
    db.session.add(rep)
    db.session.commit()

    for item in r["result"]:
        print(item)
        print("--------------------------------------------------------------------")
        it: Item = item_to_db(item["item"], rep.id)
                
    #except:
     #   print("ERRRRRRRRRRRRRRRRRRRRRROOOOOOOOOOOOOORRRRRRRRRRRRRRRRRRRRR")
        