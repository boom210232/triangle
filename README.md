## Testing with Code Coverage

`triangle.py` contains a function `is_triangle(a, b, c)`
that returns True if (a, b, c) are valid lengths of the sides of a triangle, and returns False otherwise.

`triangle_test.py` contains unit tests of is\_triangle.


## Exercise 1: Test Coverage

Use code coverage to find untested code and a problem with the tests.

1. Run the unit tests. They should all pass.
   ```bash
   python3 -m unittest triangle_test.py
   ```

2. Run the tests using code coverage, then generate an html coverage report:
   ```bash
   coverage run -m unittest triangle_test.py
   coverage html
   ```

3. View the report in a web browser. The file to view is `htmlcov/index.html`.

4. Is there any part of the code under test (`triangle.py`) that was not tested?

   Write the Line Numbers here: [    22      ]

5. Modify the tests so that all lines of the code are tested.

6. Run coverage again with the `--branch` option to see if all branches of "if" statements are covered:
   ```bash
   coverage run --branch -m unittest triangle_test.py
   coverage html
   ```

7. What lines in the **unit test code** were not executed?     
   Write the Line Numbers: [       25 , 29 , 33 , 37           ]

8. Normally, **all** the lines of test code should be executed.  When some part of test code is not executed it may indicate a problem with the tests.     
   Explain the problem in the unit test code.

   Your Answer: Because It found case that it should show assert in the line as it need so it doesn't want to check more.






When done, **push your work to Github, including your changes to README**.

## Exercise 2: Parameterized Tests

Use a loop and `self.subTest()` to replace redundant test code with a loop over sets of data values.  

By using `subTest()`, if one test case fails the test will continue to execute the other test cases.  If you simply use a loop without `subTest()`, the test will **stop** after the first failure.

1. **Copy** `triangle_test.py` to `parameterized_test.py`.

2. For **each** of the 3 test methods, create a list of tuples for the test data.  Then replace multiple "assert" statements with a loop (over the test data) that contains **only one** assert statement.
   - you must put the "assert" inside a `self.subTest()` block so that all test cases will be run if an assertion fails.

3. Run the tests with code coverage and verify that the tests work as before.

4. Add `parameterized_test.py` to git and **push** to Github.

Example:
```python
class TriangleTest(unittest.TestCase):
    # The list of data values for your tests can be defined:  
    # - outside the class (global variable)
    # - as a class variable (like this) 
    # - as a local variable inside the test method.
    # Use which ever is most readable.
    valid_triangles = [
            (1, 1, 1),
            (3, 4, 5),
            (3, 4, 6),
            ...
            ]

    def test_valid_triangle(self):
        for a,b,c in self.valid_triangles:
            with self.subTest():
                message = f"sides are ({a},{b},{c})"
                self.assertTrue( is_triangle(a, b, c), message)
```
In the assertTrue statement we include a string message (2nd parameter) so
that if a test fails we can see the values of a, b, c that were used.

If we do not add the string message, the output of a failed test will 
only show `assertTrue(is_triangle(a,b,c)) was False`,
without showing that actual values of a, b, c. 
This is a problem in using variables as test arguments.


### Install Coverage Package

On most systems you install it using "pip" or "pip3": 
```bash
pip3 install coverage`
```

For more info, see the [Coverage Documentation](https://coverage.readthedocs.io/en/coverage-5.5/).

### Learn about subTest

[Subtests](https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests) in the Python documentation.  Has examples.

[Subtest example on StackOverflow](https://stackoverflow.com/questions/32899/how-do-you-generate-dynamic-parameterized-unit-tests-in-python)
