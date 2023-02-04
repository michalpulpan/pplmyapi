# source env/bin/activate
# python3 setup.py sdist
# twine upload dist/* --verbose
python3 -m build
twine upload --repository pypi dist/*