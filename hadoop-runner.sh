hdfs dfs -rm -r /data/output

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar \
  -input '/data/input/e_commerce_dataset.csv' \
  -output /data/output \
  -mapper mapper-productcategory.py \
  -reducer reducer-productcategory.py \
  -file mapper-productcategory.py \
  -file reducer-productcategory.py

hdfs dfs -get /data/output/part-00000 ./output/hasil_mapreduce.txt