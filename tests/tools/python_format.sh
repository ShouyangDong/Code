# black format
black  transform/
black  tests/
black  encoding/
pyupgrade --py38-plus transform/*.py
pyupgrade --py38-plus tests/python/*.py
pyupgrade --py38-plus encoding/*.py
pydocstringformatter --style=pep257 --write --no-split-summary-body --capitalize-first-letter transform/*.py
pydocstringformatter --style=pep257 --write --no-split-summary-body --capitalize-first-letter tests/python/*.py
pydocstringformatter --style=pep257 --write --no-split-summary-body --capitalize-first-letter encoding/*.py
