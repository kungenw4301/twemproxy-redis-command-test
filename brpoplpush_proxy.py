import redis
import proxy_reset
pool = redis.ConnectionPool(host='localhost', port=6379)
r = redis.Redis(connection_pool = pool)
print r.rpush('mylist','one','two','three')
print r.brpoplpush('mylist', 'myotherlist')
print 'mylist: {0}'.format(r.lrange('mylist', 0, -1))
print 'myotherlist: {0}'.format(r.lrange('myotherlist', 0, -1))

for i in [6380, 6381, 6382, 6383]:
    proxy_reset.flush_each_instance(i)
