```shell
python3 -m venv env
source env/Scripts/activate
```

-m: This flag tells Python to run a module as a script. Here, it's used to run the venv module.

venv: This is the module that comes with Python's standard library, used to create lightweight, isolated Python environments.

env: This is the name of the directory where the virtual environment will be created. You can name this whatever you want, but it's common to use names like env, venv, or .venv to indicate that this directory is a virtual environment.


```shell
$ pip list
Package Version
------- -------
pip     24.2
(env)

```

https://pypi.org/project/yfinance/
https://github.com/ranaroussi/yfinance


```shell
$pip install yfinance --upgrade --no-cache-dir
```