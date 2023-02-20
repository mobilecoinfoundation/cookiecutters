<!-- markdownlint-disable -->
{%- if cookiecutter.type == "workspace" %}
# {{ cookiecutter.workspace_readme_title }}
{%- else %}
# {{ cookiecutter.crate_readme_title }}
{%- endif %}
<!-- markdownlint-enable -->

[![Project Chat][chat-image]][chat-link]<!--
-->![License][license-image]<!--
{%- if cookiecutter.type == "single-crate" %}
-->![Target][target-image]<!--
-->[![Crates.io][crate-image]][crate-link]<!--
-->[![Docs Status][docs-image]][docs-link]<!--
{%- endif %}
-->[![Dependency Status][deps-image]][deps-link]<!--
-->[![CodeCov Status][codecov-image]][codecov-link]<!--
-->[![GitHub Workflow Status][gha-image]][gha-link]<!--
-->[![Contributor Covenant][conduct-image]][conduct-link]
{% if cookiecutter.type == "workspace" %}
{{ cookiecutter.workspace_description }}
{%- else %}
{{ cookiecutter.crate_description }}
{%- endif %}

[chat-image]: https://img.shields.io/discord/844353360348971068?style=flat-square
[chat-link]: https://mobilecoin.chat
[license-image]: https://img.shields.io/crates/l/{{ cookiecutter.crate_name }}?style=flat-square
{%- if cookiecutter.type == "single-crate" %}
[target-image]: https://img.shields.io/badge/target-any-brightgreen?style=flat-square
[crate-image]: https://img.shields.io/crates/v/{{ cookiecutter.crate_name }}.svg?style=flat-square
[crate-link]: https://crates.io/crates/{{ cookiecutter.crate_name }}
[docs-image]: https://img.shields.io/docsrs/{{ cookiecutter.crate_name }}?style=flat-square
[docs-link]: https://docs.rs/crate/{{ cookiecutter.crate_name }}
{%- endif %}
[deps-image]: https://deps.rs/repo/github/mobilecoinfoundation/{{ cookiecutter.repo_name }}/status.svg?style=flat-square
[deps-link]: https://deps.rs/repo/github/mobilecoinfoundation/{{ cookiecutter.repo_name }}
[codecov-image]: https://img.shields.io/codecov/c/github/mobilecoinfoundation/{{ cookiecutter.repo_name }}/develop?style=flat-square
[codecov-link]: https://codecov.io/gh/mobilecoinfoundation/{{ cookiecutter.repo_name }}
[gha-image]: https://img.shields.io/github/workflow/status/mobilecoinfoundation/{{ cookiecutter.repo_name }}/ci.yaml?branch=main&style=flat-square
[gha-link]: https://github.com/mobilecoinfoundation/{{ cookiecutter.repo_name }}/actions/workflows/ci.yaml?query=branch%3Amain
[conduct-link]: CODE_OF_CONDUCT.md
[conduct-image]: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg?style=flat-square
