# Packaging Python Scripts into CLI Commands

### Running the script
First, create the ```setup.py```, ```caesar\__init__.py```, and ```caesar\caesar.py``` files, then run 
```bash
python3 setup.py install
```

This will install the dependencies required for you to run commands directly from the command line interface using
```bash
caesar "Whatever text you want"
```

### Source
* This was taken from the Medium [article](https://medium.com/ediblesec/turning-python-scripts-into-cli-commands-aecf56dfda18) written by Chris Doucette titled <strong>Packaging Python Scripts into CLI Commands</strong>.
