# My Cloud Lab Simulations

## Lab 1 - Partitioning & S3

In this lab I am trying to show that how partitioning should be implemented using a list of file objects. The assumption is that there are files that we ingest from an external source , each of size 150 MB. By looping through the files, we try to dynamically name the files using Hive-style partition string ( partition_name=value /filename). Name of the partition is the column we want to apply the partition algorithm to. Furthermore, I will try to   rove why we formatted the strings this way can speed up the search engine like Amazon Athena query.

Example:
year=2023/record_01.parquet
