import redis
import redis_reset
pool = redis.ConnectionPool(host='localhost', port=6384)
r = redis.Redis(connection_pool = pool)
print r.rpush('mylist','one','two','three')
print r.brpoplpush('mylist', 'myotherlist')
print 'mylist: {0}'.format(r.lrange('mylist', 0, -1))
print 'myotherlist: {0}'.format(r.lrange('myotherlist', 0, -1))

redis_reset.flush_each_instance(6384)
