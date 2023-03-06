
# Google Search CLI 

This is a simple Python script that opens Google with search parameters entered as command line arguments. The script takes a search query as input and constructs a Google search URL using the query.


## Usage/Examples

```bash
  google how to center a div
```
Will open webbrowser and google for "how to center a div"


## Install

Clone the project

```bash
  git clone https://link-to-project
```


To use this script, you must create an alias in your shell's configuration file (e.g. .bashrc, .zshrc).

```bash
  nano -w ~/.bashrc
```

add an alias (insert right path and filename)

```bash
  alias google="python3 PATH/gs-cli.py"
```

