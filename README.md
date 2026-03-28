# My Cloud Lab Simulations

## Lab 1 - Partitioning & S3

How does Hive-style partitioning actually work? In this lab, I take 150 MB raw data files and dynamically map them into a partitioned directory structure (key=value). I’ll walk through the logic of assigning partition names based on specific columns and prove why this formatting is the 'secret sauce' for high-speed queries in Amazon Athena.
