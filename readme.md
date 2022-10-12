Requirements:
    Python.
    Pipenv:
        pip install pipenv (how to install pipenv)
        
        pipenv install
        pipenv run python -m pytest (if this displays an error you must..)
            pipenv --python #pythonVersionInstalled
            pipenv update

            pipenv install pytest (if no module of pytest found)
        pipenv install selenium

To print in console a print(something) you should use the command pipenv run python -m pytest -s

Always is necessary to have a __init__.py on a python folder to let know that is a package of python.
The config.json file wichis located on the project, is to set the browser as headless and a to keep the implicit wait to 10 for example.
The conftest.py is to set fixtures.
On pages you get the objects from the page.
Is necesary to have a config.json file.
Pipfiles y .lock son dependencias.
