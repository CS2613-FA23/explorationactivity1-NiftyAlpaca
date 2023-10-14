# NumPy Package Overview
### Colton A.G. Coughlin

## Introduction
In this exploration activity, we investigate NumPy. An open source numerical computing Python module that provides a multidimensional array data type and a variety of functions that allow a developer to manipulate arrays on the fly.

I chose this module for my activity because of my curiousity of NumPy's special data type ndarray, which is an array data type that comes with functions that can do operations on every element at once. God knows every programmer gets a little sick of iterating through an array at some point. What got me really interested in NumPy was after watching the Youtube video "Learn NUMPY in 5 minutes - BEST Python Library!" by Python Programmer [\[ref\]](https://www.youtube.com/watch?v=xECXZ3tyONo&t=503s) who demonstrates the use of NumPY along with other modules by altering images, hence the inspiration for my demo. 

After creating a program using NumPy, this report will describe NumPy and my experience with the module and how it affected my relationship with coding as a whole.


## NumPy


### Aspirations
"NumPy is an open source project that enables numerical computing with Python. It was created in 2005 building on the early work of the Numeric and Numarray librariees. NumPy will always be 100% open source software and free for all to use" [\[ref\]](https://numpy.org/about/)

The goal of this open source project is simple. Make programming in Python easier for developers. NumPy created a simple solution to a big problem, but it didn't come flawless. "A list is a very useful tool offered by Python, as it lets you store values of different types at once, and perform numerous operations on it. But it has certain limitations, and some operations on list are not efficient," says Shubhanker Singh at towardsdatascience.com when reviewing the package[\[ref\]](https://towardsdatascience.com/a-quick-review-of-numpy-and-matplotlib-48f455db383)

### Code Example of multiplying two nd arrays

#### Source

```python
import numpy as np

x = [10,20,45,50,100]
y = [37,45,34,35,64]

np_x = np.array(x)
np_y = np.array(y)

summation = np_x * np_y
print(summation)
type(summation)
```
#### Output

```python
[ 370  900 1530 1750 6400]
<class 'numpy.ndarray'>
```


With Python alone, we would have had to iterate through both arrays, do the operation multiplication, and return to a newly created list. On a small scale, not a big deal but imagine large scale. "There is no limit to the numbers of rows and columns a matrix (in the usual sense) can have as long as they are positive integers.," says Wikipedia. [\[ref\]](https://en.wikipedia.org/wiki/Matrix_(mathematics)). Mathematicians are happy with it. More math, less time! "NumPy (or Numeric Python) sits at the core of every data science and machine learning project" [\[ref\]].


## Reflection

There are two takeaways I got from this activity in terms of learning Python. The first was learning slicing, which is described by the website SparkByExamples as "used for selecting a range of items from a sequence such as a list, tuple, or string." [\[ref\]](https://sparkbyexamples.com/python/python-slice-notation-explain/). Slicing is the first time I have witnessed a way of getting elements of an array outside of the classic form of indexing with a for-loop (arr[i]). Although I am still very new to this way of iteration, I look forward to trying it in other projects.

I have imported modules before in Python but this is the first time that I not only imported multiple modules, but it was also the first time I had issues that made me have to debug. It is always an interesting experience trying to debug your code and understand what issue another person's code has with your own. Or even what other's peoples code conflict with yet another person's code.

## Conclusion

When I first looked at NumPy, I was a little intimidated. There was talked of matrices and complex math and I was worried for myself. Although it is intended mostly for those purposes, the value of the ndarray data type is high for any programmer from junior to senior. Ndarrays were an unexpected discovery but it is one I will keep in my pocket from now on, especially in situations where I need to mass manipulate my arrays. Step aside for-loop.



