# Mini-Project 1: Bank Branch Customer Service

## Functionality (30 points)

### The `accounts` list
This list contains records for each of the bank's existing customers. You should not edit the `accounts` list except through the appropriate functions below.

### The `get_queue_length` function
This function should do the following:
- Ask the user how many customers are in the queue and attempt to convert the response to an integer
- If the conversion failed or if the number provided is less than zero, keep asking the user until a suitable answer is provided
- Once a suitable answer is provided, return the number that results from the conversion

### The `serve_customers` function
This function should accept a customer count and then, for each number between 1 and the customer count (inclusive), do the following:
- Call a customer by their number (e.g. by printing `"Customer number _, please!"`) and ask for their name
- If their name matches an existing customer from the `accounts` list, tell them their current balance, ask them if they would like to deposit or withdraw from their account, ask them for an amount to deposit/withdraw, and process their transaction if it is valid. If it isn't valid, explain why not, and give them more chances to provide a valid amount. Reasons why a transaction might not be valid include:
  - Trying to deposit/withdraw a non-numeric amount
  - Trying to deposit/withdraw a negative amount
  - Trying to deposit/withdraw an amount with too many decimal places
  - Trying to withdraw an amount greater than the available balance
- If the name doesn't match an existing customer from the `accounts` list, ask them if they would like to open an account, and if yes, ask them for an initial deposit amount and create an account for them if their initial deposit amount is valid. If it isn't valid, explain why not, and give them more chances to provide a valid amount

### The `if __name__ == '__main__'` block
This block gets the queue length and uses this to serve all the waiting customers. You should not edit this block.

## Refactoring (30 points)
If you keep all your customer service code in one function, `serve_customers`, it will probably be very long by the end of the exercise. Try to split it out into multiple smaller functions that aren't longer than about 15 lines each (with most ideally being even shorter). As a starting point, consider moving out chunks of functionality into functions named things like `serve_customer`, `serve_new_customer`, `serve_existing_customer`, `create_new_account`, `process_deposit_into_existing_account` and `process_withdrawal_from_existing_account`.

## Testing (40 points)
There is already a test for the `get_queue_length` function. Once you have split your code into smaller functions, you should add more tests for as many of these as you can. You are advised to use the tests from the previous lessons as inspiration.
