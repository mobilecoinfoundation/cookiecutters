{%- if cookiecutter.type == "workspace" -%}
# {{ cookiecutter.workspace_readme_title }}
{%- else -%}
# {{ cookiecutter.crate_readme_title }}
{%- endif %}

[![Project Chat][chat-image]][chat-link]<!--
-->![License][license-image]<!--
{%- if cookiecutter.type == "single-crate" %}
-->![Architecture: {{ cookiecutter.arch }}][arch-image]<!--
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
[chat-link]: https://discord.gg/mobilecoin
[license-image]: https://img.shields.io/crates/l/{{ cookiecutter.crate_name }}?style=flat-square
{%- if cookiecutter.type == "single-crate" %}
{%- if cookiecutter.arch == "sgx" %}
[arch-image]: https://img.shields.io/badge/arch-sgx-red?style=flat-square
{%- elif cookiecutter.arch == "any" %}
[arch-image]: https://img.shields.io/badge/arch-any-brightgreen?style=flat-square
{%- else %}
[arch-image]: https://img.shields.io/badge/arch-{{ cookiecutter.arch.replace('_', '__') }}-blue?style=flat-square
{%- endif %}
[crate-image]: https://img.shields.io/crates/v/{{ cookiecutter.crate_name }}.svg?style=flat-square
[crate-link]: https://crates.io/crates/{{ cookiecutter.crate_name }}
[docs-image]: https://img.shields.io/docsrs/{{ cookiecutter.crate_name }}?style=flat-square
[docs-link]: https://docs.rs/crate/{{ cookiecutter.crate_name }}
{%- endif %}
{%- if cookiecutter.type == "workspace" %}
[deps-image]: https://deps.rs/repo/github/mobilecoinfoundation/{{ cookiecutter.repo_name }}/status.svg?style=flat-square
[deps-link]: https://deps.rs/repo/github/mobilecoinfoundation/{{ cookiecutter.repo_name }}
{%- else %}
[deps-image]: https://deps.rs/crate/{{ cookiecutter.crate_name }}/{{ cookiecutter.version}}/status.svg?style=flat-square
[deps-link]: https://deps.rs/crate/{{ cookiecutter.crate_name }}/{{ cookiecutter.version }}
{%- endif %}
[codecov-image]: https://img.shields.io/codecov/c/github/mobilecoinfoundation/{{ cookiecutter.repo_name }}/main?style=flat-square
[codecov-link]: https://codecov.io/gh/mobilecoinfoundation/{{ cookiecutter.repo_name }}
[gha-image]: https://img.shields.io/github/actions/workflow/status/mobilecoinfoundation/{{ cookiecutter.repo_name }}/ci.yaml?branch=main&style=flat-square
[gha-link]: https://github.com/mobilecoinfoundation/{{ cookiecutter.repo_name }}/actions/workflows/ci.yaml?query=branch%3Amain
[conduct-link]: CODE_OF_CONDUCT.md
[conduct-image]: https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg?style=flat-square
