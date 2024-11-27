# DAT535-flight_delay_2024

Project Description
This project focuses on predicting flight delays for Southwest Airlines using machine learning models in a distributed environment with Apache Spark and Hadoop. The goal is to optimize resource allocation and evaluate the performance of different models for more accurate predictions.

___

### Technology used
**Apache Spark**: For distributed computing and model training.<br>
**Apache Hadoop**: For storing and handling large datasets.<br>
**MLlib**: Spark's machine learning library for model implementation.<br>
**Python**: For developing Spark applications.<br>

___

### Machine Learning Models
Linear Regression (LR): Baseline model.<br>
Multivariable Linear Regression (MLR): Best performance with lowest RMSE.<br>
Random Forest Regression (RF): Handles both linear and nonlinear relationships.<br>
Multilayer Perceptron Classifier (MLPC): Neural network model for deeper analysis.<br>

___

### Optimization
Tested four different Spark configurations (memory, cores, and instance resource allocation).<br>
Optimized configuration: 3 instances, 4 cores per instance, 3 GB memory.<br>

___

### Results
Best model: Multivariable Linear Regression (MLR) with $R^2$ = 0.976 and RMSE = 4.78.
Efficient resource allocation contributed to significant performance improvements in a distributed environment.

___
Acknowledgments:<br>
This readme was written with the help of ChatGPT

### Instructions
Set up a Spark and Hadoop distributed cluster.<br>
Upload the datasets to HDFS.<br>
Run the Python script for data preprocessing and model training.<br>
Analyze results via Spark UI and log files.<br>
