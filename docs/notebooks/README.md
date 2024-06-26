# How using Jupyter Notebooks for project analysis ?

<details>
	<summary>Tips: Read the Project Jupyter Documentation</summary>
	If needed, see <a href="https://docs.jupyter.org/en/latest/" alt="Project Jupyter Documentation.">https://docs.jupyter.org/en/latest/</a>.
</details>

## 1. Prepare your environment

In your Python environment, install the following libraries (with `pip` or `pipx`):

```
# Needed to launch Jupyter App.
jupyter
jupyterthemes  # optional

# Needed to run Jupyter Notebooks.
plotly>=2.5
pandas
numpy
```

## 2. Set token api (needed for LLM analysis)

To be able to call a model from OpenAI, you need to register and create a token api key on [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys), then store it in a file named `credentials.py` near the notebook.

The content of this file should look like :

```python
OPENAI_API_TOKEN: str = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# 1. Rename this file in `credentials.py`
# 2. Change value of `OPENAI_API_TOKEN` with your own API token from OpenAI (https://platform.openai.com/account/api-keys).
```

## 3. Get project data

In the web application, after several iterations of annotation, download the zip archive of your project and extract it near the jupyter notebook.

> Tips: Examples of projects data are available here : [Examples/Demo projects](../examples/README.md)

## 4. Lauch Jupyter

Run the following command:

```bash
jupyter notebook
```

> Tips: An example of analysis notebook is available here: [Analysis notebook](./analysis.ipynb)
