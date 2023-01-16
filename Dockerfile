FROM jupyter/base-notebook:python-3.10

RUN pip install pandas numpy matplotlib seaborn kafka-python fastparquet
