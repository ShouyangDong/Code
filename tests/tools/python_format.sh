# black format
black  transform/
black  tests/
pyupgrade --py38-plus transform/*.py
pyupgrade --py38-plus tests/python/*.py
pydocstringformatter --style=pep257 --write --no-split-summary-body --capitalize-first-letter transform/*.py
pydocstringformatter --style=pep257 --write --no-split-summary-body --capitalize-first-letter tests/python/*.py
