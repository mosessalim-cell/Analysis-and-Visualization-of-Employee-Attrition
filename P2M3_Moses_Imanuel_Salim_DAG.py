import psycopg2
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import datetime as dt
from datetime import timedelta
from elasticsearch import Elasticsearch
from elasticsearch import helpers

def extractPostgre():
    
    '''
    Function ini adalah function untuk DAG yang akan digunakan untuk mengambil data dari postgre. User dan password sama seperti yang telah diconfigurasi di .yaml. 
    Untuk host dan port karena akan dijalankan dalam airflow maka host adalah postgres dengan port 5432.
    Jika ingin dijalankan di local host maka host adalah localhost dengan port 5434
    '''
    db_user = "airflow"
    db_password = "airflow"
    db_host = "postgres"
    db_port = "5432" 
    db_name = "airflow"

    connection = psycopg2.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
        database=db_name
    )

    df = pd.read_sql("SELECT * FROM table_m3", connection)
    df.to_csv('/opt/airflow/dags/P2M3_Moses_Imanuel_data_raw.csv', index=False)
    print("Extract success")

def clean_data(df):
    
    '''
    Function ini digunakan untuk membersihkan datasetnya
    Cleaning yang dilakukan adalah
    1. drop duplikat
    2. Mengubah nama kolom menjadi huruf kecil semua, menghilangkan spasi pada depan dan belakang nama kolom, dan menggantikan spasi menjadi underscore
    3. Menghandle missing value
    4. Menghapus spasi di depan dan belakang untuk value pada kolom kategorikal

    parameter:
    df: dataframe yang ingin diclean

    return:
    df_clean

    contoh penggunaan:
    df_clean = clean_data(df)
    '''

    df_clean = df.copy()

    df_clean = df_clean.drop_duplicates()

    def clean_column_name(col):
        col = col.strip()
        col = col.lower()
        col = col.replace(" ", "_") 
        return col

    df_clean.columns = [clean_column_name(col) for col in df_clean.columns]

    num_cols = df_clean.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = df_clean.select_dtypes(include=['object']).columns

    for col in num_cols:
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())

    for col in cat_cols:
        df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])

    for col in cat_cols:
        df_clean[col] = df_clean[col].str.strip()

    return df_clean

def cleanData():
    
    '''
    Function ini adalah function DAG untuk data cleaning. Function ini hanya akan mengambil data yang raw lalu memanggil function data cleaning sebelumnya.
    Data yang sudah dicleaning akan di save menjadi data_clean
    '''
    df = pd.read_csv('/opt/airflow/dags/P2M3_Moses_Imanuel_data_raw.csv')
    df_clean = clean_data(df)
    df_clean.to_csv('/opt/airflow/dags/P2M3_Moses_Imanuel_data_clean.csv', index=False)
    print('saved to data_clean.csv')

def ingestion_elasticsearch():
    
    '''
    Function ini adalah function DG untuk memasukan data yang sudah dicleaning kedalam elasticsearch.
    Digunakan bulk indexing dari elasticsearch helper untuk memasukan data yang banyak.
    '''
    df = pd.read_csv('/opt/airflow/dags/P2M3_Moses_Imanuel_data_clean.csv')

    es = Elasticsearch("http://elasticsearch:9200")

    actions = [
        {
            "_index": "users",
            "_source": row.to_dict()
        }
        for _, row in df.iterrows()
    ]

    response = helpers.bulk(es, actions)
    print(response)

default_args = {
    'owner': 'Moses',
    'start_date': dt.datetime(2024, 11, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
}

with DAG(
    'P2M3_Moses_Imanuel_DAG',
    default_args=default_args,
    schedule_interval="10-30/10 9 * * 6",
    catchup=False
) as dag:
    extract_postgre = PythonOperator(task_id = 'extract',
                                     python_callable = extractPostgre)
    clean_dat = PythonOperator(task_id = 'cleaning',
                                     python_callable = cleanData)
    load = PythonOperator(task_id='load_elasticsearch',
                        python_callable=ingestion_elasticsearch)

extract_postgre >> clean_dat >> load