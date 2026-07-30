# Healthcare Big Data Analytics Pipeline 🏥📊

An end-to-end Big Data processing pipeline designed to ingest, clean, store, and analyze large-scale healthcare datasets using modern big data tools.

---

## 🚀 Project Overview & Architecture

This project processes a comprehensive healthcare dataset to extract valuable insights regarding patient demographics, medical conditions, and billing amounts. The workflow follows a standard data pipeline architecture:

1. **Data Ingestion:** Loading the raw healthcare dataset (CSV) into the processing environment.
2. **Storage & Management:** Managing distributed data structures.
3. **Processing Engine:** Utilizing **Apache Spark (PySpark)** for scalable data transformation, cleaning, and aggregations.
4. **Visualization:** Connecting processed metrics to interactive dashboards (Power BI / Reporting).

---

## 🛠️ Tools & Technologies Used

* **Programming Language:** Python 🐍
* **Big Data Framework:** Apache Spark (PySpark) ⚡
* **Containerization:** Docker & Docker Compose 🐳
* **Storage Concept:** Hadoop HDFS (Distributed File System) 📂
* **Visualization:** Power BI 📈

---

## 📂 Project Structure

```text
BigData_Project/
│
├── healthcare_dataset.csv             # Raw dataset
├── analyze.py                         # PySpark script for ETL & data analytics
├── docker-compose.yml                 # Docker configuration for cluster environment
├── Healthcare & Patient Analytics.pbix# Power BI Dashboard file
└── Healthcare_BigData_Pipeline.pptx   # Project presentation slides
