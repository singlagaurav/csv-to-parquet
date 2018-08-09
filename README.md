# CSV to Parquet
A Python script that transform a csv file to Apache Parquet format

### How to use:
  Insert the values of csvPath and parquetFilename variables then just run:
 ```sh
  python3 csv-to-parquet.py
 ```

### Requirements:
  - Python >= 3
  - pandas: https://pandas.pydata.org/

### How to test using spark-shell:
```sh
 spark-shell
 val df = spark.read.parquet("parquet filepath")
 df.show
```
