import shutil
import sys

REMOVE_PATHS = [
    '{% if cookiecutter.type == "workspace" %} src {% endif %}',
    '{% if cookiecutter.type == "single-crate" %} {{ cookiecutter.crate_sub_dir }} {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    shutil.rmtree(path, ignore_errors=True)

