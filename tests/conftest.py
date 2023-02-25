# Copyright (c) 2023 The MobileCoin Foundation

from pathlib import Path
import pytest


@pytest.fixture
def template_root():
    """
    Provides the root directory of this repository. Cookie cutters can use this as the template value and then use the `directory` parameter to specify which cookie cutter template to use.
    """
    file_path = Path(__file__)
    root = file_path.parent.parent
    return root
