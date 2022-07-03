# Coding problems discussed with Discovery Team


## 	Deduplicate chars from string
	Remove duplicate chars from a string, keeping the first occurrence of each character.
	
	Solutions 	: [GitHub Page](https://github.com/vikshind/python-samples/blob/master/discovery/RemoveDuplicates.py)
		Solution 1 	: Just iterate through each char and keep track of visited characters using Dict Data-Structure.
		Solution 2 	: Using collections.OrderedDict  <-- simple and quick soln
	
## 	Simulate phone dialing pad
	Convert a number to string using the standard phone keyboard
```	
    1   | 2 abc | 3 def
--------+-------+--------
  4 ghi | 5 jkl | 6 mno
--------+-------+--------
  7 pqrs| 8 tuv | 9 wxyz
--------+-------+--------
        | 0     |

assert phone_string("226222") == "bmc"
```
	Solutions	: Implemented in 2 ways
		Solution 1 : Brute froce method, just implemented simple linear way of parsing string. Used Python Dict, and regx at some places
			[GitHub Page](https://github.com/vikshind/python-samples/blob/master/discovery/PhoneString.py)
			
		Solution 2 : Better approach - Object oriented, considering Phone Dialing Pad as a class having method get_letters()
			Demonstrates good use of REGX. Optimized and performant solution.
			[GitHub Page](https://github.com/vikshind/python-samples/blob/master/discovery/DialingPad.py)

## 	Find Median
	Write a function to find the median of an array
	
	Solutions	: Solved in 2 ways, 
		Solution 1	: Implemented QuickSort to sort an unsorted array and then quickly find out median
						Implemented TESTs using "pytest"
		Soltuoin 2	: We can directly use statistics.median of Python.
	
	[GitHub Page](https://github.com/vikshind/python-samples/blob/master/discovery/FindMedian.py)
	
	
## 	Write a function to add up squares of all the values in an array
	Solutions 	: Again 2 ways 
		Solution 1 : Implemented own function sum_squared(arr) 
		Solution 2 : use pythonic way 1 liner code -> result = sum([num ** 2 for num in arr])
		
	[GitHub Page](https://github.com/vikshind/python-samples/blob/master/discovery/SumSquared.py)
	
		Compared performance of both solutions using different TESTs
