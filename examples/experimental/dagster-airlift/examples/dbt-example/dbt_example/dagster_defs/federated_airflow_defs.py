from dagster import Definitions, ScheduleDefinition, AutomationConditionSensorDefinition, DefaultSensorStatus

from dbt_example.dagster_defs.lakehouse import lakehouse_assets_def, lakehouse_existence_check
from dbt_example.shared.load_iris import CSV_PATH, DB_PATH, IRIS_COLUMNS

from .federated_airflow import get_federated_airflow_assets, get_federated_airflow_sensor
from .jaffle_shop import jaffle_shop_with_upstream, jaffle_shop_resource

automation_sensor = AutomationConditionSensorDefinition(
    name="some_name",
    asset_selection="*",
    default_status=DefaultSensorStatus.RUNNING,
    minimum_interval_seconds=1,
)

defs = Definitions(
    assets=[
        lakehouse_assets_def(csv_path=CSV_PATH, duckdb_path=DB_PATH, columns=IRIS_COLUMNS),
        jaffle_shop_with_upstream,
        *get_federated_airflow_assets(),
    ],
    asset_checks=[lakehouse_existence_check(csv_path=CSV_PATH, duckdb_path=DB_PATH)],
    sensors=[get_federated_airflow_sensor(), automation_sensor],
    resources={"dbt": jaffle_shop_resource()},
)
