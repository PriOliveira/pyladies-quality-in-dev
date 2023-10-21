# Quality stages on Python development

This is a repository with the contents of the presentation about "Quality stages on Python development" as part of [Pyladies 9 years Anniversary event on 19.10.23 from Pyladies Munich](https://www.meetup.com/pyladiesmunich/events/296183247/).

> In this talk, we are going to cover a set of tools that will help you write and maintain standardized, reliable and high-quality code.

## Table of contents

- [Quality stages on Python development](#quality-stages-on-python-development)
  - [Table of contents](#table-of-contents)
  - [Slides](#slides)
  - [Branches](#branches)
    - [Raw](#raw)
    - [Auto](#auto)
    - [Types and tests](#types-and-tests)
  - [How to run](#how-to-run)
    - [Dependencies](#dependencies)
    - [Initial setup](#initial-setup)
    - [Running locally](#running-locally)
    - [Tests](#tests)

## Slides

The presentation slides can be found in the root of the project: [Quality stages of Python development.pdf](<Quality stages of Python development.pdf>)

## Branches

This repo contains different branches to apply the concepts of the presentation step by step:

- [`raw_1`](#raw): represents the initial code, without applying any linter.
- [`auto_2`](#auto): just with the configuration of the IDE (VSCode) and the help of extensions, the code gets formatted.
- [`types_3`](#types-and-test): adds type hint and a couple of tests.
- `linter_4`: applies clean code, add more tests, fix some bugs.

Each branch has its `README.md` with more details about what is going on there and the tools used.

### Raw

In the `raw_1` branch the idea is to have a simple code and start without any tooling for checking the code.

Check the code in [`src/app.py`](src/app.py). There are many things that could be improved:

- The code is not intuitive about what is doing;
- There is no type hint;
- There are no tests;
- There is no documentation;
- There are many conditions in one of the functions;
- There is no input validation;
- And the **most important**, if you try to run the code, it crashes;

### Auto

In the `auto_2` branch the idea is to just use the auto formatting provided by some tools.

**First** either copy the [`app.py` from `raw_1`](https://github.com/PriOliveira/pyladies-quality-in-dev/blob/raw_1/src/app.py) and save without formatting it or just change back to `raw_1` branch and continue following the README in `auto_2` branch.

There are two options, both need that you install the dependencies, check [Initial setup section](#initial-setup).

One option is to just use the IDE (VSCode) with some extensions and invoke "Format Document" on `src/app.py`:
 - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
 - [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
 - [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

Another option is manually running them with:

```bash
# automatically fix any fixable problems, you can try running without the `--fix` flag to see the errors before fixing them.
ruff src --fix

# will automatically format the code for you
black src

# in this point you won't have any imports, but if you had, this would sort them according to PEP 8 (https://peps.python.org/pep-0008/#imports)
isort src
```

### Types and tests

In the branch `types_3` the idea is to check static typing and tests, both types and tests are now present in this branch. And there is one bug that got introduced when adding the types.

Here you'll need to install the dependencies again, since there are new libraries in `requirements-dev.txt`.

Stating with type hints, let's use `mypy` to check if the types are compatibles and correctly used. Run the following:

```bash
mypy src
```

There are some issues listed which are the root of the bug that was spotted in `raw_1` branch, this code does not work and crashes :(

Now moving on to tests, if you check [`tests/test_app.py`](tests/test_app.py) a couple of tests were added and they only cover Celsius conversions, still they catch the other bug in the code that was introduced when adding types to this branch.

To run the tests, check [How to run tests section](#tests).

## How to run

### Dependencies
- Python 3.11+ (probably works with older versions)

### Initial setup

If you are running this code for the first time or is setting up the repository from fresh state, then follow this section, otherwise feel free to skip it.

In the root folder of the project, create a virtual environment and activate it:

```bash
python -m venv env
source ./env/bin/activate
```

Install the dependencies with:
```bash
pip install -r requirements-dev.txt
```

### Running locally

In the root folder of the project, run with:

```bash
python src/app.py
```

### Tests

To run the tests, ensure that the development dependencies are installed [`requirements-dev.txt`](requirements-dev.txt), then run:

```bash
pytest tests
```
