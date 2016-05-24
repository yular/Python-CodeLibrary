from pyspark import  SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import HiveContext

sc = SparkContext( 'local', 'pyspark')

sqlContext = HiveContext(sc)
# sqlContext = SQLContext(sc)
sqlContext.sql("use default")
df = sqlContext.sql("select * from test_join_id")
df.registerTempTable("test_tmp")
res = sqlContext.sql("select count(*) from test_tmp").collect()

print res
