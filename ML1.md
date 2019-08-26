OneHotEncoder: fit() and transform() vs fit_transform()

To [center the data](https://en.wikipedia.org/wiki/Standard_score) (make it have zero mean and unit standard error), you subtract the mean and then divide the result by the standard deviation.

$x'=(x−μ)/σ$

You do that on the training set of data. But then you have to apply the same transformation to your testing set (e.g. in cross-validation), or to newly obtained examples before forecast. But you have to use the same two parameters μ and σ (values) that you used for centering the training set.

Hence, every sklearn's transform's fit() just calculates the parameters (e.g. μ and σ in case of [StandardScaler](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)) and saves them as an internal objects state. Afterwards, you can call its transform() method to apply the transformation to a particular set of examples.

fit_transform() joins these two steps and is used for the initial fitting of parameters on the training set xx, but it also returns a transformed x′. Internally, it just calls first fit() and then transform()on the same data.
For e.g.
```
imp = Imputer()
# calculating the means
imp.fit([[1, 3], [np.nan, 2], [8, 5.5]])
```

Now the imputer have learned to use a mean (1+8)/2 = 4.5 for the first column and mean (2+3+5.5)/3 = 3.5 for the second column when it gets applied to a two-column data:

```
X = [[np.nan, 11], 
     [4,      np.nan], 
     [8,      2],
     [np.nan, 1]]
print(imp.transform(X))
```
we get
```
[[4.5, 11], 
 [4, 3.5],
 [8, 2],
 [4.5, 1]]
```
Why do we need 2 separate methods -  **fit**  and  **transform**  ?

In practice we need to have a separate training and testing dataset and that is where having a separate  **fit**  and  **transform**  method helps. We apply  **fit**  on the training dataset and use the  **transform**method on both - the training dataset and the test dataset. Thus the training as well as the test dataset are then transformed(scaled) using the model parameters that were learnt on applying the  **fit**method the training dataset.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjc4MTk5OTE4LC00MTA2OTI2MjRdfQ==
-->