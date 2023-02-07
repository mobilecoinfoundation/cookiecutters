# rust-workspace-cookiecutter

A [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) for creating a
rust workspace.

## Table of Contents

- [Walkthrough](#walkthrough)
  - [Invocation](#invocation)
  - [Output](#output)
- [Installing cookiecutter](#installing-cookiecutter)
- [Usage](#usage)
  - [New Repository](#new-repository)
  - [Pre-existing Repository](#pre-existing-repository)
- [Settings](#settings)
  - [`repo_name`](#repo\_name)
  - [`workspace_description`](#workspace\_description)
  - [`workspace_readme_title`](#workspace\_readme\_title)
  - [`crate_name`](#crate\_name)
  - [`crate_namespace_prefix`](#crate\_namespace\_prefix)
  - [`crate_description`](#crate\_description)
  - [`crate_readme_title`](#crate\_readme\_title)
  - [`crate_sub_dir`](#crate\_sub\_dir)
  - [`version`](#version)
  - [`crate_keywords`](#crate\_keywords)
  - [`crate_categories`](#crate\_categories)

## Walkthrough

We'll show how one might use this cookiecutter template to create a new rust
workspace.

### Invocation

> This assumes one has already [installed](#installing-cookiecutter)
> `cookiecutter`.

Invoking cookiecutter with this repository's URL,
`gh:nick-mobilecoin/rust-workspace-cookiecutter` will begin the process of
creating a workspace using the template.  

The first line is the `cookiecutter` invocation. The subsequent lines are
prompts from `cookiecutter`.

```console
> cookiecutter gh:nick-mobilecoin/rust-workspace-cookiecutter

repo_name [repository]: a_new_repo
workspace_description [A brief summary of the workspace]: My entered description of `a_new_repo`
workspace_readme_title [MobileCoin: My entered description of `a_new_repo`]: 
crate_name [mc-crate-name]: mc-an-initial-crate
crate_namespace_prefix [mc-]: 
crate_description [A brief summary of the crate]: Describing just the initial crate
crate_readme_title [MobileCoin: Describing just the initial crate]: 
crate_sub_dir [an/initial/crate]: 
version [0.1.0]: 
crate_keywords [blockchain serde]: no-std async cli
crate_categories [cryptography no-std]: api-bindings database gui
```

Each prompt follows a similar patter.

```console
repo_name [repository]: a_new_repo
```

The above prompt can be broken down into:

- `repo_name`: is the [setting](#settings) that `cookiecutter` is asking for.
- `[repository]`: the default value `cookiecutter` will use if nothing is
  entered.
- `a_new_repo`: is the value the author entered for this example.

Notice how some values in this example have no author input. For example:

```console
crate_namespace_prefix [mc-]: 
```

The default namespace prefix of `mc-` was chosen. As mentioned in
[`crate_namespace_prefix`](#crate\_namespace\_prefix), `mc-` will be removed from
the crate name of `mc-an-initial-crate` resulting in `an-initial-crate`. This
will further be converted from kebab case to a path resulting in the default
value of `an/initial/crate` being suggested for the `crate_sub_dir` prompt.

### Output

[Invoking](#invocation) cookiecutter above created the following directory
structure:

```console
a_new_repo
├── an
│   └── initial
│       └── crate
│           ├── Cargo.toml
│           ├── README.md
│           └── src
│               └── lib.rs
├── Cargo.toml
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── deny.toml
├── .github
│   ├── auto_assign.yaml
│   ├── CODEOWNERS
│   ├── dependabot.yaml
│   ├── labeler.yaml
│   ├── pull_request_template.md
│   ├── triage-labeler.yaml
│   └── workflows
│       ├── cargo-audit.yaml
│       ├── ci.yaml
│       ├── copyright.yaml
│       ├── issues.yaml
│       ├── pr-assign.yaml
│       └── pr.yaml
├── .gitignore
├── LICENSE
├── .markdownlint-cli2.jsonc
├── README.md
├── rustfmt.toml
└── rust-toolchain.toml
```

Some things to point out:

- There is a `.github` directory with some ready to go Github actions.
  Pushing this up as the main branch on a Github repository would start running
  these actions
- An initial rust crate was created in `an/initial/crate`. This is similar to
  creating a rust crate with `cargo  new --lib`.
- The initial rust crate will be listed in the root `Cargo.toml` `workspace`
  property.

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

## Usage

### New Repository

If starting locally one can do:

```console
cookiecutter gh:nick-mobilecoin/rust-workspace-cookiecutter
... prompts

cd <repo_name>
git init
git add .
git commit
```

This will create the rust workspace, and initialize it with a git repository.

### Pre-existing Repository

If one already created a git repository and wishes to initialize with the
cookiecutter:

```console
git clone https://github.com/mobilecoinfoundation/<repo_name>
cookiecutter gh:nick-mobilecoin/rust-workspace-cookiecutter --overwrite-if-exists
cd <repo_name>
git add .
git commit
```

## Settings

### repo\_name

The repository name. Will be used for the output directory. For example if one
wanted the repo `https://github.com/mobilecoinfoundation/new_stuff` then this
value would be
`new_stuff`

### workspace\_description

The description of the workspace. This will be the used as the text body of the
workspace (root) README.md. It will also seed the suggested
`workspace_readme_title`.

### workspace\_readme\_title

The title to use in the workspace (root) README.md.

### crate\_name

The name of the initial crate available in the worksapce. This should be the
full name. It will be used unmodified as the name in the Cargo.toml.

### crate\_namespace\_prefix

The prefix that is used in the `crate_name`. Often times crates are named along
the lines of `mc-my-crate` where `mc-` is used to namespace to MobileCoin. This
prefix is often omitted from the workspace directory structure. Be sure and
include the trailing `-` when explicitly setting this value.

### crate\_description

Description of the crate. Will be used as the text body of the crate's
README.md, the Cargo.toml, and seed the suggested `crate_readme_title`.

### crate\_readme\_title

The title to use in the crate's README.md.

### crate\_sub\_dir

The subdirectory to place the crate in. The suggested value is
the `crate_name` with the `crate_namespace_prefix` removed, converted from kebab
case to a directory. For example `mc-my-new-thing` with a prefix of `mc-` would
have a default subdirectory of `my/new/thing`. `mc-common-widget` with a prefix
of `mc-commmon-` would have a default subdirectory of `widget`.

### version

The initial version of the initial crate.

### crate\_keywords

The
[`keywords`](https://doc.rust-lang.org/cargo/reference/manifest.html#the-keywords-field)
field in initial crate's Cargo.toml. See <https://crates.io/keywords> for valid
keywords. Entered as a space separated list of values.

### crate\_categories

The
[`categories`](https://doc.rust-lang.org/cargo/reference/manifest.html#the-categories-field)
field in the initial crate's Cargo.toml.  See <https://crates.io/category_slugs>
for valid categories. Entered as a space separated list of values.
