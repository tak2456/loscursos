# virtual env

```python
$ mkdir projectA
$ cd projectA
$ python3 -m venv env
$ . env/Scripts/activate

$ pip list
Package Version
------- -------
pip     24.3.1
(env)

pip install pytest
pip install ipykernel
pip install panda
pip intall numpy
pip install matplotlib
pip install beautifulsoup4
pip install randomuser

or 

pip freeze > requirements.txt 
pip install -r requirements.txt

# to upgrade PIP
python.exe -m pip install --upgrade pip

# to run interactively

#%%

then, shift + enter
...
```

https://code.visualstudio.com/docs/datascience/jupyter-notebooks
[Open Public APis](https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/)

![alt text](image.png)

dot product
![alt text](image-1.png)

```python
x = np.linspace(0, 2*np.pi, num=100)
y=np.sin(x)
plt.plot(x,y)
```
![alt text](image-2.png)

![alt text](image-3.png)


# webscraping with requests
![alt text](image-5.png)
![alt text](image-4.png)