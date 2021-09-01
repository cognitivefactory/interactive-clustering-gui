# Interactive Clustering GUI

[![ci](https://github.com/cognitivefactory/interactive-clustering-gui/workflows/ci/badge.svg)](https://github.com/cognitivefactory/interactive-clustering-gui/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://cognitivefactory.github.io/interactive-clustering-gui/)
[![pypi version](https://img.shields.io/pypi/v/cognitivefactory-interactive-clustering-gui.svg)](https://pypi.org/project/cognitivefactory-interactive-clustering-gui/)
[![DOI](https://zenodo.org/badge/368196296.svg)](https://zenodo.org/badge/latestdoi/368196296)

An annotation tool for NLP data based on Interactive Clustering methodology.

## <a name="Description"></a> Quick description

_TODO_

## <a name="Documentation"></a> Documentation

- [Main documentation](https://cognitivefactory.github.io/interactive-clustering-gui/)

## <a name="Requirements"></a> Requirements

Interactive Clustering GUI requires Python 3.6 or above.

<details>
<summary>To install Python 3.6, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>

```bash
# install pyenv
git clone https://github.com/pyenv/pyenv ~/.pyenv

# setup pyenv (you should also put these three lines in .bashrc or similar)
export PATH="${HOME}/.pyenv/bin:${PATH}"
export PYENV_ROOT="${HOME}/.pyenv"
eval "$(pyenv init -)"

# install Python 3.6
pyenv install 3.6.12

# make it available globally
pyenv global system 3.6.12
```
</details>

## <a name="Installation"></a> Installation

With `pip`:
```bash
# install package
python3 -m pip install cognitivefactory-interactive-clustering-gui

# install spacy language model dependencies (the one you want, with version "^2.3")
python3 -m spacy download fr_core_news_sm-2.3.0 --direct
```

With [`pipx`](https://github.com/pipxproject/pipx):
```bash
# install pipx
python3 -m pip install --user pipx

# install package
pipx install --python python3 cognitivefactory-interactive-clustering-gui

# install spacy language model dependencies (the one you want, with version "^2.3")
python3 -m spacy download fr_core_news_sm-2.3.0 --direct
```

## <a name="Development"></a> Development

To work on this project or contribute to it, please read
[the Copier PDM documentation](https://pawamoy.github.io/copier-pdm/).

### Quick setup and help

Get the code and prepare the environment:

```bash
git clone https://github.com/cognitivefactory/interactive-clustering-gui/
cd interactive-clustering-gui
make setup
```

Show the help:

```bash
make help  # or just make
```

## <a name="References"></a> References

_TODO_
