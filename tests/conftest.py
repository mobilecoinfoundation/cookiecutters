# Copyright (c) 2023 The MobileCoin Foundation

from .paths import DiffPath
import seedir as sd
import difflib


def pytest_assertrepr_compare(op, left, right):
    """
    Custom assert representation for `DiffPath` objects
    See https://docs.pytest.org/en/7.1.x/how-to/assert.html#defining-your-own-explanation-for-failed-assertions
    """
    if not (isinstance(left, DiffPath) and isinstance(right, DiffPath) and op == "=="):
        return None

    diffs = left.diff(right)

    message = ["Comparing Directory Contents"]
    for left, right in diffs:
        message.extend(diff_paths(left, right))

    return message


def diff_paths(left, right):
    """
    Return an iterable of the string representation of a diff between 2 Paths
    """
    left_contents = path_contents(left).splitlines()
    right_contents = path_contents(right).splitlines()

    return difflib.unified_diff(
        left_contents,
        right_contents,
        fromfile=str(left),
        tofile=str(right),
        lineterm="",
    )


def path_contents(path):
    """
    Get the contents of a path. If `path` is a file it will be the file
    contents. If `path` is a directory it will be a tree listing of the files
    similar to the unix `tree` utility.

    If `path` is none this will be an empty string
    """
    if not path:
        return ""

    if path.is_dir():
        tree = sd.seedir(path, printout=False)
        return tree

    with open(path) as f:
        return f.read()
