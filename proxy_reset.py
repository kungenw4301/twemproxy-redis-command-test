#Filename: proxy_reset.py
import redis
ports = [6380, 6381, 6382, 6383]

def flush_each_instance(port):
	pool = redis.ConnectionPool(host = '127.0.0.1', port = port)
	r = redis.Redis(connection_pool = pool)
	print("flush {0}-->{1}, dbsize-->{2}".format(port, r.flushdb(), r.dbsize())) 

for i in ports:
    flush_each_instance(i)
