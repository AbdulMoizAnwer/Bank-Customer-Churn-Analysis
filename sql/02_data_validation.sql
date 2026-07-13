-- Verify the total number of imported records
-- Business question:
-- Did all customer records import successfully?

SELECT COUNT(*) AS total_customers
FROM customers;

-- Actual result: 10000


-- Check for duplicate customer IDs
-- Business question:
-- Does every customer have a unique identifier?

SELECT
    customer_id,
    COUNT(*) AS occurrence_count
FROM customers
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- Actual result: no rows
-- Note: The PRIMARY KEY already prevents duplicate customer_id values.


-- Check for missing values in every column
-- Business question:
-- Are there missing values that could affect reporting or modelling?

SELECT
    COUNT(*) FILTER (WHERE customer_id IS NULL) AS customer_id_nulls,
    COUNT(*) FILTER (WHERE credit_score IS NULL) AS credit_score_nulls,
    COUNT(*) FILTER (WHERE country IS NULL) AS country_nulls,
    COUNT(*) FILTER (WHERE gender IS NULL) AS gender_nulls,
    COUNT(*) FILTER (WHERE age IS NULL) AS age_nulls,
    COUNT(*) FILTER (WHERE balance IS NULL) AS balance_nulls,
    COUNT(*) FILTER (WHERE estimated_salary IS NULL) AS salary_nulls,
    COUNT(*) FILTER (WHERE tenure IS NULL) AS tenure_nulls,
    COUNT(*) FILTER (WHERE products_number IS NULL) AS products_number_nulls,
    COUNT(*) FILTER (WHERE credit_card IS NULL) AS credit_card_nulls,
    COUNT(*) FILTER (WHERE active_member IS NULL) AS active_member_nulls,
    COUNT(*) FILTER (WHERE churn IS NULL) AS churn_nulls
FROM customers;

-- Actual result:
-- 0 for every column


-- Inspect categorical values
-- Business question:
-- Do country and gender contain unexpected categories?

SELECT DISTINCT country
FROM customers
ORDER BY country;

-- Actual result:
-- France, Germany and Spain

SELECT DISTINCT gender
FROM customers
ORDER BY gender;

-- Actual result:
-- Female, Male


-- Check numerical ranges
-- Business question:
-- Do important numerical fields contain unrealistic values?

SELECT
    MIN(credit_score) AS minimum_credit_score,
    MAX(credit_score) AS maximum_credit_score,
    MIN(age) AS minimum_age,
    MAX(age) AS maximum_age,
    MIN(tenure) AS minimum_tenure,
    MAX(tenure) AS maximum_tenure,
    MIN(balance) AS minimum_balance,
    MAX(balance) AS maximum_balance,
    MIN(products_number) AS minimum_products,
    MAX(products_number) AS maximum_products,
    MIN(estimated_salary) AS minimum_salary,
    MAX(estimated_salary) AS maximum_salary
FROM customers;

-- Actual results:
-- minimum_credit_score = 350
-- maximum_credit_score = 850
-- minimum_age = 18
-- maximum_age = 92
-- minimum_tenure = 0
-- maximum_tenure = 10
-- minimum_balance = 0
-- maximum_balance = 250,898.09
-- minimum_products = 1
-- maximum_products = 4
-- minimum_salary = 11.58
-- maximum_salary = 199,992.48


-- Check for clearly invalid values
-- Business question:
-- Are there records that violate basic business rules?

SELECT *
FROM customers
WHERE credit_score < 0
   OR age <= 0
   OR tenure < 0
   OR balance < 0
   OR products_number <= 0
   OR estimated_salary < 0;

-- Actual result:
-- No rows


-- View a sample of the imported data

SELECT *
FROM customers
LIMIT 10;