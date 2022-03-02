# FXT API PYTHON SCRIPT

## Setup Environment
```
$ mkdir project_dir
$ cd project_dir
$ python3 -m venv venv
$ source ./venv/bin/activate
```

Dependencies:
------------
Install Python / Python3
Install pip / pip3

pip install -U pip
pip install notebook pandas requests ciso8601

We'll also want to download the Python FTX API client. You can do that by downloading the raw file from the FTX GitHub Repo or using curl.

curl is a handy *nix command-line utility that allows you to transfer data over various protocols. It stands for "Client URL".

```
curl https://raw.githubusercontent.com/ftexchange/ftx/master/rest/client.py -o client.py
```

## Resources:
  1. [FXT Rest API Tutorial](https://analyzingalpha.com/blog/ftx-rest-api-python#get-all-market-data)
  2. [FXT API Python Tutorial Youtube](https://youtu.be/1PV2tQa9VyI)
  3. [FXT API Documentation](https://docs.ftx.com)