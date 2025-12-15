---
title: SET_LENGTH_ARRAY
---

# SET_LENGTH_ARRAY

Sets the effective length of a dimension of an array.

**Syntax:**

```netlinx
SET_LENGTH_ARRAY (<type> Array[ ], LONG Len)
```

**Parameters:**

- **<type>** - may be any intrinsic or user-defined data type.
- **Array** - array of any type.
- **Len** - value to assign as the length.

**Returns:**  
None

**Example:**

```netlinx
SET_LENGTH_ARRAY(NumArray, 5)
```

See Also

- [MAX_LENGTH_ARRAY](MAX_LENGTH_ARRAY.md)
- [LENGTH_ARRAY](LENGTH_ARRAY.md)
- [SET Keywords](SET_Keywords.md)
- [Array Keywords](Array_Keywords.md)

