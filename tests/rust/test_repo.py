# Copyright (c) 2023 The MobileCoin Foundation
from cookiecutter.main import cookiecutter
from filecmp import dircmp


def dirs_the_same(dirs):
    """
    Returns true when `dirs` and all its subdirectories are the same
    """
    if dirs.diff_files != []:
        return False

    return all(dirs_the_same(d) for d in dirs.subdirs.values())


def test_default_repo_render(template_root, tmp_path):
    cookiecutter(
        str(template_root),
        directory="rust/repo",
        no_input=True,
        default_config=True,
        output_dir=tmp_path,
    )

    dirs = dircmp(tmp_path, template_root / "tests/rust/repo/expecteds/default")

    assert dirs_the_same(dirs)
