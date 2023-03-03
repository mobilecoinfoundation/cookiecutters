#!/bin/bash

set -euo pipefail

rundir=$(dirname $0)
cookiecutter_directory="$1"
default="${cookiecutter_directory}/examples/default"
repository_root="$(git rev-parse --show-toplevel)"

function generate_example() {
	example="$1"
	echo "Generating ${example}"
	rm --recursive --force -- "${example}/output"
	poetry run cookiecutter \
		--no-input \
		--config-file "${example}/cookiecutter.yaml" \
		--output-dir "${example}/output" \
		--directory "${cookiecutter_directory}" \
		--overwrite-if-exists \
		"${repository_root}"
}

poetry install

generate_example "${default}"

for example in $(find "${cookiecutter_directory}/examples" -maxdepth 1 -mindepth 1 -type d); do
	if [[ "x${example}" == "x${default}" ]]; then
		continue
	fi

	generate_example "${example}"

	# Dedupe via symlink
	rdfind \
		-checksum sha256 \
		-makesymlinks true \
		-makeresultsfile false \
		"${default}/output" \
		"${example}/output"

	# Make .gitignore a hardlink
	find -type l -name ".gitignore" -exec bash -c 'ln -f "$(readlink -m "$0")" "$0"' {} \;

	# Make symlinks relative
	symlinks -cr "${example}/output"
done
