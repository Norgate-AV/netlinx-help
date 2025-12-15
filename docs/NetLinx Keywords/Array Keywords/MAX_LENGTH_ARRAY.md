# MAX_LENGTH_ARRAY

Returns the maximum length of a dimension of an array.

**Syntax:**

```netlinx
LONG MAX_LENGTH_ARRAY (<type> Array[ ])
```

**Parameters:**

- **Array** - a numeric array of any type
- **<type>** - may be any intrinsic or user-defined data type.

**Result:**

- The length of the specified dimension of Array.

**Example:**

```netlinx
FLOAT FPArray[10]
LONG NumArray[5][3][4]
 
Len = MAX_LENGTH_ARRAY(FPArray)        // Len = 10
Len = MAX_LENGTH_ARRAY(NumArray)       // Len = 5
Len = MAX_LENGTH_ARRAY(NumArray[1])    // Len = 3
Len = MAX_LENGTH_ARRAY(NumArray[1][1]) // Len = 4
```

See Also

- [Array Keywords](Array_Keywords.md)
- [LENGTH_ARRAY](LENGTH_ARRAY.md)
- [SET_LENGTH_ARRAY](SET_LENGTH_ARRAY.md)

