import pytest
from ontrack.task_status import set_task_status, get_task_status

def test_default_status_is_not_started():
    result = get_task_status(student_id="s001", task_id="t001")
    assert result == "not started"

def test_get_status_after_setting_it():
    set_task_status(student_id="s002", task_id="t002", status="working on it")
    result = get_task_status(student_id="s002", task_id="t002")
    assert result == "working on it"

def test_get_status_need_help():
    set_task_status(student_id="s003", task_id="t003", status="need help")
    result = get_task_status(student_id="s003", task_id="t003")
    assert result == "need help"

def test_get_status_ready_for_feedback():
    set_task_status(student_id="s004", task_id="t004", status="ready for feedback")
    result = get_task_status(student_id="s004", task_id="t004")
    assert result == "ready for feedback"

def test_set_valid_status_returns_success():
    result = set_task_status(student_id="s001", task_id="t001", status="working on it")
    assert result == "success"

def test_set_invalid_status_returns_error():
    result = set_task_status(student_id="s001", task_id="t001", status="almost done")
    assert result == "invalid status"

def test_empty_student_id_returns_error():
    result = get_task_status(student_id="", task_id="t001")
    assert result == "invalid input"

def test_empty_task_id_returns_error():
    result = get_task_status(student_id="s001", task_id="")
    assert result == "invalid input"

def test_set_status_empty_student_id():
    result = set_task_status(student_id="", task_id="t001", status="working on it")
    assert result == "invalid input"

def test_set_status_empty_task_id():
    result = set_task_status(student_id="s001", task_id="", status="working on it")
    assert result == "invalid input"