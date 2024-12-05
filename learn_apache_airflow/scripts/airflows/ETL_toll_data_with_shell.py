from datetime import timedelta
from airflow.models import DAG
#from airflow.operators.bash_operator import BashOperator
from airflow.operators.bash import BashOperator
#from airflow.utils.dates import days_ago
import pendulum

default_args = {
    'owner': 'your_name',
    #'start_date': days_ago(0),
    'start_date': pendulum.today('UTC').add(days=-1),
    'email': ['youremail@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG

# define the DAG
dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='My Toll DAG',
    schedule=timedelta(days=1),
)

INPUT='airflow/dags/finalassignment/tolldata.tgz'
DEST='airflow/dags/finalassignment/staging'

def exec_unzip_data():
    return f"tar -xvzf {INPUT} -C {DEST}" 

unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command=exec_unzip_data(),
    dag=dag,
)

def exec_extract_data_from_csv():
    return f"cut -d',' -f1,2,3,4 {DEST}/vehicle-data.csv > {DEST}/csv_data.csv"

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command=exec_extract_data_from_csv(),
    dag=dag,
)

def exec_extract_data_from_tsv():
    return f"cut -d'\t' -f5,6,7 {DEST}/tollplaza-data.tsv | tr '\t' ',' | tr -d '\r' > {DEST}/tsv_data.csv"

extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command=exec_extract_data_from_tsv(),
    dag=dag,
)

def exec_extract_data_from_fixed_width():
    #return f"cut -c 59-61,62-67 {DEST}/payment-data.txt|sed 's/ /,/g' > {DEST}/fixed_width_data.csv"
    #return f"rev {DEST}/payment-data.txt| cut -d' ' -f 1,2|rev|sed 's/ /,/g' > {DEST}/fixed_width_data.csv"
    return f"awk '{{print $(NF-1) \",\" $NF}}' {DEST}/payment-data.txt > {DEST}/fixed_width_data.csv"



extract_data_from_fixed_width  = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command=exec_extract_data_from_fixed_width(),
    dag=dag,
)

def exec_consolidate_data():
    return f"paste -d ',' {DEST}/csv_data.csv {DEST}/tsv_data.csv {DEST}/fixed_width_data.csv > {DEST}/extracted_data.csv"

consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command=exec_consolidate_data(),
    dag=dag,
)

def exec_transform_data():
    return f"awk -F, '{{ $4=toupper($4); print $0 }}' OFS=, {DEST}/extracted_data.csv > {DEST}/transformed_data.csv"

transform_data = BashOperator(
    task_id='transform_data',
    bash_command=exec_transform_data(),
    dag=dag,
)

# Pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data

### Testing Locally

#import os
#os.system(exec_unzip_data())
# os.system(exec_extract_data_from_csv())
# os.system(exec_extract_data_from_tsv())
# os.system(exec_extract_data_from_fixed_width())
# os.system(exec_consolidate_data())
# os.system(exec_transform_data())