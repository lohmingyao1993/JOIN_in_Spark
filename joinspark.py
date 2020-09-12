from pyspark import SparkContext

sc = SparkContext()

def split_show_views(line):
	key_value=line.split(",")
	show=key_value[0]
	views=int(key_value[1])
	return(show,views)
	
def split_show_channel(line):
	key_value=line.split(",")
	show=key_value[0]
	channel=key_value[1]
	return(show,channel)
	
def extract_channel_views(show_views_channel):
	channel=show_views_channel[1][1]
	views= show_views_channel[1][0]
	return(channel,views)

def sum_channel_viewers(a,b):
    return a + b		
		
show_views_file = sc.textFile("input/join2_gennum?.txt")
show_channel_file = sc.textFile("input/join2_genchan?.txt")	

show_views = show_views_file.map(split_show_views)
show_channel = show_channel_file.map(split_show_channel)

joined_dataset= show_views.join(show_channel)

channel_views = joined_dataset.map(extract_channel_views)

channel_views.reduceByKey(sum_channel_viewers).saveAsTextFile("output")
