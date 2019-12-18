import unittest
from unittest_pyspark import as_list, get_spark
import pyspark.sql.types as pst


class Test_as_list(unittest.TestCase):
  def setUp(self):
    self.spark = get_spark()

  def test_as_list_deep(self):
    input = [ pst.Row(id=1, a=pst.Row(b=101)) ]
    input_df = self.spark.createDataFrame(input)

    actual = as_list(input_df, True)
    expect = [{'id':1, 'a':{'b':101}}]

    self.assertEqual(actual, expect)

  def test_as_list_shallow(self):
    input = [ pst.Row(id=1, a=pst.Row(b=101)) ]
    input_df = self.spark.createDataFrame(input)

    actual = as_list(input_df, False)
    expect = [{'id':1, 'a':pst.Row(b=101)}]

    self.assertEqual(actual, expect)    

