hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar \
  -input '/home/ach/ach-codespace/uas-bigdata/data/E-commerce Dataset.csv' \
  -output /home/ach/ach-codespace/uas-bigdata/output \
  -mapper mapper-productcategory.py \
  -reducer reducer-productcategory.py \
  -file mapper-productcategory.py \
  -file reducer-productcategory.py
