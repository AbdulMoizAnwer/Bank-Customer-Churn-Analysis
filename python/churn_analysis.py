# ==========================================================
# 1. Import Libraries
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# 2. Load Dataset
# ==========================================================

df = pd.read_csv("D:\Moiz\Programming\Bank-Customer-Churn-Analysis\data/Bank Customer Churn Prediction.csv")
# Display the first five records
print(df.head())

# ==========================================================
# 3. Exploratory Data Analysis (EDA)
# ==========================================================

# Dataset dimensions
print(df.shape)

# Column names
print(df.columns)

# Display dataset information, including data types and missing values
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Generate summary statistics for numerical variables
print(df.describe())

# ==========================================================
# 4. Data Quality Assessment
# ==========================================================

# Missing Value Assessment
# No missing values were identified; therefore, no data imputation or record removal was required.

# Check for duplicate customer records
print(df.duplicated().sum())

# Categorical Variables

# Country distribution
print(df["country"].value_counts())

# Gender distribution
print(df["gender"].value_counts())

# Numerical Data Validation

# Credit score
print("Minimum credit score:", df["credit_score"].min())

# Age
print("Minimum age:", df["age"].min())
print("Maximum age:", df["age"].max())

# Account balance
print("Minimum account balance:", df["balance"].min())

# Estimated salary
print("Minimum estimated salary:", df["estimated_salary"].min())
print("Maximum estimated salary:", df["estimated_salary"].max())

# Outlier Detection

# Summary statistics for estimated salary
print(df["estimated_salary"].describe())

# Boxplot visualization for outlier detection
plt.figure(figsize=(8, 5))
plt.boxplot(df["estimated_salary"])
plt.title("Boxplot of Estimated Salary")
plt.ylabel("Estimated Salary")
plt.tight_layout()
plt.show()

# Business Interpretation:
# The boxplot indicates that the estimated salary variable does not contain statistically significant outliers. Although the minimum salary appears relatively low, it falls within the acceptable range according to the distribution shown in the boxplot.

# Interquartile Range (IQR) method for outlier detection

Q1 = df["estimated_salary"].quantile(0.25)
Q3 = df["estimated_salary"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

print(f"Lower Bound: {lower_bound:.2f}")
print(f"Upper Bound: {upper_bound:.2f}")

# Identify observations outside the IQR boundaries
outliers = df[
    (df["estimated_salary"] < lower_bound) |
    (df["estimated_salary"] > upper_bound)
]

print(f"Number of Outliers: {len(outliers)}")

# Business Interpretation:
# The summary statistics indicated a relatively low minimum estimated salary. To determine whether this represented an outlier, additional analysis was performed using a boxplot and the Interquartile Range (IQR) method. Both techniques confirmed that the estimated salary variable contains no statistically significant outliers.

# Column Name Assessment
# All column names are written in lowercase and use underscores to separate words, following Python naming conventions. Therefore, no column renaming was required.

# Target Variable Distribution
print(df["churn"].value_counts())
print((df["churn"].value_counts(normalize=True) * 100).round(2))

# Business Interpretation:
# Approximately 20% of customers have churned, while nearly 80% remain with the bank. The target variable is moderately imbalanced, but the distribution is appropriate for exploratory data analysis.

# Data Cleaning Summary
# • No missing values were identified.
# • No duplicate records were detected.
# • Data types were appropriate for analysis.
# • Categorical variables were consistent.
# • No invalid numerical values were identified.
# • No statistically significant outliers were detected.
# • Column names followed Python naming conventions and required no modification.

# Conclusion:
# The dataset passed all major data quality checks and was considered suitable for exploratory data analysis without requiring additional preprocessing.

# ==========================================================
# 5. Univariate Analysis
# ==========================================================

# Age Distribution

plt.figure(figsize=(8, 5))
plt.hist(df["age"], bins=20)

plt.title("Distribution of Customer Age")
plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Business Interpretation:
# The majority of customers are between 30 and 45 years of age. Customers older than 70 represent only a small proportion of the customer base. Overall, the bank's customers consist primarily of working-age adults.

# Credit Score Distribution

# Visualize the distribution of customer credit scores
plt.figure(figsize=(8, 5))
plt.hist(df["credit_score"], bins=20)

plt.title("Distribution of Credit Scores")
plt.xlabel("Credit Score")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Business Interpretation:
# Most customers have moderate to good credit scores. Customers with extremely low credit scores represent only a small proportion of the customer base.

# Country Distribution

print(df["country"].value_counts())

plt.figure(figsize=(8,5))
df["country"].value_counts().plot(kind="bar")

plt.title("Customers by Country")
plt.xlabel("Country")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Business Interpretation:
# France represents the largest customer segment, while Germany and Spain contribute smaller customer populations.

# Gender Distribution

# Display the number of customers by gender
print(df["gender"].value_counts())

# Visualize the gender distribution
plt.figure(figsize=(8, 5))
df["gender"].value_counts().plot(kind="bar")

plt.title("Customers by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Business Interpretation:
# The customer base is relatively balanced between male and female customers, with a slight majority of males. This balanced distribution reduces the likelihood of gender-related sampling bias and supports meaningful comparisons in the subsequent churn analysis.

# Product Ownership Distribution

# Display the number of customers by product ownership
print(df["products_number"].value_counts().sort_index())

# Visualize the distribution of banking products
plt.figure(figsize=(8, 5))
df["products_number"].value_counts().sort_index().plot(kind="bar")

plt.title("Customers by Number of Products")
plt.xlabel("Number of Products")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Percentage distribution by product ownership
product_percent = (
    df["products_number"]
    .value_counts(normalize=True)
    .sort_index() * 100
).round(2)

print(product_percent)

# Business Interpretation:
# Approximately 50.84% of customers hold one banking product, while 45.90% hold two products. Only 3.26% of customers own three or more products. This indicates that the majority of customers maintain relatively limited banking relationships, with only a small proportion using a broader range of the bank's products.

# Customer Activity Distribution

# Display the number of active and inactive customers
print(df["active_member"].value_counts())

# Visualize customer activity status
plt.figure(figsize=(8, 5))
df["active_member"].value_counts().plot(kind="bar")

plt.title("Customer Activity Status")
plt.xlabel("Active Member (0 = No, 1 = Yes)")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Percentage distribution by customer activity status
active_percent = (
    df["active_member"]
    .value_counts(normalize=True) * 100
).round(2)

print(active_percent)

# Business Interpretation:
# Approximately 51.51% of customers are active members, while 48.49% are inactive. The relatively balanced distribution indicates that nearly half of the bank's customers are not actively engaging with the bank's services. This represents a potential retention risk, as inactive customers may be more likely to leave the bank and may also present fewer opportunities for cross-selling additional products.

# Credit Card Ownership Distribution

# Display the number of customers with and without a credit card
print(df["credit_card"].value_counts())

# Visualize credit card ownership
plt.figure(figsize=(8, 5))
df["credit_card"].value_counts().plot(kind="bar")

plt.title("Customers with Credit Card")
plt.xlabel("Credit Card (0 = No, 1 = Yes)")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Percentage distribution by credit card ownership
credit_card_percent = (
    df["credit_card"]
    .value_counts(normalize=True) * 100
).round(2)

print(credit_card_percent)

# Business Interpretation:
# Approximately 70.55% of customers own a credit card issued by the bank, while 29.45% do not. This indicates that credit card ownership is common among the bank's customers and reflects strong adoption of one of the bank's core products. High credit card ownership may provide additional opportunities for customer engagement through card-related services, rewards programmes, and targeted marketing campaigns.

# ==========================================================
# 6. Bivariate Analysis
# ==========================================================

# Customer Churn by Country

# Business Question:
# Which country has the highest customer churn rate?

# Calculate the number of churned and retained customers by country
country_churn = pd.crosstab(df["country"], df["churn"])
print(country_churn)

# Visualize customer churn by country
plt.figure(figsize=(8, 5))
country_churn.plot(kind="bar")

plt.title("Customer Churn by Country")
plt.xlabel("Country")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Calculate the churn rate (%) by country
country_churn_rate = (
    pd.crosstab(
        df["country"],
        df["churn"],
        normalize="index"
    ) * 100
).round(2)

print(country_churn_rate)

# Business Interpretation:
# Although France recorded a similar number of churned customers (810) compared with Germany (814), Germany has a substantially smaller customer base. The churn rate analysis shows that approximately 32.44% of customers in Germany left the bank, compared with 16.15% in France and 16.67% in Spain. This indicates that customers in Germany are considerably more likely to leave the bank than customers in the other two countries. These findings suggest that customer retention challenges are more pronounced in the German market.

# Business Recommendation:
# The bank should prioritise customer retention initiatives in Germany. Further investigation should be conducted to identify the underlying causes of the higher churn rate, such as customer satisfaction, product offerings, pricing strategies, service quality, or competitive pressures. Based on these findings, targeted retention programmes and personalised customer engagement strategies should be implemented.

# Customer Churn by Gender

# Business Question:
# Does customer churn differ between male and female customers?

# Calculate the number of churned and retained customers by gender
gender_churn = pd.crosstab(df["gender"], df["churn"])
print(gender_churn)

# Visualize customer churn by gender
plt.figure(figsize=(8, 5))
gender_churn.plot(kind="bar")

plt.title("Customer Churn by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Calculate the churn rate (%) by gender
gender_churn_rate = (
    pd.crosstab(
        df["gender"],
        df["churn"],
        normalize="index"
    ) * 100
).round(2)

print(gender_churn_rate)

# Business Interpretation:
# The customer churn rate differs noticeably between male and female customers. Although the dataset contains slightly more male customers, female customers exhibit a considerably higher churn rate. Approximately 25.07% of female customers left the bank compared with 16.46% of male customers. These findings suggest that gender is associated with customer churn and should be considered alongside other customer characteristics in churn analysis.

# Business Recommendation:
# The bank should investigate the factors contributing to the higher churn rate among female customers. This may include evaluating customer satisfaction, product suitability, service quality, pricing, communication, and engagement across gender segments. However, customer retention strategies should not be based on gender alone. Gender should be analysed together with other factors such as age, customer activity, number of products, country, and account balance to develop more targeted and effective retention initiatives.

# Customer Churn by Age

# Business Question:
# Are older customers more likely to leave the bank?

# Visualize the age distribution by customer churn
plt.figure(figsize=(8, 5))
df.boxplot(column="age", by="churn")

plt.title("Age by Customer Churn")
plt.suptitle("")
plt.xlabel("Customer Churn (0 = No, 1 = Yes)")
plt.ylabel("Age")

plt.tight_layout()
plt.show()

# Summary statistics by customer churn
age_summary = df.groupby("churn")["age"].describe()
print(age_summary)

# Business Interpretation: The boxplot and summary statistics indicate a clear difference in the age distribution between customers who remained with the bank and those who churned. Customers who left the bank have a noticeably higher median age (45 years) than customers who remained (36 years). The upward shift in the age distribution suggests that older customers are more likely to discontinue their banking relationship. These findings indicate that age is an important factor associated with customer churn and should be considered together with other customer characteristics when assessing customer retention risk.

# Business Recommendation:
# The bank should further investigate why older customers exhibit higher churn rates. Targeted retention initiatives, such as personalised financial advice, retirement planning services, loyalty programmes, and relationship management support, may help strengthen engagement among older customers. However, age should not be considered in isolation and should be analysed alongside account balance, customer activity, product ownership, and country before implementing retention strategies.

# Customer Churn by Credit Score

# Business Question:
# Does credit score influence customer retention?

# Visualize the credit score distribution by customer churn
plt.figure(figsize=(8, 5))
df.boxplot(column="credit_score", by="churn")

plt.title("Credit Score by Customer Churn")
plt.suptitle("")
plt.xlabel("Customer Churn (0 = No, 1 = Yes)")
plt.ylabel("Credit Score")

plt.tight_layout()
plt.show()

# Summary statistics by customer churn
credit_summary = df.groupby("churn")["credit_score"].describe()
print(credit_summary)

# Business Interpretation:
# The boxplot and summary statistics show substantial overlap between the credit score distributions of customers who remained with the bank and those who churned. Although churned customers have a slightly lower median credit score (646) than retained customers (653), the difference is relatively small. These findings suggest that credit score alone is not a strong indicator of customer churn and should be interpreted together with behavioural and demographic variables.

# Business Recommendation:
# The bank should avoid relying solely on credit score when identifying customers at risk of churn. Instead, credit score should be incorporated into a broader customer risk assessment model alongside variables such as customer activity, product ownership, account balance, tenure, age, and country. A multi-factor approach is likely to provide more accurate predictions and support more effective customer retention strategies.

# Customer Churn by Account Balance

# Business Question:
# Does account balance influence customer churn?

# Visualize the account balance distribution by customer churn
plt.figure(figsize=(8, 5))
df.boxplot(column="balance", by="churn")

plt.title("Account Balance by Customer Churn")
plt.suptitle("")
plt.xlabel("Customer Churn (0 = No, 1 = Yes)")
plt.ylabel("Account Balance")

plt.tight_layout()
plt.show()

# Summary statistics by customer churn
balance_summary = df.groupby("churn")["balance"].describe()
print(balance_summary)

# Business Interpretation:
# The relationship between account balance and customer churn was examined using both a boxplot and summary statistics. The boxplot indicates that customers who churned generally maintained higher account balances than customers who remained with the bank. This observation is supported by the summary statistics, which show that both the average account balance (91,108.54 vs. 72,745.30) and the median account balance (109,349.29 vs. 92,072.68) are higher among churned customers than retained customers. Although many retained customers have relatively low or zero account balances, customers with larger balances appear to be overrepresented in the churned group. These findings suggest that account balance is associated with customer churn and indicate that the bank may be losing customers who represent higher financial value.

# Business Recommendation:
# The bank should prioritise retention efforts for customers with higher account balances, as losing these customers may result in a disproportionate loss of deposits and future business opportunities. Relationship managers should proactively engage these customers through personalised financial advice, premium banking services, investment products, and loyalty programmes. Further analysis should also investigate whether high-balance customers are leaving because of limited product usage, lower engagement, dissatisfaction with services, or more attractive offers from competing financial institutions. Combining account balance with variables such as customer activity, age, tenure, number of products, and country will enable more effective customer retention strategies.

# Customer Churn by Estimated Salary

# Business Question:
# Is customer salary associated with churn?

# Visualize the estimated salary distribution by customer churn
plt.figure(figsize=(8, 5))
df.boxplot(column="estimated_salary", by="churn")

plt.title("Estimated Salary by Customer Churn")
plt.suptitle("")
plt.xlabel("Customer Churn (0 = No, 1 = Yes)")
plt.ylabel("Estimated Salary")

plt.tight_layout()
plt.show()

# Summary statistics by customer churn
salary_summary = df.groupby("churn")["estimated_salary"].describe()
print(salary_summary)

# Business Interpretation:
# The relationship between estimated salary and customer churn was analysed using both a boxplot and summary statistics. The boxplot shows substantial overlap in the salary distributions of customers who remained with the bank and those who churned. This observation is supported by the summary statistics, which indicate that both the average estimated salary (101,465.68 vs. 99,738.39) and the median estimated salary (102,460.84 vs. 99,645.04) are very similar across the two groups. These findings suggest that estimated salary has only a weak association with customer churn and is not a strong standalone predictor of customer retention.

# Business Recommendation:
# Since estimated salary demonstrates only a weak relationship with customer churn, the bank should avoid using customer income as the primary criterion for identifying customers at risk of leaving. Instead, greater emphasis should be placed on variables that exhibit stronger relationships with churn, such as customer activity, product ownership, age, account balance, and country. Estimated salary may still contribute to a broader predictive model, but it should not be relied upon independently when developing customer retention strategies.

# Customer Churn by Number of Products

# Business Question:
# Does owning more banking products reduce churn?

# Calculate the number of churned and retained customers by number of products
product_churn = pd.crosstab(df["products_number"], df["churn"])
print(product_churn)

# Visualize customer churn by number of products
plt.figure(figsize=(8, 5))
product_churn.plot(kind="bar")

plt.title("Customer Churn by Number of Products")
plt.xlabel("Number of Products")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Calculate churn rate (%) by number of products
product_churn_rate = (
    pd.crosstab(
        df["products_number"],
        df["churn"],
        normalize="index"
    ) * 100
).round(2)

print(product_churn_rate)

# Visualize churn rate (%) by number of products
plt.figure(figsize=(8, 5))
product_churn_rate.plot(kind="bar", stacked=True)

plt.title("Customer Churn Rate by Number of Products")
plt.xlabel("Number of Products")
plt.ylabel("Percentage of Customers")
plt.legend(["Stayed", "Churned"])

plt.tight_layout()
plt.show()

# Business Interpretation:
# The relationship between the number of banking products and customer churn was analysed using grouped bar charts and churn rate percentages. Customers holding two banking products exhibit the lowest churn rate, suggesting that they are the most loyal customer segment. Customers with only one product are considerably more likely to leave the bank, indicating a weaker customer relationship. Although customers with three or four products display very high churn rates, these groups contain relatively few customers and should therefore be interpreted with caution. Overall, product ownership appears to be an important behavioural indicator of churn.

# Business Recommendation:
# The bank should focus on increasing customer engagement by encouraging customers with only one product to adopt additional suitable products, such as savings accounts, credit cards, investment services, or loans. A broader banking relationship may strengthen customer loyalty and reduce churn risk. At the same time, the unusually high churn rates among customers with three or four products should be investigated further to determine whether these results are caused by small sample sizes or other underlying issues.

# Customer Churn by Activity Status

# Business Question:
# Are inactive customers more likely to churn?

# Calculate the number of churned and retained customers by activity status
active_churn = pd.crosstab(df["active_member"], df["churn"])
print(active_churn)

# Visualize customer churn by activity status
plt.figure(figsize=(8, 5))
active_churn.plot(kind="bar")

plt.title("Customer Churn by Activity Status")
plt.xlabel("Active Member (0 = No, 1 = Yes)")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Calculate churn rate (%) by activity status
active_churn_rate = (
    pd.crosstab(
        df["active_member"],
        df["churn"],
        normalize="index"
    ) * 100
).round(2)

print(active_churn_rate)

# Business Interpretation:
# The relationship between customer activity status and churn was analysed using a grouped bar chart and churn rate percentages. Inactive customers have a churn rate of approximately 26.85%, compared with 14.27% for active customers. This means inactive customers are almost twice as likely to leave the bank. The findings suggest that customer engagement plays a significant role in retention.

# Business Recommendation:
# The bank should prioritise engagement initiatives for inactive customers. Strategies such as personalised communication, digital banking campaigns, financial education, loyalty programmes, and tailored product recommendations may encourage customers to use banking services more frequently. Customer activity should also be included as a key variable in future churn prediction models.

# Customer Churn by Credit Card Ownership

# Business Question:
# Does owning a credit card influence customer retention?

# Calculate the number of churned and retained customers by credit card ownership
credit_churn = pd.crosstab(df["credit_card"], df["churn"])
print(credit_churn)

# Visualize customer churn by credit card ownership
plt.figure(figsize=(8, 5))
credit_churn.plot(kind="bar")

plt.title("Customer Churn by Credit Card Ownership")
plt.xlabel("Credit Card (0 = No, 1 = Yes)")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()

# Calculate churn rate (%) by credit card ownership
credit_churn_rate = (
    pd.crosstab(
        df["credit_card"],
        df["churn"],
        normalize="index"
    ) * 100
).round(2)

print(credit_churn_rate)

# Business Interpretation:
# The relationship between credit card ownership and customer churn was analysed using a grouped bar chart and churn rate percentages. Although customers with credit cards account for a larger number of churn cases in absolute terms, they also represent a substantially larger proportion of the bank's customer base. The churn rate analysis shows that approximately 20.18% of customers with a credit card and 20.81% of customers without a credit card left the bank. The difference between these groups is minimal, suggesting that credit card ownership has only a weak association with customer churn and is not a reliable standalone indicator of customer retention.

# Business Recommendation:
# The bank should avoid relying on credit card ownership as a primary indicator of customer loyalty or churn risk. Instead, retention strategies should focus on variables that demonstrate stronger relationships with churn, such as customer activity, age, product ownership, account balance, and country. Further analysis could also investigate whether credit card usage, transaction frequency, reward programme participation, or spending behaviour influence customer retention.

# Customer Churn by Tenure

# Business Question:
# Does the length of the customer relationship affect churn?

# Visualize the tenure distribution by customer churn
plt.figure(figsize=(8, 5))
df.boxplot(column="tenure", by="churn")

plt.title("Tenure by Customer Churn")
plt.suptitle("")
plt.xlabel("Customer Churn (0 = No, 1 = Yes)")
plt.ylabel("Tenure (Years)")

plt.tight_layout()
plt.show()

# Summary statistics by customer churn
tenure_summary = df.groupby("churn")["tenure"].describe()
print(tenure_summary)

# Business Interpretation:
# The relationship between customer tenure and churn was analysed using both a boxplot and summary statistics. The boxplot shows substantial overlap in the tenure distributions of customers who remained with the bank and those who churned. The summary statistics indicate that the average tenure is very similar for retained customers (5.03 years) and churned customers (4.93 years), while both groups share the same median tenure of 5 years. These findings suggest that customer tenure has only a weak association with churn and is not a strong standalone indicator of customer retention.

# Business Recommendation:
# Since customer tenure demonstrates only a weak relationship with churn, the bank should avoid using tenure as the sole criterion for identifying customers at risk of leaving. Instead, tenure should be considered alongside stronger behavioural indicators such as customer activity, product ownership, age, account balance, and country. Combining tenure with these variables in a predictive model is likely to improve the bank's ability to identify customers who would benefit from targeted retention initiatives.

# ==========================================================
# 7. Correlation Analysis
# ==========================================================

# Calculate the correlation matrix for numerical variables
# Customer ID is excluded because it is a unique identifier and does not carry business meaning.
numeric_df = df.drop(columns=["customer_id"]).select_dtypes(include=["number"])

correlation = numeric_df.corr().round(2)
print(correlation)

# Visualize the correlation matrix
plt.figure(figsize=(10, 8))

image = plt.imshow(
    correlation,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

plt.colorbar(image, label="Correlation Coefficient")

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=90
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Matrix")

plt.tight_layout()
plt.show()

# Business Interpretation:
# A correlation analysis was conducted to examine the linear relationships among the numerical variables in the dataset. The results indicate that age has the strongest positive correlation with customer churn (r = 0.29), suggesting that older customers are more likely to leave the bank. Active membership exhibits the strongest negative correlation with churn (r = -0.16), indicating that active customers are less likely to discontinue their banking relationship. Account balance shows a weak positive correlation with churn (r = 0.12), suggesting that customers with higher balances are slightly more likely to leave the bank. In contrast, estimated salary (r = 0.01), tenure (r = -0.01), credit card ownership (r = -0.01), and credit score (r = -0.03) display only very weak relationships with churn. Overall, the correlation analysis supports the findings obtained from the earlier bivariate analyses by confirming that age and customer activity are among the variables most strongly associated with customer churn.

# Business Recommendation:
# The bank should prioritise variables demonstrating stronger relationships with customer churn, particularly customer activity, age, account balance, and product ownership, when developing predictive models and customer retention strategies. Variables with weak correlations, such as estimated salary, tenure, credit card ownership, and credit score, should not be used independently to identify customers at risk of leaving. Instead, these variables may provide additional predictive value when combined with behavioural and demographic characteristics in a comprehensive churn prediction model.

# Limitation:
# Correlation analysis measures the strength and direction of linear relationships between variables but does not imply causation. Therefore, although age and customer activity are associated with customer churn, these relationships do not necessarily indicate that they directly cause customers to leave the bank.

# ==========================================================
# 8. Key Business Insights
# ==========================================================

# i. Germany recorded the highest customer churn rate (32.4%), almost twice that of France and Spain, indicating that the German market should be prioritised for customer retention initiatives.

# ii. Older customers were more likely to churn, suggesting that age is an important demographic factor associated with customer retention.

# iii. Inactive customers exhibited nearly twice the churn rate of active customers, highlighting customer engagement as one of the strongest indicators of churn.

# iv. Customers holding two banking products demonstrated the lowest churn rate, whereas customers with only one product were considerably more likely to leave the bank.

# v. Customers with higher account balances appeared more frequently in the churned group, suggesting that the bank may be losing financially valuable customers.

# vi. Estimated salary, credit card ownership, tenure, and credit score demonstrated only weak relationships with customer churn and should not be used independently for customer retention decisions.

# vii. Correlation analysis confirmed that age and customer activity exhibited the strongest relationships with customer churn, supporting the findings obtained through the earlier exploratory analyses.