from datetime import timedelta
from airflow.models import DAG
#from airflow.operators.bash_operator import BashOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
#from airflow.utils.dates import days_ago

import pendulum

default_args = {
    'owner': 'Cooper Anderson',
    #'start_date': days_ago(0),
    'start_date': pendulum.today('UTC').add(days=-1),
    'email': ['ca@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule=timedelta(days=1),
)

INPUT='/home/project/airflow/dags/finalassignment/tolldata.tgz'
DEST='/home/project/airflow/dags/finalassignment/staging'

unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command="tar -xvzf $INPUT -C $DEST" ,
    dag=dag,
)

def extract_vehicle():
    input_file=f"{DEST}/vehicle-data.csv"
    output_file=f"{DEST}/csv_data.csv"
    print("Inside Extract vehicle")
    # Read the contents of the file into a string
    with open(input_file, 'r') as infile_vehicle, \
            open(output_file, 'w') as outfile:
        for line in infile_vehicle:
            fields = line.split(',')
            if len(fields) >= 6:
                field_1 = fields[0].strip()
                field_2 = fields[1].strip()
                field_3 = fields[2].strip()
                field_4 = fields[3].strip()
                outfile.write(field_1 + "," + field_2 + "," + field_3 + "," + field_4 + "\n")

extract_data_from_csv = PythonOperator(
    task_id='extract_data_from_csv',
    python_callable=extract_vehicle,
    dag=dag,
)

def extract_tollplaza():
    input_file=f"{DEST}/tollplaza-data.tsv"
    output_file=f"{DEST}/tsv_data.csv"
    print("Inside Extract tollplaza")
    # Read the contents of the file into a string
    with open(input_file, 'r') as infile, \
            open(output_file, 'w') as outfile:
        for line in infile:
            fields = line.split('\t')
            if len(fields) >= 6:
                field_1 = fields[4].strip()
                field_2 = fields[5].strip()
                field_3 = fields[6].strip()
                outfile.write(field_1 + "," + field_2 + "," + field_3 + "\n")

extract_data_from_tsv = PythonOperator(
    task_id='extract_data_from_tsv',
    python_callable=extract_tollplaza,
    dag=dag,
)


def extract_wixed_width():
    input_file=f"{DEST}/payment-data.txt"
    output_file=f"{DEST}/fixed_width_data.csv"
    with open(input_file, mode='r') as infile:
        with open(output_file, mode='w', newline='') as outfile:
            index=0
            for line in infile:
                id = line[0:6].strip()
                ts=line[7:31].strip()
                anonymized=line[32:39].strip()
                # tollplaza id
                tid=line[40:47].strip()
                # toll plaza code
                tpc=line[48:57].strip()
                # type of payment
                tp=line[58:61].strip()
                # vehicle code            
                vc=line[62:67].strip()
                
                outfile.write(f"{tp}, {vc}\n")

extract_data_from_fixed_width = PythonOperator(
    task_id='extract_data_from_fixed_width',
    python_callable=extract_wixed_width,
    dag=dag,
)

consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command=f"paste -d ',' {DEST}/csv_data.csv {DEST}/tsv_data.csv {DEST}/fixed_width_data.csv > {DEST}/extracted_data.csv",
    dag=dag,
)

transform_data = BashOperator(
    task_id='transform_data',
    bash_command=f"tr '[:lower:]' '[:upper:]' < {DEST}/extracted_data.csv > {DEST}/transformed_data.csv",
    dag=dag,
)

# task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data


#extract_vehicle()
#extract_tollplaza()
#extract_wixed_width()