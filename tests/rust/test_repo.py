# Copyright (c) 2023 The MobileCoin Foundation
from cookiecutter.main import cookiecutter
from ..paths import DiffPath, TEMPLATE_ROOT
import yaml
import toml

DEFAULT_REPO_DIR = TEMPLATE_ROOT / "tests/rust/repo/expected/default/repository"
AGPL_ALLOW_LICENSES = [
    "Apache-2.0",
    "Apache-2.0 WITH LLVM-exception",
    "BSD-3-Clause",
    "ISC",
    "MIT",
    "Unicode-DFS-2016",
    "GPL-3.0-only",
    "GPL-3.0-or-later",
    "LGPL-3.0-only",
    "LGPL-3.0-or-later",
    "AGPL-3.0-only",
    "AGPL-3.0-or-later",
]
AGPL_LICENSE = TEMPLATE_ROOT / "tests/expected/licenses/AGPL-3.0-only"


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


def test_agpl(tmp_path):
    config = {"default_context": {"license": "AGPL-3.0-only"}}
    config_file = tmp_path / "config.yaml"
    with config_file.open(mode="w") as f:
        yaml.dump(config, f)

    cookiecutter(
        str(TEMPLATE_ROOT),
        directory="rust/repo",
        no_input=True,
        output_dir=tmp_path,
        config_file=config_file,
    )

    expected = DiffPath(DEFAULT_REPO_DIR)
    actual_path = tmp_path / "repository"
    actual = DiffPath(actual_path)
    actual.exclude(("Cargo.toml", "deny.toml", "LICENSE"))

    assert expected == actual

    cargo_toml = toml.load(actual_path / "Cargo.toml")
    assert cargo_toml["workspace"]["package"]["license"] == "AGPL-3.0-only"

    deny_toml = toml.load(actual_path / "deny.toml")
    assert deny_toml["licenses"]["allow"] == AGPL_ALLOW_LICENSES
    assert deny_toml["licenses"]["copyleft"] == "allow"
    assert deny_toml["licenses"]["allow-osi-fsf-free"] == "both"

    actual_license = DiffPath(actual_path / "LICENSE")
    assert DiffPath(AGPL_LICENSE) == actual_license
