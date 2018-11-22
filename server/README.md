# Dell Hackathon

> Server Side is built on python ( Flask )

## Get Started

- Creating a virtual environment ( optional )

``` bash
# install miniconda
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source .bashrc

# create a virtual environment and activate it
conda create --name <environment-name> python=3.7
source activate <environment-name>

```

- Installing the important python packages
``` bash
# install flask
pip install flask

# install gunicorn
pip install gunicorn

```

- Running the server
``` bash
# install flask
pip install flask

# install gunicorn
pip install gunicorn

# running the server
gunicorn --bind 0.0.0.0:8000 server:app

```
