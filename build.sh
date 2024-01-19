#!/usr/bin/env bash

set -o errexit

make install
make collect-static
make migrate
