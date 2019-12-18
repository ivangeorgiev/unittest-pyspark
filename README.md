# unittest-pyspark
Extensions for testing pyspark with unittest and doctest.

These utils can be used in standalone Python or in Databricks
notebooks.

## Usage With Doctest

```python
from unittest_pyspark import get_spark
spark = get_spark()

def go_spark():
    """
    >>> spark.sql("SELECT 'hello world'").show()
    +-----------+
    |hello world|
    +-----------+
    |hello world|
    +-----------+
    <BLANKLINE>
    >>> spark.createDataFrame([{'hello':'world'}], 'hello:string').show()
    +-----+
    |hello|
    +-----+
    |world|
    +-----+
    <BLANKLINE>
    """
    pass

import doctest
doctest.testmod()
```

## Usage With Unittest

Here is a simple `unittest` test case, which can be used as
template for pySpark test case. 

```python
import unittest
from unittest_pyspark import as_list, get_spark
import pyspark.sql.types as pst

class Test_Spark(unittest.TestCase):
  def setUp(self):
      self.spark = get_spark()

  def test_i_can_fly(self):
    input = [ pst.Row(a=1, b=2)]
    input_df = self.spark.createDataFrame(input)
    
    expect = [{'a':1}]
    
    actual_df = input_df.select("a")
    actual = as_list(actual_df)
    
    self.assertEqual(actual, expect)
```

You can find this entire example in the 
`tests.test_sample` module. To execute it from the command line:

```bash
python -m unittest tests.test_sample
```

## Usage With Unittest and Databricks

To execute the `unittest` test cases in Databricks, add following cell:

```python
from unittest_pyspark.unittest import *
if __name__ == "__main__":
  execute_test_cases(discover_test_cases())
```

Above code will automatically discover all test cases (unittest.TestCase
sub classes) defined in the global scope and execute them.

## Build package

You will need `setuptools` and `twine`:
```bash
pip install --upgrade setuptools
pip install --upgrade wheel
```
Build and upload:
```bash
python setup.py sdist bdist_wheel
python -m twine upload dist/*
```