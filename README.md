# Quality stages on Python development

This is a repository with the contents of the presentation about "Quality stages on Python development" as part of [Pyladies 9 years Anniversary event on 19.10.23 from Pyladies Munich](https://www.meetup.com/pyladiesmunich/events/296183247/).

> In this talk, we are going to cover a set of tools that will help you write and maintain standardized, reliable and high-quality code.

## Table of contents

- [Quality stages on Python development](#quality-stages-on-python-development)
  - [Table of contents](#table-of-contents)
  - [Slides](#slides)
  - [Branches](#branches)
    - [Raw](#raw)
  - [How to run](#how-to-run)
    - [Dependencies](#dependencies)
    - [Initial setup](#initial-setup)
    - [Running locally](#running-locally)

## Slides

The presentation slides can be found in the root of the project: [Quality stages of Python development.pdf](<Quality stages of Python development.pdf>)

## Branches

This repo contains different branches to apply the concepts of the presentation step by step:

- [`raw_1`](#raw): represents the initial code, without applying any linter.
- `auto_2`: just with the configuration of the IDE (VSCode) and the help of extensions, the code gets formatted.
- `types_3`: adds type hint and a couple of tests.
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

### Running locally

In the root folder of the project, run with:

```bash
python src/app.py
```
