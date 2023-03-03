#!/bin/bash

set -euo pipefail

rundir=$(dirname $0)
cookiecutter_directory="$1"
repository_root="$(git rev-parse --show-toplevel)"

for test in $(find "${cookiecutter_directory}/examples" -maxdepth 1 -mindepth 1 -type d); do
	rm --recursive --force -- "${test}/output"
	poetry run cookiecutter \
		--no-input \
		--config-file "${test}/cookiecutter.yaml" \
		--output-dir "${test}/output" \
		--directory "${cookiecutter_directory}" \
		--overwrite-if-exists \
		"${repository_root}"
done
