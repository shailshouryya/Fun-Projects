# Packaging Python Scripts into CLI Commands

### Running the script
First, create the ```bash setup.py```, ```bash caesar\__init__.py```, and ```bash caesar\caesar.py``` files, then run 
```bash
python3 setup.py install
```

This will install the dependencies required for you to run commands directly from the command line interface using
```bash
caesar "Whatever text you want"
```

### Source
* This was taken from the Medium [article](https://medium.com/employbl/scrape-the-web-for-amsterdam-coffeeshops-with-python-and-beautiful-soup-19ed25394234) written by Chris Doucette titled <strong>Packaging Python Scripts into CLI Commands</strong>.
