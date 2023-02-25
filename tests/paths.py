# Copyright (c) 2023 The MobileCoin Foundation

import filecmp
from filecmp import dircmp, DEFAULT_IGNORES
from pathlib import Path

#: The root of this repository. This can be used as the `template` parameter to
#: `cookiecutter` specifying the directory to the desired template as one would
#: do on the command line.
TEMPLATE_ROOT = Path(__file__).parent.parent


class DiffPath:
    """
    Provides a way of comparing paths for use with pytest.

    Implements an `==` operator that looks at the path contents of
    both `a` and `b` in `a == b`.

    Args:
        path(Path): Can be a directory or file. Directories will recursively
            compare all files and directories. When a file, only the file
            contents will be compared.
    """

    def __init__(self, path):
        self.path = path

        # Not sure why but dircmp has `hide` and `ignore`, both of those get
        # added together and behave the same...
        # Be sure and copy `DEFAULT_IGNORES` since it's a list, not a tuple
        # We need to ensure we don't accidentally modify it.
        self.excludes = list(DEFAULT_IGNORES)

    def diff(self, other):
        """
        Compare the file(s) in `self` to `other` and return a list of the files
        and directories that differ. Paths which have been added to
        :meth:`exclude()` will not be considered in the comparison.

        Returns:
            List[tuple(Path, Path)]: Where the first item is a `Path` in
            `self` and the second item is a `Path` in `other`. There
            are 3 cases:
                - (Path, None): Means a file or directory exists in `self` but
                  not `other`
                - (None, Path): Means a file or directory exists ln the `other`
                  but not `self`
                - (Path, Path): Means a file or directory exists in both `self`
                  and `other` but the contents are different.

            The paths to files and directories will be the full paths

            If `self` and `other` refer to  files, then the returned list will
            be a list with only one tuple, the filenames of `self` and `other`.
        """
        diffs = []
        if self.path.is_dir() and other.path.is_dir():
            ignore = self.excludes + other.excludes
            dirs = dircmp(self.path, other.path, ignore=ignore)
            diffs = diff_dirs(dirs)
        else:
            result = filecmp.cmp(self.path, other.path)
            if not result:
                diffs = [(self.path, other.path)]

        return diffs

    def __eq__(self, other):
        if self.diff(other):
            return False

        return True

    def exclude(self, excludes):
        """
        Will omit entries in `excludes` from being compared in :meth:`diff()`
        and the `==` operator.

        Args:
            excludes(Seq[str]): A sequence of strings for the names of files or
                directories to exclude. These should be names without parent
                paths. This means that *all* files with that name will be
                excluded. For example "Cargo.toml" would exclude all
                "Cargo.toml" files in the directory tree.
        """
        self.excludes.extend(excludes)


def diff_dirs(dirs):
    """
    Returns:
        List[tuple(Path, Path)]: Where the first item is a `Path` in `dirs.left`
        and the second item is a `Path` in `dirs.right`. There are 3 cases:
            - (Path, None): Means a file or directory exists on the left but
              not the right
            - (None, Path): Means a file or directory exists on the right but
              not the left
            - (Path, Path): Means a file or directory exists on both the left
              and the right but the contents are different.

        The paths to files and directories will be the full paths
    """
    left_path = Path(dirs.left)
    right_path = Path(dirs.right)
    diffs = []
    diffs.extend((left_path / f, None) for f in dirs.left_only)
    diffs.extend((None, right_path / f) for f in dirs.right_only)
    diffs.extend((left_path / f, right_path / f) for f in dirs.diff_files)

    for subdir in dirs.subdirs.values():
        diffs.extend(diff_dirs(subdir))

    return diffs
