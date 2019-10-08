# Algorithms


# 1, Range Query

# 2,Number compositions
Write a function **compositions** that takes two natural numbers k and n as inputs and returns the set of all tuples of size k that sum to n. 

<font  style="color:blue"> **Code:**</font>
```python
func_out = compositions(3,4)

print "all possible combinations: "
print_compositions(func_out)
print;print "Actual Output from compositions(3,4)"; func_out
```


<font  style="color:magenta"> **Output**</font>
```
all possible combinations: 
1 + 2 + 1 
2 + 1 + 1 
1 + 1 + 2 

Actual Output from: compositions(3,4)
{(1, 1, 2), (1, 2, 1), (2, 1, 1)}
```
