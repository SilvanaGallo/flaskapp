import pytest
import cli

#inclomplete I found it in the docs but I didn't have time to do it
def test_get_items_command(runner)-> None:
    result = runner.invoke(args="get-items")
    assert "World" in result.output

    result = runner.invoke(args=["hello", "--name", "Flask"])
    assert "Flask" in result.output


def test_add_item_command(runner)-> None:
    result = runner.invoke(args="add-item")
    assert "World" in result.output

    result = runner.invoke(args=["hello", "--name", "Flask"])
    assert "Flask" in result.output


def test_get_item_command(runner)-> None:
    result = runner.invoke(args="get-item")
    assert "World" in result.output

    result = runner.invoke(args=["hello", "--name", "Flask"])
    assert "Flask" in result.output