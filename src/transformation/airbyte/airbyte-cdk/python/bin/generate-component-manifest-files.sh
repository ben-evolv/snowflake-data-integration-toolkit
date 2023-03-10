#!/usr/bin/env bash

set -e

[ -z "$ROOT_DIR" ] && exit 1

YAML_DIR=airbyte-cdk/python/airbyte_cdk/sources/declarative
OUTPUT_DIR=airbyte-cdk/python/airbyte_cdk/sources/declarative/models

function main() {
  rm -rf "$ROOT_DIR/$OUTPUT_DIR"/*.py
  echo "# generated by generate-component-manifest-files" > "$ROOT_DIR/$OUTPUT_DIR"/__init__.py

  for f in "$ROOT_DIR/$YAML_DIR"/*.yaml; do
    filename_wo_ext=$(basename "$f" | cut -d . -f 1)
    echo "from .$filename_wo_ext import *" >> "$ROOT_DIR/$OUTPUT_DIR"/__init__.py

    docker run --user "$(id -u):$(id -g)" -v "$ROOT_DIR":/airbyte airbyte/code-generator:dev \
      --input "/airbyte/$YAML_DIR/$filename_wo_ext.yaml" \
      --output "/airbyte/$OUTPUT_DIR/$filename_wo_ext.py" \
      --use-title-as-name \
      --disable-timestamp \
      --enum-field-as-literal one
  done
}

main "$@"
