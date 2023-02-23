# {{ cookiecutter.crate_readme_title }}

[![Project Chat][chat-image]][chat-link]<!--
-->![License][license-image]<!--
-->![Architecture: {{ cookiecutter.arch }}][arch-image]<!--
-->[![Crates.io][crate-image]][crate-link]<!--
-->[![Docs Status][docs-image]][docs-link]<!--
-->[![Dependency Status][deps-image]][deps-link]

{{ cookiecutter.crate_description }}

[chat-image]: https://img.shields.io/discord/844353360348971068?style=flat-square
[chat-link]: https://mobilecoin.chat
[license-image]: https://img.shields.io/crates/l/{{ cookiecutter.crate_name }}?style=flat-square
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
[deps-image]: https://deps.rs/crate/{{ cookiecutter.crate_name }}/{{ cookiecutter.version }}/status.svg?style=flat-square
[deps-link]: https://deps.rs/crate/{{ cookiecutter.crate_name }}/{{ cookiecutter.version }}
