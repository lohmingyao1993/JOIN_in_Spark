# JOIN_in_Spark

## Requirements

* Cloudera VM

## Setup

Open a terminal in the VM.

Clone directly from source code:

```bash
git clone https://github.com/lohmingyao1993/JOIN_in_Spark
```
Move data to hdfs:

```bash
hdfs dfs -put ./JOIN_in_Spark/data/join_gen*.txt /user/cloudera/input
```


### IPython

Install IPython:

```bash
sudo yum install python-ipython
```

Launch pyspark with IPython:

```bash
PYSPARK_DRIVER_PYTHON=ipython pyspark
```
Check verison:

```bash
from pyspark import SparkContext

sc = SparkContext()

sc.version
```
output:

```bash
u'1.3.0'
```

Run python file:

```bash
%run ./JOIN_in_Spark/joinspark.py
```

CTRL+Z to exit IPython

### Result

Result saved in "output" folder:

```bash
hdfs dfs -ls output

hdfs dfs -cat output/*
```

