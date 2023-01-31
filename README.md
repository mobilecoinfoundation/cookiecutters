# rust-workspace-cookiecutter

A [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) for creating a
rust workspace.

## Usage

### New Repository

If starting locally one can do:

```console
cookiecutter gh:nick-mobilecoin/rust-workspace-cookiecutter
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
git clone <url_to_repo>
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
the lines of `mc-my-crate` where `mc` is used to namespace to MobileCoin. This
prefix is often omitted from the workspace directory structure.

### crate\_description

Description of the crate. Will be used as the text body of the crate's
README.md, the Cargo.toml, and seed the suggested `crate_readme_title`.

### crate\_readme\_title

The title to use in the crate's README.md.

### crate\_sub\_dir

The subdirectory to place the crate in. The suggested value is
derived from the `crate_name` sans the `crate_namespace_prefix`.

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
