# Rust Workspace Crate cookiecutter

A [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) for creating a
rust crate inside of a workspace.

## Table of Contents

- [Walkthrough](#walkthrough)
  - [Invocation](#invocation)
  - [Output](#output)
- [Settings](#settings)
  - [`crate_name`](#crate\_name)
  - [`crate_namespace_prefix`](#crate\_namespace\_prefix)
  - [`crate_description`](#crate\_description)
  - [`crate_readme_title`](#crate\_readme\_title)
  - [`crate_sub_dir`](#crate\_sub\_dir)
  - [`version`](#version)
  - [`repo_name`](#repo\_name)
  - [`crate_keywords`](#crate\_keywords)
  - [`crate_categories`](#crate\_categories)

## Walkthrough

We'll show how one might use this cookiecutter template to create a new rust
crate.

### Invocation

> This assumes one has already [installed](/README.md/#installing-cookiecutter)
> `cookiecutter`.

Invoking cookiecutter with this repository's URL and this directory,
`gh:mobilecoinfoundation/cookiecutters --directory rust-crate` will begin
the process of creating a crate using the template.  

The first line is the `cookiecutter` invocation. The subsequent lines are
prompts from `cookiecutter`.

```console
> cookiecutter gh:mobilecoinfoundation/cookiecutters --directory rust-crate

crate_name [mc-crate-name]: mc-some-nice-thing
crate_namespace_prefix [mc-]: 
crate_description [A brief summary of the crate]: A nice thing to do stuff with
crate_readme_title [MobileCoin: A nice thing to do stuff with]: 
version [0.1.0]: 
crate_sub_dir [some/nice/thing]: 
repo_name [a_repo]: 
crate_keywords [blockchain serde]: no-std async cli
crate_categories [cryptography no-std]: api-bindings
```

Each prompt follows a similar patter.

```console
repo_name [a_repo]: a_new_repo
```

The above prompt can be broken down into:

- `repo_name`: is the [setting](#settings) that `cookiecutter` is asking for.
- `[a_repo]`: the default value `cookiecutter` will use if nothing is
  entered.
- `a_new_repo`: is the value the author entered for this example.

Notice how some values in this example have no author input. For example:

```console
crate_namespace_prefix [mc-]: 
```

The default namespace prefix of `mc-` was chosen. As mentioned in
[`crate_namespace_prefix`](#crate\_namespace\_prefix), `mc-` will be removed from
the crate name of `mc-some-nice-thing` resulting in `some-nice-thing`. This
will further be converted from kebab case to a path resulting in the default
value of `some/nice/thing` being suggested for the `crate_sub_dir` prompt.

### Output

[Invoking](#invocation) cookiecutter above created the following directory
structure:

```console
some
└── nice
    └── thing
        ├── Cargo.toml
        ├── README.md
        └── src
            └── lib.rs
```

This is similar to invoking `cargo new --lib`. The difference being that this
provides a `README.md` in a common format and will add additional info to the
`Cargo.toml`

## Settings

### crate\_name

The name of the crate. This should be the full name. It will be used unmodified
as the name in the Cargo.toml.

### crate\_namespace\_prefix

The prefix that is used in the `crate_name`. Often times crates are named along
the lines of `mc-my-crate` where `mc-` is used to namespace to MobileCoin. This
prefix is often omitted from the crate directory structure. Be sure and
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

### repo\_name

The repository name. Will be used to populate the `repository` property in the
crate's `Cargo.toml`. When this cookiecutter template is executed inside of a
repository the default will be filled out using the current repository.

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
