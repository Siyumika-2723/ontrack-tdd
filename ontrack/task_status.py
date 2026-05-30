# Valid statuses matching OnTrack's actual interface
VALID_STATUSES = [
    "not started",
    "working on it",
    "need help",
    "ready for feedback"
]

# In-memory store simulating a database
_task_store = {}


def get_task_status(student_id: str, task_id: str) -> str:
    """
    Returns the current status of a task for a given student.
    Defaults to 'not started' if no status has been set.
    """
    if not student_id or not task_id:
        return "invalid input"
    key = (student_id, task_id)
    return _task_store.get(key, "not started")


def set_task_status(student_id: str, task_id: str, status: str) -> str:
    """
    Sets the status of a task for a given student.
    Returns 'success' or an error string.
    """
    if not student_id or not task_id:
        return "invalid input"
    if status not in VALID_STATUSES:
        return "invalid status"
    key = (student_id, task_id)
    _task_store[key] = status
    return "success"