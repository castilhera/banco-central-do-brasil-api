import os
import unittest

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    loader = unittest.TestLoader()
    suite = loader.discover(dir_path)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
