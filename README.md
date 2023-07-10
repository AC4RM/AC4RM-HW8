### Introduction
- This is the week 8 homework repository of ERMC K5455 (Applied Coding for Risk Mgmt) at Columbia University. 
- Please refer to Canvas for the homework deadline.

<hr>

### How to submit the homework

1. - Implement the function `calculator(num1, num2, ops)` so that:
    - `num1` and `num2` can take any numeric number
    - `ops` can take one of `add`, `sub`, `mul` or `div`
    - return the result or print `'Invalid Operation'` if you encounter division by zero error.
2. Find the customers who located in Virginia and who have total sales more than $100. 
   - Total sales is defined as `quantity * unit_price` in the `order_items` table. 
   - Include the `customer_id`, `first_name`, `last_name` and `total_sales` columns in the result
3. We will be using the same Titanic dataset, but we will train a Decision Tree model this time
   - Follow the same preprocessing steps as HW3
   - Split the data into training and testing set (80/20) and use a random seed of 42
   - Return the decision tree model fitted on the training set and the predictions made on the test set.
4. Write a regex pattern that will only match email address ends with `.com` or `.net`
   - `re.search(regex_pattern, 'abc123@gmail.com')` => Match
   - `re.search(regex_pattern, 'abc123@gmail.net')` => Match
   - `re.search(regex_pattern, 'abc123@gmail.xyz')` => Not Match
