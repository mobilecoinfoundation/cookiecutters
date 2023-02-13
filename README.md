# Cookiecutter Templates

A collection of [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
templates for use in MobileCoinFoundation repositories.

Each subdirectory contains a `cookiecutter` template. See individual README
files for more details on what each one does.

## Usage

Invoking `cookiecutter` with this repository requires the use of the
[`--directory`](https://cookiecutter.readthedocs.io/en/stable/cli_options.html#cmdoption-cookiecutter-directory)
option.

For example to use the `rust-workspace` template.

```console
cookiecutter gh:mobilecoinfoundation/cookiecutters --directory rust-workspace
```

## Installing cookiecutter

To install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
consider using something like [pipx](https://pypa.github.io/pipx/).

The advantage to using `pipx` is that `cookiecutter` will be installed in an
isolated python environment.

> Note:
> The following suggested install is isolated to the current user. This means
> the use `sudo` is not needed, or recommended. Using `sudo` with these specific
> commands will almost certainly cause issues.

Install pipx:

```console
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Restart your terminal

Install cookiecutter:

```console
pipx install cookiecutter
```

There is alternate installation instructions provided by the `cookiecutter`
docs, <https://cookiecutter.readthedocs.io/en/stable/installation.html>, however
this results in pulling `cookiecutter` dependencies into the system or user python
environment.
