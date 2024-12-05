# venv
```sh
python3 -m venv env
. env/bin/activate

pip3 install apache-airflow
```

# Apache Airflow
```sh
export AIRFLOW_HOME

export AIRFLOW_HOME=./airflow
echo $AIRFLOW_HOME

airflow db init
airflow webserver --port 8080
airflow scheduler


cp my_first_dag.py $AIRFLOW_HOME/dags
airflow dags list
airflow dags list|grep 'my-frist-dag'
airflow tasks list my-first-dag

```

```
 curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz -o data/tolldata.tgz
```