# Interactive Clustering GUI

[![ci](https://github.com/cognitivefactory/interactive-clustering-gui/workflows/ci/badge.svg)](https://github.com/cognitivefactory/interactive-clustering-gui/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://cognitivefactory.github.io/interactive-clustering-gui/)
[![pypi version](https://img.shields.io/pypi/v/cognitivefactory-interactive-clustering-gui.svg)](https://pypi.org/project/cognitivefactory-interactive-clustering-gui/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4775270.svg)](https://doi.org/10.5281/zenodo.4775270)

A web application designed for NLP data annotation using Interactive Clustering methodology.


## <a name="Description"></a> Quick description

_Interactive clustering_ is a method intended to assist in the design of a training data set.

This iterative process begins with an unlabeled dataset, and it uses a sequence of two substeps :

1. the user defines constraints on data sampled by the computer ;
2. the computer performs data partitioning using a constrained clustering algorithm.

Thus, at each step of the process :

- the user corrects the clustering of the previous steps using constraints, and
- the computer offers a corrected and more relevant data partitioning for the next step.

<p align="center">
	<i align="center" style="font-size: smaller; color:grey">Simplified diagram of how Interactive Clustering works.</i>
	</br>
	<img src="docs/figures/interactive-clustering.png" alt="Simplified diagram of how Interactive Clustering works." width="75%"/>
	
</p>
<p align="center">
	<i style="font-size: smaller; color:grey">Example of iterations of Interactive Clustering.</i>
	</br>
	<img src="docs/figures/interactive-clustering-example.png" alt="Example of iterations of Interactive Clustering." width="90%"/>
</p>

This web application implements this annotation methodology with several features:

- _data preprocessing and vectorization_ in order to reduce noise in data;
- _constrainted clustering_ in order to automatically partition the data;
- _constraints sampling_ in order to select the most relevant data to annotate;
- _binary constraints annotation_ in order to correct clustering relevance;
- _annotation review and conflicts analysis_ in order to improve constraints consistency.

<p align="center">
	<i style="font-size: smaller; color:grey">Welcome page of Interactive Clustering Web Application.</i>
	</br>
	<img src="docs/figures/interactive-clustering-gui-welcome-page.png" alt="Welcome page of Interactive Clustering Web Application." width="75%"/>
</p>

For more details, read the [Documentation](#Documentation) and the articles in the [References](#References) section.


## <a name="Documentation"></a> Documentation

- [Main documentation](https://cognitivefactory.github.io/interactive-clustering-gui/)


## <a name="Requirements"></a> Requirements

Interactive Clustering GUI requires Python 3.8 or above.

To install with [`pip`](https://github.com/pypa/pip):

```bash
# install package
python3 -m pip install cognitivefactory-interactive-clustering-gui

# install spacy language model dependencies (the one you want, with version "3.4.x")
python3 -m spacy download fr_core_news_md-3.4.0 --direct
```

To install with [`pipx`](https://github.com/pypa/pipx):

```bash
# install pipx
python3 -m pip install --user pipx

# install package
pipx install --python python3 cognitivefactory-interactive-clustering-gui

# install spacy language model dependencies (the one you want, with version "3.4.x")
python3 -m spacy download fr_core_news_md-3.4.0 --direct
```


## <a name="Run"></a> Run

To display the help message:

```bash
cognitivefactory-interactive-clustering-gui --help
```

To launch the web application:

```bash
cognitivefactory-interactive-clustering-gui  # launch on 127.0.0.1:8080
```

Then, go to one of the following pages in your browser:

- Welcome page (web application home): [http://localhost:8080](http://localhost:8080)
- Swagger (interactive documentation): [http://localhost:8080/docs](http://localhost:8080/docs)


## <a name="Development"></a> Development


To work on this project or contribute to it, please read:

- the [Copier PDM](https://pawamoy.github.io/copier-pdm/) template documentation ;
- the [Contributing](https://cognitivefactory.github.io/interactive-clustering-gui/contributing/) page for environment setup and development help ;
- the [Code of Conduct](https://cognitivefactory.github.io/interactive-clustering-gui/code_of_conduct/) page for contribution rules.


## <a name="References"></a> References

- **Interactive Clustering**:
	- PhD report: `Schild, E. (2024, in press). De l'Importance de Valoriser l'Expertise Humaine dans l'Annotation : Application à la Modélisation de Textes en Intentions à l'aide d'un Clustering Interactif. Université de Lorraine.` ;
	- First presentation: `Schild, E., Durantin, G., Lamirel, J.C., & Miconi, F. (2021). Conception itérative et semi-supervisée d'assistants conversationnels par regroupement interactif des questions. In EGC 2021 - 21èmes Journées Francophones Extraction et Gestion des Connaissances. Edition RNTI. <hal-03133007>.`
	- Theoretical study: `Schild, E., Durantin, G., Lamirel, J., & Miconi, F. (2022). Iterative and Semi-Supervised Design of Chatbots Using Interactive Clustering. International Journal of Data Warehousing and Mining (IJDWM), 18(2), 1-19. http://doi.org/10.4018/IJDWM.298007. <hal-03648041>.`
	- Methodological discussion: `Schild, E., Durantin, G., & Lamirel, J.C. (2021). Concevoir un assistant conversationnel de manière itérative et semi-supervisée avec le clustering interactif. In Atelier - Fouille de Textes - Text Mine 2021 - En conjonction avec EGC 2021. <hal-03133060>.`
    - Implementation: `Schild, E. (2021). cognitivefactory/interactive-clustering. Zenodo. https://doi.org/10.5281/zenodo.4775251.`

- **Web application**:
    - _FastAPI_: `https://fastapi.tiangolo.com/`


## <a name="Other links"></a> Other links

- Several comparative studies of Interactive Clustering methodology on NLP datasets: `Schild, E. (2021). cognitivefactory/interactive-clustering-comparative-study. Zenodo. https://doi.org/10.5281/zenodo.5648255`. (GitHub: [cognitivefactory/interactive-clustering-comparative-study](https://github.com/cognitivefactory/interactive-clustering-comparative-study)).

<p align="center">
	<a href="https://github.com/cognitivefactory/interactive-clustering-comparative-study">
		<i style="font-size: smaller; color:grey">Organizational diagram of the different Comparative Studies of Interactive Clustering.</i>
		</br>
		<img src="docs/figures/interactive-clustering-comparative-study.png" alt="Organizational diagram of the different comparative studies of Interactive Clustering." width="75%"/>
	</a>
</p>


## <a name="How to cite"></a> How to cite

`Schild, E. (2021). cognitivefactory/interactive-clustering-gui. Zenodo. https://doi.org/10.5281/zenodo.4775270.`