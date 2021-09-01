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
I used `pytest` for testing my application. It is convenient for testing small applications. I testes the availability of my application. Here are the best practices I used in my Unit Tests:<br/>
- Tests need to be fast and simple. Since our application is small it was easy to achieve this goal.
- Tests should not copy the implementation logic of the application. Previously I implemented tests that basivally mirrored the way my app works. Now I use different methods to check if my app works.
- Tests should be readable. My tests are simple, use `assert` keyword and have comments provided with them.
- Tests need to be deterministic. Tests I implemeted return the same result if the project is not changed.
- Tests shouldn't be coupled with implementation details. My tests are not aware of any deployment details or application logic.
## .gitignore
## Requirements
I generate `requirements.txt` file in a following way:<br/>
`pdm list --freeze >> requirements.txt`
