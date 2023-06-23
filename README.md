### Introduction
- This is the week 7 homework repository of ERMC K5455 (Applied Coding for Risk Mgmt) at Columbia University. 
- Please refer to Canvas for the homework deadline.

<hr>

### How to submit the homework

1. Implement the function `check_user(user)` that uses match statement to check user type.
   - If user equals `admin`, returns `'Admin account detected'`
   - If user equals `user` or `customer`, returns `'User account detected'`
   - Else return `'Invalid'`
2. Write SQL queries to do the following:
    - In the `customers` table, give any customers born before 1990 50 extra points.
    - In `orders` table, update comments to `'Gold Customer'` for customers with more than 3000 points.
3. Using the iris datasets from the sklearn package, try to group the observations into clusters using all the features.
   - The four columns in the iris dataset are `sepal length`, `sepal width`, `petal length`, `petal width`.
   - Using `dendrogram` to figure out the best number of clusters.
   - Return the Hierarchical Cluster model re-fitted with the optimal number of clusters.
4. Write a function that uses regex to extract the number from the numeric string.
    - Some numbers could be written as 1st, 2nd, 3rd, 4th
    - `extract_numer('Today is July 4th') => '4'`
    - Hint: since we need to use `st, nd, rd, th` to find the pattern but not returning them, we can put them in a non-capturing group.
    - Return the number at the end of the function.
5. Make a slight modification to the `general_bettor` function and call it `general_bettor_quick`
   - Remove history tracking and just return final value of funds
