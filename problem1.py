import argparse
import re

from pyspark import SparkContext, SparkConf
conf = SparkConf().setMaster("local").setAppName('Word Count')
sc = SparkContext(conf=conf)

def quiet_logs(sc):
    logger = sc._jvm.org.apache.log4j
    logger.LogManager.getLogger("org"). setLevel( logger.Level.ERROR )
    logger.LogManager.getLogger("akka").setLevel( logger.Level.ERROR )

quiet_logs(sc)

def main():
	lines  = sc.textFile(args.infile)
	lines  = lines.map(lambda line: line.encode('ascii','ignore').strip().upper())
	words  = lines.flatMap(lambda word: re.split('[^A-Z]+',word))
	words  = words.flatMap(lambda line: line.split())
	pairs  = words.map(lambda word: (len(word), 1))
	counts = pairs.reduceByKey(lambda a, b: a+b)

	results = counts.collect()
	print results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    args = parser.parse_args()

    main()

