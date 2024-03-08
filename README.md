# streamlit_alpine

Template for creating a [Streamlit custom component](https://docs.streamlit.io/library/components) with [Alpine.js](https://alpinejs.dev/).

![Screenshot](/screenshot.png)

## Developing

### 1) Install streamlit in a local Python environment : [https://docs.streamlit.io/get-started/installation](https://docs.streamlit.io/get-started/installation)

Create a virtual environment
```
python3 -m venv ./venv
```

Activate the virtual environment (Linux/Mac)

```
source ./venv/bin/activate
```

Activate the virtual environment (Windows)

```
.\venv\Scripts\activate.ps1
```

Install Streamlit

```
pip install streamlit
```

### 2) Start the example app with:

```
streamlit run example.py
```

### 3) Make edits to streamlit_alpine/index.html

Note that you will need to refresh your browser each time you make a change to index.html.

You can setup live reload by using [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) in VSCode.  See the note on line 7 of streamlit_alpine/\_\_init\_\_.py on how to use it.
