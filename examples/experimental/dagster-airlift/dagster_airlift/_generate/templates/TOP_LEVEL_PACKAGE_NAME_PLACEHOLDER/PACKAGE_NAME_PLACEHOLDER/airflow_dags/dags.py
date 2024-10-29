# Define the default arguments for the DAG
import os
from datetime import timedelta
from pathlib import Path

from airflow import DAG
from airflow.operators.bash import BashOperator
from dagster._time import get_current_datetime_midnight
from dagster_airlift.in_airflow import proxying_to_dagster
from dagster_airlift.in_airflow.proxied_state import load_proxied_state_from_yaml
from ..shared.constants import CUSTOMERS_CSV_PATH, WAREHOUSE_PATH

from .csv_operators import ExportDuckDBToCSV, LoadCSVToDuckDB, LoadCsvToDuckDbArgs

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": get_current_datetime_midnight(),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}
DBT_DIR = os.getenv("TUTORIAL_DBT_PROJECT_DIR")
# Create the DAG with the specified schedule interval
dag = DAG(
    "rebuild_customers_list",
    default_args=default_args,
    schedule="@daily",
    is_paused_upon_creation=False,
)

# start_load
load_raw_customers = LoadCSVToDuckDB(
    task_id="load_raw_customers",
    dag=dag,
    loader_args=LoadCsvToDuckDbArgs(
        table_name="raw_customers",
        csv_path=CUSTOMERS_CSV_PATH,
        duckdb_path=WAREHOUSE_PATH,
        names=[
            "id",
            "first_name",
            "last_name",
        ],
        duckdb_schema="raw_data",
        duckdb_database_name="jaffle_shop",
    ),
)
# end_load


args = f"--project-dir {DBT_DIR} --profiles-dir {DBT_DIR}"
run_dbt_model = BashOperator(task_id="build_dbt_models", bash_command=f"dbt build {args}", dag=dag)

export_customers = ExportDuckDBToCSV(
    task_id="export_customers",
    dag=dag,
    duckdb_path=WAREHOUSE_PATH,
    duckdb_database_name="jaffle_shop",
    table_name="customers",
    csv_path=CUSTOMERS_CSV_PATH,
)

load_raw_customers >> run_dbt_model >> export_customers  # type: ignore

# Set this to True to begin the proxying process
PROXYING = False

if PROXYING:
    proxying_to_dagster(
        global_vars=globals(),
        proxied_state=load_proxied_state_from_yaml(Path(__file__).parent / "proxied_state"),
    )
