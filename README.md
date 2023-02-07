# python_check_updates

Update a setup.py or pypackage.toml file automatically,
like the [npm-check-updates](https://www.npmjs.com/package/npm-check-updates) tool 

# Print updated list of packages

```
$ python3 ./python_check_updates.py setup.py
$ python3 ./python_check_updates.py pypackage.toml
```

## Convert to a different format

Specify the `--format-type` flag to change the output format of the list of dependencies.

```
$ python3 ./python_check_updates.py pypackage.toml --format-type requirements.txt
$ python3 ./python_check_updates.py requirements.txt --format-type setup.py
```

# Roadmap

## Features

- [x] load a setup.py file
- [ ] load a requirements.txt file
- [ ] load a pyproject.toml file
- [x] output in the format of a setup.py file
- [ ] output in the format of a requirements.txt file
- [ ] output in the format of a pyproject.toml file
- [ ] in-place file editing

## Developer UX and code quality

- [ ] code linting, formatting, type checking
- [ ] unit testing for many Python versions (pypy, 3.6+)
- [ ] deploy to pypi.org
