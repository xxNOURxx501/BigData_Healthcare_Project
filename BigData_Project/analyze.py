from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, col, when

spark = SparkSession.builder \
    .appName("Complete Healthcare BigData Analysis") \
    .master("local[*]") \
    .getOrCreate()

file_path = "healthcare_dataset.csv"

df = spark.read.option("header", "true").option("inferSchema", "true").csv(file_path)

print("--- 1. Average Billing Amount by Medical Condition ---")
df.groupBy("Medical Condition") \
  .agg(avg("Billing Amount").alias("Average_Billing")) \
  .show(truncate=False)

print("--- 2. Patient Count by Blood Type ---")
df.groupBy("Blood Type") \
  .agg(count("*").alias("Patient_Count")) \
  .show(truncate=False)

print("--- 3. Filtered Patients (Age > 60) ---")
df.filter(col("Age") > 60) \
  .select("Name", "Age", "Medical Condition", "Billing Amount") \
  .show(5, truncate=False)


print("--- 4. Data Cleaning: Dropping Duplicates and Nulls ---")
initial_count = df.count()
df_cleaned = df.dropna().dropDuplicates()
cleaned_count = df_cleaned.count()
print(f"Rows before cleaning: {initial_count}")
print(f"Rows after cleaning: {cleaned_count}")

print("\n--- 5. Advanced Operation: Adding Age Category Column ---")
df_categorized = df_cleaned.withColumn(
    "Age_Category",
    when(col("Age") > 60, "Senior").otherwise("Adult")
)
df_categorized.select("Name", "Age", "Age_Category", "Medical Condition").show(5, truncate=False)

print("\n--- 6. Advanced Operation: Grouping by Medical Condition & Gender with Sorting ---")
df_categorized.groupBy("Medical Condition", "Gender") \
  .agg(avg("Billing Amount").alias("Average_Billing")) \
  .orderBy(col("Average_Billing").desc()) \
  .show(truncate=False)

spark.stop()