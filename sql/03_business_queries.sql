-- Business question:
-- How many customers left the bank, and how many remained?

SELECT
    churn,
    COUNT(*) AS customer_count
FROM customers
GROUP BY churn
ORDER BY churn;

-- Actual Result
-- FALSE = 7,963 customers remained
-- TRUE  = 2,037 customers churned

-- Business Interpretation:
-- Of the 10,000 customers, 2,037 have churned and 7,963 were retained. This establishes the overall scale of customer attrition in the dataset.


-- Business question:
-- What percentage of customers left the bank?

SELECT
    COUNT(*) AS total_customers,
    COUNT(*) FILTER (WHERE churn = TRUE) AS churned_customers,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE churn = TRUE) / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM customers;

-- Actual Result
-- total_customers = 10,000
-- churned_customers = 2,037
-- churn_rate_percentage = 20.37%

-- Business Interpretation:
-- The overall churn rate is 20.37%, meaning approximately one in five customers left the bank.


-- Business question:
-- In which country is customer attrition highest?

SELECT
    country,
    COUNT(*) AS total_customers,
    COUNT(*) FILTER (WHERE churn = TRUE) AS churned_customers,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE churn = TRUE) / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM customers
GROUP BY country
ORDER BY churn_rate_percentage DESC;

-- Actual Result
-- country total_customers churned_customers  churn_rate_percentage
-- Germany	   2509	             814	          32.44
-- Spain	   2477	             413	          16.67
-- France	   5014	             810	          16.15

-- Business Interpretation:
-- Germany has the highest churn rate at 32.44%, nearly twice the rates observed in Spain and France. Although Germany and France lost a similar number of customers, France has approximately twice as many customers overall. Therefore, Germany represents the more serious proportional retention issue.


-- Business question:
-- Is customer inactivity associated with a higher churn rate?

SELECT
    active_member,
    COUNT(*) AS total_customers,
    COUNT(*) FILTER (WHERE churn = TRUE) AS churned_customers,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE churn = TRUE) / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM customers
GROUP BY active_member
ORDER BY active_member;

-- Actual Result
-- active_member total_customers churned_customers churn_rate_percentage
-- false	         4849	          1302	              26.85
-- true	             5151	           735	              14.27

-- Business Interpretation:
-- Inactive customers have a churn rate of 26.85%, compared with 14.27% among active customers. This suggests that customer inactivity may be a useful warning indicator. The bank could test targeted engagement campaigns to determine whether increased activity improves retention.


-- Business question:
-- Is the number of products owned related to customer churn?

SELECT
    products_number,
    COUNT(*) AS total_customers,
    COUNT(*) FILTER (WHERE churn = TRUE) AS churned_customers,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE churn = TRUE) / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM customers
GROUP BY products_number
ORDER BY products_number;

-- Actual Result
-- products_number total_customers churned_customers churn_rate_percentage
--       1	            5084	         1409	            27.71
--       2	            4590	          348	             7.58
--       3               266              220               82.71
--       4                60               60                 100

-- Business Interpretation:
-- Customers with two products have the lowest churn rate at 7.58%, while customers with one product have a churn rate of 27.71%. -- This suggests that customers with two products may have a stronger relationship with the bank than customers holding only one product.
--
-- Customers with three or four products show very high churn rates. However, these groups contain only 266 and 60 customers respectively, so the results should be interpreted cautiously. Further analysis of product combinations, fees, customer needs and service experience would be required before recommending additional products.


-- Business question:
-- How do churned customers differ from retained customers?

SELECT
    churn,
    ROUND(AVG(age), 2) AS average_age,
    ROUND(AVG(credit_score), 2) AS average_credit_score,
    ROUND(AVG(balance), 2) AS average_balance,
    ROUND(AVG(tenure), 2) AS average_tenure,
    ROUND(AVG(products_number), 2) AS average_products,
    ROUND(AVG(estimated_salary), 2) AS average_salary
FROM customers
GROUP BY churn
ORDER BY churn;

-- Actual Result
-- churn average_age average_credit_score average_balance average_tenure average_products average_salary
-- false	37.41	      651.85	          72745.30	       5.03	          1.54	         99738.39
-- true	    44.84	      645.35	          91108.54	       4.93	          1.48	        101465.68

-- Business Interpretation:
-- Churned customers are older on average and hold higher average balances than retained customers. Credit score, tenure, product ownership and estimated salary show smaller average differences.
--
-- These descriptive results suggest that age and balance may be useful variables for further churn analysis. However, statistical testing or predictive modelling would be needed to determine whether the differences are statistically significant or independently associated with churn.


-- Business question:
-- Which high-value customers may require closer retention attention?

SELECT
    customer_id,
    country,
    age,
    balance,
    products_number,
    active_member,
    churn
FROM customers
ORDER BY balance DESC
LIMIT 10;

-- Actual Result
-- customer_id  country    age   balance  products_number  active_member  churn
-- 15757408	     Spain	    38	250898.09	     3	           true	       true
-- 15715622	     France	    57	238387.56	     1	           true	       true
-- 15714241	     Spain	    42	222267.63	     1	           false	   true
-- 15571958	     Spain	    40	221532.80	     1	           false	   false
-- 15586674	     Spain	    58	216109.88	     1	           true	       true
-- 15599131	     Germany	26	214346.96	     2	           false	   false
-- 15594408	     Spain	    48	213146.20	     1	           false	   true
-- 15769818	     France	    37	212778.20	     1	           true	       false
-- 15620268	     Germany	43	212696.32	     1	           false	   false
-- 15780212	     France	    37	212692.97	     1	           false	   false

-- Business Interpretation:
-- Among the ten customers with the highest balances, six are inactive and five have already churned. This indicates substantial exposure to customer loss among high-balance customers. Customers who have already churned may be considered for win-back analysis, while retained but inactive customers may require proactive retention attention.


-- Business question:
-- Which retained but inactive high-balance customers may require
-- proactive retention attention?

SELECT
    customer_id,
    country,
    age,
    balance,
    products_number,
    active_member,
    churn
FROM customers
WHERE active_member = FALSE
  AND churn = FALSE
ORDER BY balance DESC
LIMIT 10;

-- Actual Result
-- customer_id country   age    balance   products_number active_member  churn
-- 15571958	    Spain	  40	221532.80	     1	          false	     false
-- 15599131	    Germany	  26	214346.96	     2	          false	     false
-- 15620268	    Germany	  43	212696.32	     1	          false	     false
-- 15780212	    France	  37	212692.97	     1	          false	     false
-- 15627971	    France	  32	206663.75	     1	          false	     false
-- 15664498	    France	  26	205962.00	     1	          false	     false
-- 15745433	    Germany	  30	205770.78	     2	          false	     false
-- 15746664	    Spain	  20	204223.03	     1	          false	     false
-- 15663888	    Germany	  34	204017.40	     2	          false	     false
-- 15620570	    France	  43	202443.47	     1	          false	     false

-- Business Interpretation:
-- These customers have not yet churned but are inactive and hold the highest balances within that segment. They may be suitable candidates for a targeted retention review, subject to further investigation of behaviour, profitability and contact eligibility.