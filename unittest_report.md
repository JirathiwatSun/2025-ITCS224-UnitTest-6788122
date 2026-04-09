# Unit Test Report: unittest Module Testing

## Commands Executed

### Command 1: `unittest.TestCase().assertEqual(abs(10), 10)`
**Result:** ✓ No assertion error - test passed!

**Explanation:** This statement asserts that `abs(10)` equals `10`. Since the absolute value of 10 is indeed 10, the assertion is **true** and the test passes silently without raising an error.

---

### Command 2: `unittest.TestCase().assertEqual(abs(-10), 10)`
**Result:** ✓ No assertion error - test passed!

**Explanation:** This statement asserts that `abs(-10)` equals `10`. Since the absolute value of -10 is 10, the assertion is **true** and the test passes silently without raising an error.

---

### Command 3: `unittest.TestCase().assertEqual(abs(10), -10)`
**Result:** ✗ AssertionError - `10 != -10`

**Explanation:** This statement asserts that `abs(10)` equals `-10`. Since the absolute value of 10 is 10 (not -10), the assertion is **false** and raises an `AssertionError` with the message `10 != -10`.

---

## How did you fix the error?

To fix command 3 and eliminate the `AssertionError`, change the expected value from `-10` to `10`:

**Original (causes error):**
```python
unittest.TestCase().assertEqual(abs(10), -10)  # ✗ AssertionError: 10 != -10
```

**Fixed (no error):**
```python
unittest.TestCase().assertEqual(abs(10), 10)   # ✓ No error
```

**Explanation of the fix:** 
- `abs(10)` returns `10` (the absolute value of 10 is 10)
- The second parameter is the expected value
- Since the actual value (10) and expected value (10) now match, the assertion passes with no error

**Alternative fix:**
You could also change the input value instead:
```python
unittest.TestCase().assertEqual(abs(-10), 10)  # ✓ No error (abs(-10) = 10)
```

The key principle is: **`assertEqual()` passes when both values are equal, and raises an `AssertionError` when they don't match.**

---

## Additional unittest Assertions

### Command 4: `unittest.TestCase().assertNotEqual(5, 10)`
**Result:** ✓ No assertion error - test passed!

**Explanation:** This statement asserts that `5` is **not equal** to `10`. Since 5 and 10 are indeed different values, the assertion is **true** and the test passes. `assertNotEqual()` verifies that two values are different.

---

### Command 5: `unittest.TestCase().assertTrue(3 < 5)`
**Result:** ✓ No assertion error - test passed!

**Explanation:** This statement asserts that `3 < 5` is **True**. Since the comparison `3 < 5` evaluates to `True`, the assertion is **true** and the test passes. `assertTrue()` verifies that a condition/expression is True.

---

### Command 6: `unittest.TestCase().assertFalse(5 < 3)`
**Result:** ✓ No assertion error - test passed!

**Explanation:** This statement asserts that `5 < 3` is **False**. Since the comparison `5 < 3` evaluates to `False`, the assertion is **true** and the test passes. `assertFalse()` verifies that a condition/expression is False.

---

### Command 7: `assertIsNot(a, b)` where `a = [1, 2, 3]` and `b = [1, 2, 3]`
**Result:** ✓ No assertion error - test passed!

**Explanation:** This statement asserts that `a` is **not** the same object as `b`. Although both lists have identical contents `[1, 2, 3]`, they are two different objects in memory (different identity). `assertIsNot()` checks object identity (using `is not`), not value equality. The test passes because `a` and `b` are indeed different objects.

---

### Command 8: `unittest.TestCase().assertIn(5, [1, 2, 3])`
**Result:** ✗ AssertionError - `5 not found in [1, 2, 3]`

**Explanation:** This statement asserts that `5` is **in** the list `[1, 2, 3]`. Since 5 does not exist in the list, the assertion is **false** and raises an `AssertionError`. `assertIn()` verifies that a value exists within a collection (list, tuple, string, etc.).

---

## How did you fix the error?

To fix Command 8 and eliminate the `AssertionError`, you need to use a value that **actually exists in the list**:

**Original (causes error):**
```python
unittest.TestCase().assertIn(5, [1, 2, 3])  # ✗ AssertionError: 5 not found in [1, 2, 3]
```

**Fixed Options:**
```python
unittest.TestCase().assertIn(1, [1, 2, 3])  # ✓ No error (1 is in the list)
unittest.TestCase().assertIn(2, [1, 2, 3])  # ✓ No error (2 is in the list)
unittest.TestCase().assertIn(3, [1, 2, 3])  # ✓ No error (3 is in the list)
```

**Explanation of the fix:** 
- The `assertIn()` method checks if a value exists in a collection
- The list `[1, 2, 3]` contains only the values 1, 2, and 3
- Since 5 is not in the list, the assertion fails
- By changing 5 to 1, 2, or 3 (values that exist in the list), the assertion passes

**Alternative fix** (change the list instead):
```python
unittest.TestCase().assertIn(5, [1, 2, 3, 4, 5])  # ✓ No error (5 is now in the list)
```

---

## Key Takeaway

The `unittest.TestCase()` class provides multiple assertion methods for different validation scenarios:
- **`assertEqual(a, b)`** - Passes if a equals b
- **`assertNotEqual(a, b)`** - Passes if a does not equal b
- **`assertTrue(x)`** - Passes if x is True
- **`assertFalse(x)`** - Passes if x is False
- **`assertIsNot(a, b)`** - Passes if a and b are different objects (different identity)
- **`assertIn(x, collection)`** - Passes if x exists in the collection

All assertions raise `AssertionError` when the condition fails, which is the expected behavior for detecting test failures.
