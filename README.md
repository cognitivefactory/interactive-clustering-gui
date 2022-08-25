# Interactive Clustering GUI

[![ci](https://github.com/cognitivefactory/interactive-clustering-gui/workflows/ci/badge.svg)](https://github.com/cognitivefactory/interactive-clustering-gui/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://cognitivefactory.github.io/interactive-clustering-gui/)
[![pypi version](https://img.shields.io/pypi/v/cognitivefactory-interactive-clustering-gui.svg)](https://pypi.org/project/cognitivefactory-interactive-clustering-gui/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4775270.svg)](https://doi.org/10.5281/zenodo.4775270)


An annotation tool for NLP data based on Interactive Clustering methodology.

## <a name="Description"></a> Quick description

_Interactive clustering_ is a method intended to assist in the design of a training data set.

This iterative process begins with an unlabeled dataset, and it uses a sequence of two substeps :

1. the user defines constraints on data sampled by the computer ;

2. the computer performs data partitioning using a constrained clustering algorithm.

Thus, at each step of the process :

- the user corrects the clustering of the previous steps using constraints, and

- the computer offers a corrected and more relevant data partitioning for the next step.

This web application implements this annotation methodology with several features:

- _data preprocessing and vectorization_ in order to reduce noise in data;
- _constrainted clustering_ in order to automatically partition the data;
- _constraints sampling_ in order to select the most relevant data to annotate;
- _binary constraints annotation_ in order to correct clustering relevance;
- _annotation review and conflicts analysis_ in order to improve constraints consistency.

- For more details, read the [Documentation](#Documentation) and the articles in the [References](#References) section.

## <a name="Documentation"></a> Documentation

- [Main documentation](https://cognitivefactory.github.io/interactive-clustering-gui/)

## <a name="Requirements"></a> Requirements

Interactive Clustering GUI requires Python 3.7 or above.

<details>
<summary>To install Python 3.7, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>

```bash
# install pyenv
git clone https://github.com/pyenv/pyenv ~/.pyenv

# setup pyenv (you should also put these three lines in .bashrc or similar)
export PATH="${HOME}/.pyenv/bin:${PATH}"
export PYENV_ROOT="${HOME}/.pyenv"
eval "$(pyenv init -)"

# install Python 3.7
pyenv install 3.7

# make it available globally
pyenv global system 3.7
```
</details>

## <a name="Installation"></a> Installation

With `pip`:
```bash
# install package
python3 -m pip install cognitivefactory-interactive-clustering-gui

# install spacy language model dependencies (the one you want, with version "3.1.x")
python3 -m spacy download fr_core_news_md-3.1.0 --direct
```

With [`pipx`](https://github.com/pipxproject/pipx):
```bash
# install pipx
python3 -m pip install --user pipx

# install package
pipx install --python python3 cognitivefactory-interactive-clustering-gui

# install spacy language model dependencies (the one you want, with version "3.1.x")
python3 -m spacy download fr_core_news_md-3.1.0 --direct
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

For more details, read the [Contributing](https://cognitivefactory.github.io/interactive-clustering-gui/contributing/) documentation.

## <a name="References"></a> References

- **Interactive Clustering**:
    - First presentation: `Schild, E., Durantin, G., Lamirel, J.C., & Miconi, F. (2021). Conception itérative et semi-supervisée d'assistants conversationnels par regroupement interactif des questions. In EGC 2021 - 21èmes Journées Francophones Extraction et Gestion des Connaissances. Edition RNTI. ⟨hal-03133007⟩.`
    - Theoretical study: `Schild, E., Durantin, G., Lamirel, J., & Miconi, F. (2022). Iterative and Semi-Supervised Design of Chatbots Using Interactive Clustering. International Journal of Data Warehousing and Mining (IJDWM), 18(2), 1-19. http://doi.org/10.4018/IJDWM.298007. ⟨hal-03648041⟩.`
    - Methodological discussion: `Schild, E., Durantin, G., & Lamirel, J.C. (2021). Concevoir un assistant conversationnel de manière itérative et semi-supervisée avec le clustering interactif. In Atelier - Fouille de Textes - Text Mine 2021 - En conjonction avec EGC 2021. ⟨hal-03133060⟩.`
    - Implementation: `Schild, E. (2021). cognitivefactory/interactive-clustering. Zenodo. https://doi.org/10.5281/zenodo.4775251.`

- **Web application**:
    - _FastAPI_: `https://fastapi.tiangolo.com/`

## <a name="How to cite"></a> How to cite

`Schild, E. (2021). cognitivefactory/interactive-clustering-gui. Zenodo. https://doi.org/10.5281/zenodo.4775270.`