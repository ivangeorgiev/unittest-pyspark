"""
To run this example:
   python -m unittest tests.test_sample
"""

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

from unittest_pyspark.unittest import *
execute_test_cases(discover_test_cases())