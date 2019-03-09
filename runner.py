import unittest
from account import account
from test_instructor import TestInstructor
def main():
    """Runs the unit tests"""

    suite = unittest.TestSuite()

    suite.addTests(unittest.makeSuite(TestInstructor))

    result = unittest.TextTestRunner(verbosity=1).run(suite)

    n_errors = len(result.errors)
    n_failures = len(result.failures)

    if n_errors or n_failures:
        print('\n\nSummary: %d errors and %d failures reported\n'
            (n_errors, n_failures))

    print()

main()