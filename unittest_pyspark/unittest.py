
import inspect, unittest

def discover_test_cases():
  """Discover unittest Test Cases defined in the global scope.
  
  Returns a list of unittest.TestCase objects."""
  def is_test_case(obj):
    if not inspect.isclass(obj):
      return False
    if not issubclass(obj, unittest.TestCase):
      return False
    if not obj.__name__.lower().find('test_') == 0:
      return False
    return True
  
  g = globals()
  result = set()
  for name in g.keys():
    obj = g[name]
    if not is_test_case(obj):
      continue
    result.add(obj)
  return result

def execute_test_cases(test_cases):
  """Execute a list of test cases."""
  loader = unittest.TestLoader()
  suite = unittest.TestSuite()
  for t in test_cases:
    suite.addTests(loader.loadTestsFromTestCase(t))
  runner = unittest.TextTestRunner()
  runner.run(suite)
