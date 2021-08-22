# Python best practices
## Python Framework used
I used `Flask` as a framework for its simplicity and straightforward use.
## Package manager
I used `pdm` package manager. It has certain benefits over other package managers such as:
1. Fast and simple dependency resolver
2. No use of virtualenv
3. General simplicity and convenience
## Code formatting
I used following code formatters:
1. `isort` for formatting imports
2. `autopep8` for formatting code in a PEP8 style guide
## Linters
I used only `pylint` for linting my python code
## Testing
I used `pytest` for testing my application. It is convenient for testing small applications. Specifically I test availability of an API used.
## .gitignore
## Requirements
I generate `requirements.txt` file in a following way:<br/>
`pdm list --freeze >> requirements.txt`
