## Feature Scaling

**Feature scaling** is a method used to normalize the range of independent variables or features of data. In [data processing](https://en.m.wikipedia.org/wiki/Data_processing "Data processing"), it is also known as data normalization and is generally performed during the data preprocessing step.

Reasons for including Feature Scaling

 - Since the range of values of raw data varies widely, in some [machine learning](https://en.m.wikipedia.org/wiki/Machine_learning "Machine learning") algorithms, objective functions will not work properly without [normalization](https://en.m.wikipedia.org/wiki/Normalization_(statistics) "Normalization (statistics)"). For example, many [classifiers](https://en.m.wikipedia.org/wiki/Statistical_classification "Statistical classification") calculate the distance between two points by the [Euclidean distance](https://en.m.wikipedia.org/wiki/Euclidean_distance "Euclidean distance"). If one of the features has a broad range of values, the distance will be governed by this particular feature. Therefore, the range of all features should be normalized so that each feature contributes approximately proportionately to the final distance.
 - Another reason why feature scaling is applied is that  [gradient descent](https://en.m.wikipedia.org/wiki/Gradient_descent "Gradient descent")  converges much faster with feature scaling than without it.

## Methods
Rescaling (min-max normalization)

Also known as min-max scaling or min-max normalization, is the simplest method and consists in rescaling the range of features to scale the range in [0, 1] or [−1, 1]. Selecting the target range depends on the nature of the data. The general formula for a min-max of [0, 1] is given as:
$x' = \frac{x-min(x)}{max(x)-min(x)}$
where  $x$ is an original value,  $x'$  is the normalized value. For example, suppose that we have the students' weight data, and the students' weights span [160 pounds, 200 pounds]. To rescale this data, we first subtract 160 from each student's weight and divide the result by 40 (the difference between the maximum and minimum weights).

To rescale a range between an arbitrary set of values [a, b], the formula becomes:
$x' = a + \frac{(x-min(x))(b-a)} {max(x) - min(x)}$
where  $a,b$  are the min-max values.

### Mean normalization

$x' = \frac{x-average(x)}{max(x) - min(x)}$
where  $x$ is an original value,  $x'$ is the normalized value. There is another form of the mean normalization which is when we divide by the standard deviation which is also called standardization.

### Standardization (Z-score Normalization)

In machine learning, we can handle various types of data, e.g. audio signals and pixel values for image data, and this data can include multiple  [dimensions](https://en.m.wikipedia.org/wiki/Dimensions "Dimensions"). Feature standardization makes the values of each feature in the data have zero-mean (when subtracting the mean in the numerator) and unit-variance. This method is widely used for normalization in many machine learning algorithms e.g.,  support vector machines, Logistic regression and Artificial neural network. The general method of calculation is to determine the distribution  mean and  standard deviation for each feature. Next we subtract the mean from each feature. Then we divide the values (mean is already subtracted) of each feature by its standard deviation.

$x' = \frac{x-\bar{x}}{\sigma}$
Where  symbols have usual meanings.

### Scaling to unit length

Another option that is widely used in machine-learning is to scale the components of a feature vector such that the complete vector has length one. This usually means dividing each component by the  [Euclidean length](https://en.m.wikipedia.org/wiki/Euclidean_length "Euclidean length")  of the vector:

$x'=\frac{x}{\text{\textbardbl}{x}\text{\textbardbl}}$  

In some applications (e.g. Histogram features) it can be more practical to use the L1 norm (i.e. Manhattan Distance, City-Block Length or  [Taxicab Geometry](https://en.m.wikipedia.org/wiki/Taxicab_Geometry "Taxicab Geometry")) of the feature vector. This is especially important if in the following learning steps the Scalar Metric is used as a distance measure.

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY0NTY0NzU5NiwtMTQ2ODA1ODE4NywxOT
Q0MDAxMDc5XX0=
-->