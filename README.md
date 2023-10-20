# Showcase site - Flask

## Setting up

### Venv

```bash
# create a venv

python3 -m venv "nameofyourvenv"

# activate a venv

source myenv/bin/activate
```

### Requirements

```bash
pip install -r requirements.txt

if you are on Debian, you may need to do this installation :
sudo apt-get install libpq-dev
```

## Launching the project


```bash
export FLASK_APP=app
export FLASK_DEBUG=true

flask run
```

