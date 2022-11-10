#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python3 manage.py collectstatic
python3 manage.py migrate