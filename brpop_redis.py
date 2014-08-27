import redis
pool = redis.ConnectionPool(host='localhost', port=6384)
r = redis.Redis(connection_pool = pool)
print r.delete('list1','list2')
print r.rpush('list1','a','b','c')
keys = ['list1','list2']
print r.brpop(keys, timeout=0)
