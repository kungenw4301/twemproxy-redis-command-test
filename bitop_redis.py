# Filename: bitop_redis.py
import redis
pool = redis.ConnectionPool(host = '127.0.0.1', port = 6384)
r = redis.Redis(connection_pool = pool)
print r.set('bitop_1','bit_key_1')
print r.set('bitop_2','bit_key_2')
print r.bitop('AND', 'result', 'bitop_1', 'bitop_2')
print r.get('result')

print r.set('bitop_1','bit_key_1_0101')
print r.set('bitop_2','bit_key_2_1010')
print r.bitop('AND', 'result2', 'bitop_1', 'bitop_2')
print r.get('result2')
