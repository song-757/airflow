from airflow.sdk import DAG
import datetime
import pendulum
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["song", "song"],
) as dag:
    t1_orange = BashOperator(
        task_id ="t1_orange",
        bash_command="/opt/airflow/plugins/shell/test_fruit.sh ORANGE"
    )

    t12orange = BashOperator(
        task_id ="t2_orange",
        bash_command="/opt/airflow/plugins/shell/test_fruit.sh AVOCADO"
    )