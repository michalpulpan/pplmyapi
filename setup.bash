source env/bin/activate
python3 setup.py sdist
twine upload dist/* --verbose