# 📊 Financial Forecasting Frontier: Distributed Machine Learning

## 🔍 Project Overview
This project demonstrates how distributed computing and machine learning can be used to extract insights and make predictions from large-scale banking data. Using tools like Apache Spark, Hadoop, MapReduce, and PySpark, the project explores data processing, predictive modeling, real-time analytics, and system scalability.

## 🎯 Objectives

- Analyze banking customer data using **distributed systems**
- Build a predictive model to forecast term deposit subscriptions
- Perform **real-time stream processing** using Spark Streaming
- Use **MapReduce** to solve targeted analytical tasks
- Apply performance optimizations and parallel processing techniques

---

## 🧠 Key Features

1. **Data Ingestion with Hadoop & Hive**  
   - Setup using local and Dockerized Hadoop environments  
   - HDFS operations: file transfer, directory creation, data querying

2. **Exploratory Data Analysis with PySpark**  
   - Group-wise aggregation, filtering, visualization  
   - Feature selection based on domain insights

3. **Predictive Modeling**  
   - Logistic Regression & Random Forest with Spark MLlib  
   - Hyperparameter tuning using CrossValidator  
   - Model evaluation using accuracy, AUC

4. **MapReduce Jobs (Python)**  
   - Avg balance per job  
   - Housing loan status per education  
   - Contacts and subscriptions per month  
   - Avg duration per poutcome  
   - Avg balance per age

5. **Real-Time Transaction Monitoring (Spark Streaming)**  
   - Windowed aggregations on simulated live data  
   - Watermarking for late data handling  
   - Rolling average balance and transaction count visualization

---

### 🔧 Requirements

- Apache Spark (with PySpark)
- Hadoop (HDFS)
- Python 3.x
- Google Colab or Jupyter Notebook
- Docker (optional for Hadoop containerization)

---
### 📊 Results Summary
-Top Job Types by Avg Balance: Retired, Housemaid
-Most Contacted Month: May (Success rate: ~6.65%)
-Real-Time Stream Results: Over 4,500 simulated transactions processed in live mode
-Model AUC: 0.84 using Random Forest (100 trees)

---
### 💡 Learning Outcomes
-Hands-on experience with distributed ML pipelines
-Practical use of MapReduce and Spark Streaming
-Understanding of real-world banking analytics and feature importance
-Exposure to MLOps concepts like modularization, pipeline building, and experiment tracking

---

### 🙋‍♂️ Author
Ayush Bhagat
Capstone Project — AlmaBetter Masters Program

