import pytest
import os
from flaskapp import create_app, db
from flaskapp.models import Report
from flaskapp.repository import RollbarRepository


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({ "TESTING": True, 
                        "WTF_CSRF_ENABLED": False, 
                        "SQLALCHEMY_DATABASE_URI": os.getenv('TEST_DATABASE_URI',
                                        default=f"sqlite:///test.db")

                    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


@pytest.fixture()
def init_database(client):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    dict_data = {
  "err": 0,
  "result": [
    {
      "counts": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        3,
        0,
        0
      ],
      "item": {
        "counter": 11,
        "environment": "development",
        "framework": 0,
        "group_status": 1,
        "id": 1350424236,
        "last_occurrence_timestamp": 1669884940,
        "level": 40,
        "occurrences": 3,
        "project_id": 604161,
        "title": "Message from CLI 12",
        "unique_occurrences": null
      }
    },
    {
      "counts": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        3,
        0,
        0
      ],
      "item": {
        "counter": 12,
        "environment": "unknown",
        "framework": 0,
        "group_status": 1,
        "id": 1350427779,
        "last_occurrence_timestamp": 1669884889,
        "level": 40,
        "occurrences": 3,
        "project_id": 604161,
        "title": "Message from CLI 13",
        "unique_occurrences": null
      }
    },
    {
      "counts": [0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        0,
        0
      ],
      "item": {
        "counter": 10,
        "environment": "production",
        "framework": 0,
        "group_status": 1,
        "id": 1350423454,
        "last_occurrence_timestamp": 1669883677,
        "level": 40,
        "occurrences": 2,
        "project_id": 604161,
        "title": "Updated title",
        "unique_occurrences": null
      }
    },
    {
      "counts": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0
      ],
      "item": {
        "counter": 13,
        "environment": "unknown",
        "framework": 0,
        "group_status": 1,
        "id": 1350428891,
        "last_occurrence_timestamp": 1669884686,
        "level": 40,
        "occurrences": 1,
        "project_id": 604161,
        "title": "Hello, world!",
        "unique_occurrences": null
      }
    }
  ]
}
    rep = Report(content=dict_data)
    db.session.add(rep)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()

