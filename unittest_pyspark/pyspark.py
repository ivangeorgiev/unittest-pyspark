
import pyspark.sql as ps
import pyspark.sql.types as pst
import pyspark

_sc = None

def get_spark(master='local', appName='myAppName', driverHost='127.0.0.1'):
  """Get SparkSession object. Note: Spark context is persisted between calls."""
  global _sc

  if not _sc:
    conf = pyspark.SparkConf().set('spark.driver.host',driverHost)
    _sc = pyspark.SparkContext(master=master, appName=appName,conf=conf)

  spark = pyspark.sql.SparkSession.builder.getOrCreate() 
  return spark


def as_list(input_df, deep=True, **kwargs):
    """Convert Spark DataFrame to list"""
    def row_as_dict(r):
      d = r.asDict()
      if deep:
        for k in d:
          if isinstance(d[k], pst.Row):
            d[k] = row_as_dict(d[k])
      return d
    
    if isinstance(input_df, ps.DataFrame):
        result = [row_as_dict(r) for r in input_df.collect()]
    else:
        result = input_df
    return result

