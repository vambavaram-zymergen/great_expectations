from airflow.hooks.dbapi_hook import DbApiHook
import great_expectations as ge


class ExpectationMySQLHook(DbApiHook):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_ge_df(self, dataset_name, **kwargs):
        self.log.info("Connecting to dataset {dataset} on {uri}".format(uri=self.get_uri(), dataset=dataset_name))
        sql_context = ge.get_data_context('SqlAlchemy', self.get_uri())

        return sql_context.get_dataset(dataset_name=dataset_name, **kwargs)
