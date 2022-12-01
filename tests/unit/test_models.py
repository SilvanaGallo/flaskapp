import pytest
from flaskapp.models import Report

class TestReport:

    def test_empty_report_creation(self) -> None:
        rep: Report = Report()
        assert rep.content is None
        assert str(rep) == "Report(None)"

    def test_with_content_report_creation(self) -> None:
        js: dict = {'key': 'value'}
        rep = Report(content=js)
        assert rep.content == js
        assert str(rep) == f"Report({str(js)})"


