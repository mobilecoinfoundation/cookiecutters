# Copyright (c) 2023 The MobileCoin Foundation
from cookiecutter.main import cookiecutter
from ..paths import DiffPath, TEMPLATE_ROOT


def test_default_repo_render(tmp_path):
    cookiecutter(
        str(TEMPLATE_ROOT),
        directory="rust/repo",
        no_input=True,
        default_config=True,
        output_dir=tmp_path,
    )

    expected = DiffPath(TEMPLATE_ROOT / "tests/rust/repo/expected/default")
    actual = DiffPath(tmp_path)

    assert expected == actual
