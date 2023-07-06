### Introduction
- This is the week 8 homework repository of ERMC K5455 (Applied Coding for Risk Mgmt) at Columbia University. 
- Please refer to Canvas for the homework deadline.

<hr>

### How to submit the homework

1. - Implement the function `calculator(num1, num2, ops)` so that:
    - `num1` and `num2` can take any numeric number
    - `ops` can take one of `add`, `sub`, `mul` or `div`
    - return the result or print `'Invalid Operation'` if you encounter division by zero error.
2. Write SQL queries to do the following:
    - In the `customers` table, give any customers born before 1990 50 extra points.
    - In `orders` table, update comments to `'Gold Customer'` for customers with more than 3000 points.
3. Using the iris datasets from the sklearn package, try to group the observations into clusters using all the features.
   - The four columns in the iris dataset are `sepal length`, `sepal width`, `petal length`, `petal width`.
   - Using `dendrogram` to figure out the best number of clusters.
   - Return the Hierarchical Cluster model re-fitted with the optimal number of clusters.
4. Write a regex pattern that will only match email address ends with `.com` or `.net`
   - `re.search(regex_pattern, 'abc123@gmail.com')` => Match
   - `re.search(regex_pattern, 'abc123@gmail.net')` => Match
   - `re.search(regex_pattern, 'abc123@gmail.xyz')` => Not Match
