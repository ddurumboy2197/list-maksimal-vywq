# test_max_number_in_list.py
import pytest
from max_number_in_list import max_number_in_list

def test_max_number_in_list_empty_list():
    assert max_number_in_list([]) == None

def test_max_number_in_list_single_element():
    assert max_number_in_list([5]) == 5

def test_max_number_in_list_multiple_elements():
    assert max_number_in_list([1, 2, 3, 4, 5]) == 5

def test_max_number_in_list_negative_numbers():
    assert max_number_in_list([-1, -2, -3, -4, -5]) == -1

def test_max_number_in_list_zero():
    assert max_number_in_list([0, 1, 2, 3, 4]) == 4

def test_max_number_in_list_duplicates():
    assert max_number_in_list([5, 5, 5, 5, 5]) == 5
```

```javascript
// maxNumberInList.test.js
import { maxNumberInList } from './maxNumberInList';

describe('maxNumberInList', () => {
  it('should return null for empty list', () => {
    expect(maxNumberInList([])).toBeNull();
  });

  it('should return single element for single element list', () => {
    expect(maxNumberInList([5])).toBe(5);
  });

  it('should return max number for multiple elements', () => {
    expect(maxNumberInList([1, 2, 3, 4, 5])).toBe(5);
  });

  it('should return max number for negative numbers', () => {
    expect(maxNumberInList([-1, -2, -3, -4, -5])).toBe(-1);
  });

  it('should return max number for list with zero', () => {
    expect(maxNumberInList([0, 1, 2, 3, 4])).toBe(4);
  });

  it('should return max number for list with duplicates', () => {
    expect(maxNumberInList([5, 5, 5, 5, 5])).toBe(5);
  });
});
