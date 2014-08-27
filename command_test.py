import redis


def flush_each_instance(port):
	pool = redis.ConnectionPool(host = '127.0.0.1', port = port)
	r = redis.Redis(connection_pool = pool)
	print("flush {0}-->{1}, dbsize-->{2}".format(port, r.flushdb(), r.dbsize())) 


def flush_all():
    for port in [6380, 6381, 6382, 6383, 6384]:
        pool = redis.ConnectionPool(host = '127.0.0.1', port = port)
        r = redis.Redis(connection_pool = pool)
        print('flush {0}>{1}, dbsize>{2} |'.format(port, r.flushdb(), r.dbsize())),
    print '\n' 

proxy_pool = redis.ConnectionPool(host='localhost', port=6379)
redis_pool = redis.ConnectionPool(host='localhost', port=6384)

redis_client = redis.Redis(connection_pool = redis_pool)
proxy_client = redis.Redis(connection_pool = proxy_pool)

def getrange_test(client):
    print 'command: getrange';
    print 'set mykey "this is a string":\n %s' % client.set('mykey', 'this is a string')
    print 'getrange mykey 0 3:\n %s' % client.getrange('mykey', 0, 3)
    print 'getrange mykey -3 -1:\n %s' % client.getrange('mykey', -3, -1)
    print 'getrange mykey 0 -1:\n %s' % client.getrange('mykey', 0, -1)
    print 'getrange mykey 10 100:\n %s' % client.getrange('mykey', 10, 100)

def getset_test(client):
    print 'command: getset';
    print 'set mykey "Hello"":\n %s' % client.set('mykey', 'Hello')
    print 'getset mykey "world":\n %s' % client.getset('mykey', 'World')
    print 'get mykey :\n %s' % client.get('mykey')

def hdel_test(client):
    print 'command: hdel';
    print 'hset myhash field1 "foo":\n %s' % client.hset('myhash','field1', 'foo')
    print 'hdel myhash field1:\n %s' % client.hdel('myhash', 'field1')
    print 'hdel myhash field2 :\n %s' % client.hdel('myhash', 'field2')

def hexists_test(client):
    print 'command: exists';
    print 'hset myhash field1 "foo":\n %s' % client.hset('myhash','field1', 'foo')
    print 'hexists myhash field1:\n %s' % client.hexists('myhash', 'field1')
    print 'hexists myhash field2 :\n %s' % client.hexists('myhash', 'field2')


def hget_test(client):
    print 'command: hget';
    print 'hset myhash field1 "foo":\n %s' % client.hset('myhash','field1', 'foo')
    print 'hget myhash field1:\n %s' % client.hget('myhash', 'field1')
    print 'hget myhash field2 :\n %s' % client.hget('myhash', 'field2')

def hgetall_test(client):
    print 'command: hgetall';
    print 'hset myhash field1 "Hello":\n %s' % client.hset('myhash','field1', 'Hello')
    print 'hset myhash field2 "World":\n %s' % client.hset('myhash','field2', 'World')
    print 'hgetall myhash :\n %s' % client.hgetall('myhash')

def hincrby_test(client):
    print 'command: hincrby';
    print 'hset myhash field 5:\n %s' % client.hset('myhash','field',5)
    print 'hincrby myhash field 1:\n %s' % client.hincrby('myhash','field', 1)
    print 'hincrby myhash field -1 :\n %s' % client.hincrby('myhash', 'field', -1)
    print 'hincrby myhash field -10:\n %s' % client.hincrby('myhash', 'field', -10)

def hincrbyfloat_test(client):
    print 'command: hincrbyfloat';
    print 'hset mykey field 10.50:\n %s' % client.hset('mykey','field', 10.50)
    print 'hincrbyfloat mykey field 0.1:\n %s' % client.hincrbyfloat('mykey','field', 0.1)
    print 'hset mykey field 5.0e3 :\n %s' % client.hset('mykey', 'field', 5.0e3)
    print 'hincrbyfloat mykey field 2.0e2:\n %s' % client.hincrbyfloat('mykey', 'field', 2.0e2)

def hkeys_test(client):
    print 'command: hkeys';
    print 'hset myhash field1 "Hello":\n %s' % client.hset('myhash', 'field1', 'Hello')
    print 'hset myhash field2 "World":\n %s' % client.hset('myhash', 'field2', 'World')
    print 'hkeys myhash:\n %s' % client.hkeys('myhash')

def hlen_test(client):
    print 'command: hlen';
    print 'hset myhash field1 "Hello":\n %s' % client.hset('myhash', 'field1', 'Hello')
    print 'hset myhash field2 "World":\n %s' % client.hset('myhash', 'field2', 'World')
    print 'hlen myhash:\n %s' % client.hlen('myhash')

def hmget_test(client):
    print 'command: hmget';
    print 'hset myhash field1 "Hello":\n %s' % client.hset('myhash', 'field1', 'Hello')
    print 'hset myhash field2 "World":\n %s' % client.hset('myhash', 'field2', 'World')
    print 'hmget myhash field1 field2 nofield:\n %s' % client.hmget('myhash', 'field1', 'field2', 'nofield')

def hmset_test(client):
    print 'command: hmset';
    mapping = {'field1': 'Hello', 'field2':'World'}
    print 'hset myhash field1 "Hello" field2 "World":\n %s' % client.hmset('myhash', mapping)
    print 'hget myhash field1:\n %s' % client.hget('myhash', 'field1')
    print 'hget myhash field2:\n %s' % client.hget('myhash', 'field2')

def hset_test(client):
    print 'command: hset';
    print 'hset myhash field1 "Hello":\n %s' % client.hset('myhash', 'field1', 'Hello')
    print 'hget myhash field1:\n %s' % client.hget('myhash', 'field1')

def hsetnx_test(client):
    print 'command: hsetnx';
    print 'hsetnx myhash field "Hello":\n %s' % client.hsetnx('myhash', 'field', 'Hello')
    print 'hsetnx myhash field "World":\n %s' % client.hsetnx('myhash', 'field', 'World')
    print 'hget myhash field:\n %s' % client.hget('myhash', 'field')

def hvals_test(client):
    print 'command: hvals';
    print 'hset myhash field1 "Hello":\n %s' % client.hset('myhash', 'field1', 'Hello')
    print 'hset myhash field2 "World":\n %s' % client.hset('myhash', 'field2', 'World')
    print 'hvals myhash:\n %s' % client.hvals('myhash')

def incr_test(client):
    print 'command: incr';
    print 'set mykey "10":\n %s' % client.set('mykey', '10')
    print 'incr mykey:\n %s' % client.incr('mykey')
    print 'get mykey:\n %s' % client.get('mykey')

def incrby_test(client):
    print 'command: incrby';
    print 'set mykey "10":\n %s' % client.set('mykey', '10')
    print 'incrby mykey 5:\n %s' % client.incr('mykey', amount = 5)
    print 'get mykey:\n %s' % client.get('mykey')

def incrbyfloat_test(client):
    print 'command: incrbyfloat';
    print 'set mykey 10.50:\n %s' % client.set('mykey', 10.50)
    print 'incrbyfloat mykey 0.1:\n %s' % client.incrbyfloat('mykey', 0.1)
    print 'set mykey 5.0e3 :\n %s' % client.set('mykey', 5.0e3)
    print 'incrbyfloat mykey 2.0e2:\n %s' % client.incrbyfloat('mykey', 2.0e2)

def lindex_test(client):
    print 'command: lindex';
    print 'lpush mylist "World":\n %s' % client.lpush('mylist', "World")
    print 'lpush mylist "Hello":\n %s' % client.lpush('mylist', "Hello")
    print 'lindex 0 :\n %s' % client.lindex('mylist', 0)
    print 'lindex -1 :\n %s' % client.lindex('mylist', -1)
    print 'lindex 3 :\n %s' % client.lindex('mylist', 3)

def linsert_test(client):
    print 'command: linsert';
    print 'rpush mylist "Hello":\n %s' % client.rpush('mylist', "Hello")
    print 'rpush mylist "World":\n %s' % client.rpush('mylist', "World")
    print 'linsert mylist BEFORE "World" "There" :\n %s' % client.linsert('mylist','before' ,'World', 'There')
    print 'lrange 0 -1 :\n %s' % client.lrange('mylist',0, -1)

def llen_test(client):
    print 'command: llen';
    print 'lpush mylist "World":\n %s' % client.lpush('mylist', "World")
    print 'lpush mylist "Hello":\n %s' % client.lpush('mylist', "Hello")
    print 'llen "mylist" :\n %s' % client.llen('mylist')

def lpop_test(client):
    print 'command: lpop';
    print 'rpush mylist "one":\n %s' % client.rpush('mylist', "one")
    print 'rpush mylist "two":\n %s' % client.rpush('mylist', "two")
    print 'rpush mylist "three":\n %s' % client.rpush('mylist', "three")
    print 'lpop mylist :\n %s' % client.lpop('mylist')
    print 'lrange 0 -1 :\n %s' % client.lrange('mylist',0, -1)

def lpush_test(client):
    print 'command: lpush';
    print 'lpush mylist "World":\n %s' % client.lpush('mylist', "World")
    print 'lpush mylist "Hello":\n %s' % client.lpush('mylist', "Hello")
    print 'lrange "mylist" :\n %s' % client.lrange('mylist', 0, -1)

def lpushx_test(client):
    print 'command: lpushx';
    print 'lpush mylist "World":\n %s' % client.lpush('mylist', "World")
    print 'lpushx mylist "Hello":\n %s' % client.lpushx('mylist', "Hello")
    print 'lpush myotherlist "Hello":\n %s' % client.lpushx('myotherlist', "Hello")
    print 'lrange "mylist" :\n %s' % client.lrange('mylist', 0, -1)
    print 'lrange "myotherlist" :\n %s' % client.lrange('myotherlist', 0, -1)

def lrange_test(client):
    print 'command: lrange';
    print 'rpush mylist "one":\n %s' % client.rpush('mylist', "one")
    print 'rpush mylist "two":\n %s' % client.rpush('mylist', "two")
    print 'rpush mylist "three":\n %s' % client.rpush('mylist', "three")
    print 'lrange "mylist 0 0" :\n %s' % client.lrange('mylist', 0, 0)
    print 'lrange "mylist -3 2" :\n %s' % client.lrange('mylist', -3, 2)
    print 'lrange "mylist -100 100" :\n %s' % client.lrange('mylist', -100, 100)
    print 'lrange "mylist 5 10" :\n %s' % client.lrange('mylist', 5, 10)


def lrem_test(client):
    print 'command: lrem';
    print 'rpush mylist "hello":\n %s' % client.rpush('mylist', "hello")
    print 'rpush mylist "hello":\n %s' % client.rpush('mylist', "hello")
    print 'rpush mylist "foo":\n %s' % client.rpush('mylist', "foo")
    print 'rpush mylist "hello":\n %s' % client.rpush('mylist', "hello")
    print 'lrange "mylist 0 -1":\n %s' % client.lrange('mylist', 0, -1)
    print 'lrem  mylist -2 "hello(Redis)":\n %s' % client.lrem('mylist', 'hello', -2)
    #print 'lrem mylist -2 "hello":\n %s' % client.execute_command('LREM', 'mylist', -2, 'hello')
    print 'lrange "mylist 0 -1" :\n %s' % client.lrange('mylist', 0, -1)


def lset_test(client):
    print 'command: lset';
    print 'rpush mylist "one":\n %s' % client.rpush('mylist', "one")
    print 'rpush mylist "two":\n %s' % client.rpush('mylist', "two")
    print 'rpush mylist "three":\n %s' % client.rpush('mylist', "three")
    print 'lset mylist 0 "four"" :\n %s' % client.lset('mylist', 0, "four")
    print 'lset "mylist -2 "five"" :\n %s' % client.lset('mylist', -2, "five")
    print 'lrange "mylist 0 -1" :\n %s' % client.lrange('mylist', 0, -1)

def ltrim_test(client):
    print 'command: ltrim';
    print 'rpush mylist "one":\n %s' % client.rpush('mylist', "one")
    print 'rpush mylist "two":\n %s' % client.rpush('mylist', "two")
    print 'rpush mylist "three":\n %s' % client.rpush('mylist', "three")
    print 'ltrim mylist 1 -1 :\n %s' % client.ltrim('mylist', 1, -1)
    print 'lrange "mylist 0 -1" :\n %s' % client.lrange('mylist', 0, -1)

def mget_test(client):
    print 'command: mget';
    print 'set key1 "Hello":\n %s' % client.set('key1', "Hello")
    print 'set key2 "World":\n %s' % client.set('key2', "World")
    print 'mget key1 key2 nonexisting:\n %s' % client.mget('key1', "key2", 'nonexisting')


def mset_test(client):
    print 'command: mset';
    mapping = {'key1': "Hello", 'key2': "World"}
    print 'mset key1 "Hello" key2 "World":\n %s' % client.mset(mapping)
    print 'get key1:\n %s' % client.get('key1')
    print 'get key2:\n %s' % client.get('key2')


def msetnx_test(client):
    print 'command: msetnx';
    mapping = {'key1':'hello', 'key2':'there'}
    print 'msetnx key1 "hello" key2 "there":\n %s' % client.msetnx(mapping)
    mapping = {'key2':'there', 'key3':'world'}
    print 'msetnx key2 "there" key3 "world":\n %s' % client.msetnx(mapping)
    print 'mget key1 key2 key3:\n %s' % client.mget('key1', "key2", 'key3')

def multi_test(client):
    pass


def persist_test(client):
    print 'command: persist';
    print 'set mykey "Hello":\n %s' % client.set('mykey', "Hello")
    print 'expire mykey 10:\n %s' % client.expire('mykey', 10)
    print 'TTL mykey:\n %s' % client.ttl('mykey')
    print 'persist mykey:\n %s' % client.persist('mykey')
    print 'TTL mykey:\n %s' % client.ttl('mykey')


def pexpire_test(client):
    print 'command: pexpire';
    print 'set mykey "Hello":\n %s' % client.set('mykey', "Hello")
    print 'pexpire mykey 1500:\n %s' % client.pexpire('mykey', 1500)
    print 'TTL mykey:\n %s' % client.ttl('mykey')
    print 'PTTL mykey:\n %s' % client.pttl('mykey')


def pexpireat_test(client):
    print 'command: pexpireat';
    print 'set mykey "Hello":\n %s' % client.set('mykey', "Hello")
    print 'pexpireat mykey  1555555555005:\n %s' % client.pexpireat('mykey',1555555555005)
    print 'TTL mykey:\n %s' % client.ttl('mykey')
    print 'PTTL mykey:\n %s' % client.pttl('mykey')


def psetex_test(client):
    print 'command: psetex';
    print 'psetex mykey 1000 "Hello":\n %s' % client.psetex('mykey',1000, "Hello")
    print 'PTTL mykey:\n %s' % client.pttl('mykey')
    print 'GET mykey:\n %s' % client.get('mykey')

def pttl_test(client):
    print 'command: pttl';
    print 'set mykey "Hello":\n %s' % client.set('mykey', "Hello")
    print 'expire mykey 1 :\n %s' % client.expire('mykey',1)
    print 'PTTL mykey:\n %s' % client.pttl('mykey')


def randomkey_test(client):
    print 'command: randomkey';
    print 'set key1 "Hello":\n %s' % client.set('key1', "Hello")
    print 'set key2 "World" :\n %s' % client.set('key2',"World")
    print 'set key3 "there" :\n %s' % client.set('key3',"there")
    print 'randomkey :\n %s' % client.randomkey()


def rpop_test(client):
    print 'command: rpop';
    print 'rpush mylist "one":\n %s' % client.rpush('mylist', "one")
    print 'rpush mylist "two":\n %s' % client.rpush('mylist', "two")
    print 'rpush mylist "three":\n %s' % client.rpush('mylist', "three")
    print 'rpop mylist :\n %s' % client.rpop('mylist')
    print 'lrange mylist 0 -1 :\n %s' % client.lrange('mylist', 0, -1)


def rpoplpush_test(client):
    print 'command: rpoplpush';
    print 'rpush mylist "one":\n %s' % client.rpush('{my}list', "one")
    print 'rpush mylist "two":\n %s' % client.rpush('{my}list', "two")
    print 'rpush mylist "three":\n %s' % client.rpush('{my}list', "three")
    print 'rpoplpush mylist myotherlist :\n %s' % client.rpoplpush('{my}list', '{my}otherlist')
    print 'lrange mylist 0 -1 :\n %s' % client.lrange('{my}list', 0, -1)
    print 'lrange myotherlist 0 -1 :\n %s' % client.lrange('{my}otherlist', 0, -1)


def rpush_test(client):
    print 'command: rpush';
    print 'rpush mylist "hello":\n %s' % client.rpush('mylist', "hello")
    print 'rpush mylist "world":\n %s' % client.rpush('mylist', "world")
    print 'lrange mylist 0 -1 :\n %s' % client.lrange('mylist', 0, -1)


def rpushx_test(client):
    print 'command: rpushx';
    print 'rpush mylist "Hello":\n %s' % client.rpush('mylist', "Hello")
    print 'rpush mylist "World":\n %s' % client.rpush('mylist', "World")
    print 'rpushx myotherlist "World":\n %s' % client.rpushx('myotherlist', "World")
    print 'lrange mylist 0 -1 :\n %s' % client.lrange('mylist', 0, -1)
    print 'lrange myotherlist 0 -1 :\n %s' % client.lrange('myotherlist', 0, -1)


def sadd_test(client):
    print 'command: sadd';
    print 'sadd myset "Hello":\n %s' % client.sadd('myset', "Hello")
    print 'sadd myset "World":\n %s' % client.sadd('myset', "World")
    print 'sadd myset "World":\n %s' % client.sadd('myset', "World")
    print 'smembers :\n %s' % client.smembers('myset')


def scard_test(client):
    print 'command: scard';
    print 'sadd myset "Hello":\n %s' % client.sadd('myset', "Hello")
    print 'sadd myset "World":\n %s' % client.sadd('myset', "World")
    print 'scard myset:\n %s' % client.scard('myset')


def sdiff_test(client):
    print 'command: sdiff';
    print 'sadd key1 "a":\n %s' % client.sadd('key1', "a")
    print 'sadd key1 "b":\n %s' % client.sadd('key1', "b")
    print 'sadd key1 "c":\n %s' % client.sadd('key1', "c")
    print 'sadd key2 "c":\n %s' % client.sadd('key2', "c")
    print 'sadd key2 "d":\n %s' % client.sadd('key2', "d")
    print 'sadd key2 "e":\n %s' % client.sadd('key2', "e")
    print 'sdiff key1 key2:\n %s' % client.sdiff('key1', 'key2')


def sdiffstore_test(client):
    print 'command: sdiffstore';
    print 'sadd key1 "a":\n %s' % client.sadd('key1', "a")
    print 'sadd key1 "b":\n %s' % client.sadd('key1', "b")
    print 'sadd key1 "c":\n %s' % client.sadd('key1', "c")
    print 'sadd key2 "c":\n %s' % client.sadd('key2', "c")
    print 'sadd key2 "d":\n %s' % client.sadd('key2', "d")
    print 'sadd key2 "e":\n %s' % client.sadd('key2', "e")
    print 'sdiffstore key key1 key2:\n %s' % client.sdiffstore('key', 'key1', 'key2')
    print 'smembers key:\n %s' % client.smembers('key')

def set_test(client):
    print 'command: set'
    print 'set mykey "Hello":\n %s' % client.set('mykey', 'Hello')
    print 'get mykey:\n %s' % client.get('mykey')

def setbit_test(client):
    print 'command: setbit'
    print 'setbit mykey 7 1:\n %s' % client.setbit('mykey', 7, 1)
    print 'get mykey:\n %s' % (client.get("mykey"))
    print 'setbit mykey 7 0:\n %s' % client.setbit('mykey', 7, 0)
    print 'get mykey:\n %s' % client.get('mykey')


def setex_test(client):
    print 'command: setex'
    print 'setex mykey 10 "Hello":\n %s' % client.setex('mykey', time=10, value="Hello")
    print 'TTL mykey:\n %s' % client.ttl('mykey')
    print 'get mykey:\n %s' % client.get('mykey')


def setnx_test(client):
    print 'command: setnx'
    print 'setnx mykey "Hello":\n %s' % client.setnx('mykey',"Hello")
    print 'setnx mykey "World":\n %s' % client.setnx('mykey',"World")
    print 'get mykey:\n %s' % client.get('mykey')


def setrange_test(client):
    print 'command: setrange'
    print 'set key1 "Hello World":\n %s' % client.set('key1',"Hello World")
    print 'setrange key1 6 "Redis":\n %s' % client.setrange('key1', 6, "Redis")
    print 'get key1:\n %s' % client.get('key1')
    print 'setrange key2 6 "Redis":\n %s' % client.setrange('key2', 6, "Redis")
    print 'get key2:\n %s' % client.get('key2')


def sinter_test(client):
    print 'command: sinter';
    print 'sadd key1 "a":\n %s' % client.sadd('key1', "a")
    print 'sadd key1 "b":\n %s' % client.sadd('key1', "b")
    print 'sadd key1 "c":\n %s' % client.sadd('key1', "c")
    print 'sadd key2 "c":\n %s' % client.sadd('key2', "c")
    print 'sadd key2 "d":\n %s' % client.sadd('key2', "d")
    print 'sadd key2 "e":\n %s' % client.sadd('key2', "e")
    print 'sinter key1 key2:\n %s' % client.sinter('key1', 'key2')


def sinterstore_test(client):
    print 'command: sinterstore';
    print 'sadd key1 "a":\n %s' % client.sadd('key1', "a")
    print 'sadd key1 "b":\n %s' % client.sadd('key1', "b")
    print 'sadd key1 "c":\n %s' % client.sadd('key1', "c")
    print 'sadd key2 "c":\n %s' % client.sadd('key2', "c")
    print 'sadd key2 "d":\n %s' % client.sadd('key2', "d")
    print 'sadd key2 "e":\n %s' % client.sadd('key2', "e")
    print 'sinterstore key key1 key2:\n %s' % client.sinterstore('key', 'key1', 'key2')
    print 'smembers key:\n %s' % client.smembers('key')


def sismember_test(client):
    print 'command: sismember';
    print 'sadd myset "one":\n %s' % client.sadd('myset', "one")
    print 'sismember myset "one":\n %s' % client.sismember('myset', 'one' )
    print 'sismember myset "two":\n %s' % client.sismember('myset', 'two' )

def smembers_test(client):
    print 'command: smembers';
    print 'sadd myset "Hello":\n %s' % client.sadd('myset', "Hello")
    print 'sadd myset "World":\n %s' % client.sadd('myset', "World")
    print 'smembers myset":\n %s' % client.smembers('myset')


def smove_test(client):
    print 'command: smove';
    print 'sadd myset "one":\n %s' % client.sadd('myset', "one")
    print 'sadd myset "two":\n %s' % client.sadd('myset', "two")
    print 'sadd myotherset "three":\n %s' % client.sadd('myotherset', "three")
    print 'smove myset myother "two":\n %s' % client.smove('myset', 'myotherset', 'two')
    print 'smembers myset":\n %s' % client.smembers('myset')
    print 'smembers myiotherset":\n %s' % client.smembers('myotherset')


def sort_test(client):
    print 'command: sort';
    print 'sadd myset "one":\n %s' % client.sadd('myset', "one")
    print 'sadd myset "two":\n %s' % client.sadd('myset', "two")
    print 'sadd myset "three":\n %s' % client.sadd('myset', "three")
    print 'sadd myset "four"":\n %s' % client.sadd('myset', 'four')
    print 'sadd myset "five"":\n %s' % client.sadd('myset', 'five')
    print 'sort myset alpha:\n %s' % client.sort('myset', alpha = True)


def spop_test(client):
    print 'command: spop';
    print 'sadd myset "one":\n %s' % client.sadd('myset', "one")
    print 'sadd myset "two":\n %s' % client.sadd('myset', "two")
    print 'sadd myset "three":\n %s' % client.sadd('myset', "three")
    print 'sadd myset "four"":\n %s' % client.sadd('myset', 'four')
    print 'sadd myset "five"":\n %s' % client.sadd('myset', 'five')
    print 'spop myset:\n %s' % client.spop('myset')
    print 'smembers myset:\n %s' % client.smembers('myset')


def srandmember_test(client):
    print 'command: srandmember';
    print 'sadd myset one two three:\n %s' % client.sadd('myset', "one", "two", "three")
    print 'srandmember myset:\n %s' % client.srandmember('myset')
    print 'srandmember myset 2:\n %s' % client.srandmember('myset', 2)
    print 'srandmember myset -5:\n %s' % client.srandmember('myset', -5)


def srem_test(client):
    print 'command: srem';
    print 'sadd myset one two three:\n %s' % client.sadd('myset', "one", "two", "three")
    print 'srem myset one:\n %s' % client.srem('myset', 'one')
    print 'srem myset four:\n %s' % client.srem('myset', 'four')
    print 'smembers myset:\n %s' % client.smembers('myset')


def strlen_test(client):
    print 'command: strlen';
    print 'set myset "Hello World":\n %s' % client.set('mykey', "Hello World")
    print 'strlen mykey:\n %s' % client.strlen('mykey')
    print 'strlen nonexisting:\n %s' % client.strlen('nonexisting')


def sunion_test(client):
    print 'command: sunion';
    print 'sadd key1 "a":\n %s' % client.sadd('key1', "a")
    print 'sadd key1 "b":\n %s' % client.sadd('key1', "b")
    print 'sadd key1 "c":\n %s' % client.sadd('key1', "c")
    print 'sadd key2 "c":\n %s' % client.sadd('key2', "c")
    print 'sadd key2 "d":\n %s' % client.sadd('key2', "d")
    print 'sadd key2 "e":\n %s' % client.sadd('key2', "e")
    print 'sunion key1 key2 :\n %s' % client.sunion('key1', 'key2')


def sunionstore_test(client):
    print 'command: sunionstore';
    print 'sadd key1 "a":\n %s' % client.sadd('key1', "a")
    print 'sadd key1 "b":\n %s' % client.sadd('key1', "b")
    print 'sadd key1 "c":\n %s' % client.sadd('key1', "c")
    print 'sadd key2 "c":\n %s' % client.sadd('key2', "c")
    print 'sadd key2 "d":\n %s' % client.sadd('key2', "d")
    print 'sadd key2 "e":\n %s' % client.sadd('key2', "e")
    print 'sunion key key1 key2 :\n %s' % client.sunionstore('key', 'key1', 'key2')
    print 'smembers key:\n %s' % client.smembers('key')


def ttl_test(client):
    print 'command: ttl';
    print 'set mykey "Hello":\n %s' % client.set('mykey', "Hello")
    print 'expire mykey:\n %s' % client.expire('mykey', 10)
    print 'ttl mykey:\n %s' % client.ttl('mykey')


def zadd_test(client):
    print 'command: zadd';
    print 'zadd myzset 1 "one":\n %s' % client.zadd('myzset', "one", 1.0)
    print 'zadd myzset 1 "uno":\n %s' % client.zadd('myzset', "uno", 1.0)
    print 'zadd myzset 2 "two" 3 "three" "one":\n %s' % client.zadd('myzset',  "two", 2.0, "three", 3.0)
    print 'zrange myzset 0 -1 withscores:\n %s' % client.zrange('myzset', 0, -1, withscores = True)
    local_port = {'redis':6384, 'proxy':6379}

    #print client is redis_client

    if (client is redis_client):
        port = local_port['redis']
    else:
        port = local_port['proxy']

    r = redis.StrictRedis(host='localhost', port = port)
    print 'StrictRedis-->port:%s-->zadd myzset 1 "niuno":\n %s' % (port, r.zadd('myzset', 1, "niuno"))


def zcard_test(client):
    print 'command: zcard';
    print 'zadd myzset 1 "one":\n %s' % client.zadd('myzset', "one", 1.0)
    print 'zadd myzset 2 "two":\n %s' % client.zadd('myzset', "two", 2.0)
    print 'zcard myzset:\n %s' % client.zcard('myzset')


def zcount_test(client):
    print 'command: zcount';
    print 'zadd myzset 1 "one":\n %s' % client.zadd('myzset', "one", 1.0)
    print 'zadd myzset 2 "two":\n %s' % client.zadd('myzset', "two", 2.0)
    print 'zadd myzset 3 "three":\n %s' % client.zadd('myzset', "three", 3.0)
    print 'zcount myzset:\n %s' % client.zcount('myzset', '-inf', '+inf')
    print 'zcount myzset:\n %s' % client.zcount('myzset', '(1', 3)


def zincrby_test(client):
    print 'command: zincrby';
    print 'zadd myzset 1 "one":\n %s' % client.zadd('myzset', "one", 1.0)
    print 'zadd myzset 2 "two":\n %s' % client.zadd('myzset', "two", 2.0)
    print 'zincrby myzset 2 "one":\n %s' % client.zincrby('myzset', "one",  2.0)
    print 'zrange myzset 0 -1 withscores:\n %s' % client.zrange('myzset', 0, -1, withscores = True)


def zinterstore_test(client):
    print 'command: zinterstore';
    print 'zadd zset1 1 "one":\n %s' % client.zadd('zset1', "one", 1.0)
    print 'zadd zset1 2 "two":\n %s' % client.zadd('zset1', "two", 2.0)
    print 'zadd zset2 1 "one":\n %s' % client.zadd('zset2', "one", 1.0)
    print 'zadd zset2 2 "two":\n %s' % client.zadd('zset2', "two", 2.0)
    print 'zadd zset2 3 "three":\n %s' % client.zadd('zset2', "three", 3.0)
    weighted_set = {'zset1': 2, 'zset2':3}
    print 'zinterstore out 2  zset1 zset2 weights 2 3:\n %s' % client.zinterstore('out', weighted_set, aggregate='SUM')
    print 'zrange myzset 0 -1 withscores:\n %s' % client.zrange('out', 0, -1, withscores = True)


def zlexcount_test(client):
    print 'command: zlexcount';
    print 'ZADD myzset 0 a 0 b 0 c 0 d 0 e:\n %s' % client.zadd('myzset', 'a', 0, 'b', 0, 'c', 0, 'd', 0, 'e', 0)
    print 'zadd myzset 0 f 0 g:\n %s' % client.zadd('myzset', 'f', 0, 'g', 0)
    print 'zlexcount myzset - +:\n %s' % client.zlexcount('myzset', '-', '+')
    print 'zlexcount myzset [b [f:\n %s' % client.zlexcount('myzset', '[b', '[f')

def zrange_test(client):
    print 'command: zrange';
    print 'zadd myzset 1 "one":\n %s' % client.zadd('myzset', 'one', 1)
    print 'zadd myzset 2 "two":\n %s' % client.zadd('myzset', 'two', 2)
    print 'zadd myzset 3 "three":\n %s' % client.zadd('myzset', 'three', 3)
    print 'zrange myzset 0 -1:\n %s' % client.zrange('myzset', 0, -1)
    print 'zrange myzset 2 3:\n %s' % client.zrange('myzset', 2, 3)
    print 'zrange myzset -2 -1:\n %s' % client.zrange('myzset', -2, -1)

def zrangebylex_test(client):
    print 'command: zrangebylex';
    print 'ZADD myzset 0 a 0 b 0 c 0 d 0 e 0 f 0 g:\n %s' % client.zadd('myzset', 'a', 0, 'b', 0, 'c', 0, 'd', 0, 'e', 0, 'f', 0, 'g', 0)
    print 'zrangebylex myzset - [c:\n %s' % client.zrangebylex('myzset', '-', '[c')
    print 'zrangebylex myzset - (c:\n %s' % client.zrangebylex('myzset', '-', '(c')
    print 'zrangebylex myzset [aaa (g:\n %s' % client.zrangebylex('myzset', '[aaa', '(g')

def zrangebyscore_test(client):
    print 'command: zrangebyscore';
    print 'zadd myzset 1 "one":\n %s' % client.zadd('myzset', 'one', 1)
    print 'zadd myzset 2 "two":\n %s' % client.zadd('myzset', 'two', 2)
    print 'zadd myzset 3 "three":\n %s' % client.zadd('myzset', 'three', 3)
    print 'zrangebyscore myzset -inf +inf:\n %s' % client.zrangebyscore('myzset', '-inf', '+inf')
    print 'zrangebyscore myzset 1 2:\n %s' % client.zrangebyscore('myzset', 1, 2)
    print 'zrangebyscore myzset (1 2:\n %s' % client.zrangebyscore('myzset', '(1', 2)
    print 'zrangebyscore myzset (1 (2:\n %s' % client.zrangebyscore('myzset', '(1', '(2')

def zrank_test(client):
    print 'command: zrank';
    print 'zadd myzset 1 "one":\n %s' % client.zadd('myzset', 'one', 1)
    print 'zadd myzset 2 "two":\n %s' % client.zadd('myzset', 'two', 2)
    print 'zadd myzset 3 "three":\n %s' % client.zadd('myzset', 'three', 3)
    print 'zrank myzset "three":\n %s' % client.zrank('myzset', 'three')
    print 'zrank myzset "four":\n %s' % client.zrank('myzset', 'four')

def zrem_test(client):
    print 'command: zrem';
    print 'zadd myzset 1 "one":\n %s' % client.zadd('myzset', 'one', 1)
    print 'zadd myzset 2 "two":\n %s' % client.zadd('myzset', 'two', 2)
    print 'zadd myzset 3 "three":\n %s' % client.zadd('myzset', 'three', 3)
    print 'zrem myzset "two":\n %s' % client.zrem('myzset', 'two')
    print 'zrange myzset 0 -1 WITHSCORES:\n %s' % client.zrange('myzset', 0, -1, withscores = True)

def zremrangebylex_test(client):
    print 'command: zremrangebylex';
    print 'zadd myzset 0 aaaa 0 b 0 c 0 d 0 e:\n %s' % client.zadd('myzset', 'aaaa', 0, 'b', 0, 'c', 0, 'd', 0, 'e', 0)
    print 'zadd myzset 0 foo 0 zap 0 zip 0 ALPHA 0 alpha:\n %s' % client.zadd('myzset', 'foo', 0, 'zap', 0, 'zip', 0, 'ALPHA', 0, 'alpha', 0)
    print 'zremrangebylex myzset [alpha [omega:\n %s' % client.zremrangebylex('myzset', '[alpha', '[omega')
    print 'zrange myzset 0 -1:\n %s' % client.zrange('myzset', 0, -1)

def zremrangebyrank_test(client):
    print 'command: zremrangebyrank';
    print 'zadd myzset 1 "one":\n %s' % client.zadd('myzset', 'one', 1)
    print 'zadd myzset 2 "two":\n %s' % client.zadd('myzset', 'two', 2)
    print 'zadd myzset 3 "three":\n %s' % client.zadd('myzset', 'three', 3)
    print 'zremrangebyrank myzset 0 1:\n %s' % client.zremrangebyrank('myzset', 0, 1)
    print 'zrange myzset 0 -1 WITHSCORES:\n %s' % client.zrange('myzset', 0, -1, withscores = True)

def zremrangebyscore_test(client):
    print 'command: zremrangebyscore';
    print 'zadd myzset 1 "one":\n %s' % client.zadd('myzset', 'one', 1)
    print 'zadd myzset 2 "two":\n %s' % client.zadd('myzset', 'two', 2)
    print 'zadd myzset 3 "three":\n %s' % client.zadd('myzset', 'three', 3)
    print 'zremrangebyscore myzset 0 1:\n %s' % client.zremrangebyscore('myzset', '-inf', '(2')
    print 'zrange myzset 0 -1 WITHSCORES:\n %s' % client.zrange('myzset', 0, -1, withscores = True)

def zrevrange_test(client):
    print 'command: zrevrange';
    print 'zadd myzset 1 "one":\n %s' % client.zadd('myzset', 'one', 1)
    print 'zadd myzset 2 "two":\n %s' % client.zadd('myzset', 'two', 2)
    print 'zadd myzset 3 "three":\n %s' % client.zadd('myzset', 'three', 3)
    print 'zrevrange myzset 0 -1:\n %s' % client.zrevrange('myzset', 0, -1)
    print 'zrevrange myzset 2 3:\n %s' % client.zrevrange('myzset', 2, 3)
    print 'zrevrange myzset -2 -1:\n %s' % client.zrevrange('myzset', -2, -1)

def zrevrangebyscore_test(client):
    print 'command: zrevrangebyscore';
    print 'zadd myzset 1 "one":\n %s' % client.zadd('myzset', 'one', 1)
    print 'zadd myzset 2 "two":\n %s' % client.zadd('myzset', 'two', 2)
    print 'zadd myzset 3 "three":\n %s' % client.zadd('myzset', 'three', 3)
    print 'zrevrangebyscore myzset -inf +inf\n %s' % client.zrevrangebyscore('myzset', '+inf', '-inf')
    print 'zrevrangebyscore myzset 2 1:\n %s' % client.zrevrangebyscore('myzset', 2, '1')
    print 'zrevrangebyscore myzset 2 (1:\n %s' % client.zrevrangebyscore('myzset', 2, '(1')
    print 'zrevrangebyscore myzset (2 (1:\n %s' % client.zrevrangebyscore('myzset', '(2', '(1')

def zrevrank_test(client):
    print 'command: zrevrank';
    print 'zadd myzset 1 "one":\n %s' % client.zadd('myzset', 'one', 1)
    print 'zadd myzset 2 "two":\n %s' % client.zadd('myzset', 'two', 2)
    print 'zadd myzset 3 "three":\n %s' % client.zadd('myzset', 'three', 3)
    print 'zrevrank myzset "one":\n %s' % client.zrevrank('myzset', 'one')
    print 'zrevrank myzset "four":\n %s' % client.zrevrank('myzset', 'four')

def zscore_test(client):
    print 'command: zscore';
    print 'zadd myzset 1 "one":\n %s' % client.zadd('myzset', 'one', 1)
    print 'zscore myzset "one":\n %s' % client.zscore('myzset', 'one')

def zunionstore_test(client):
    print 'command: zunionstore';
    print 'zadd zset1 1 "one":\n %s' % client.zadd('zset1', "one", 1.0)
    print 'zadd zset1 2 "two":\n %s' % client.zadd('zset1', "two", 2.0)
    print 'zadd zset2 1 "one":\n %s' % client.zadd('zset2', "one", 1.0)
    print 'zadd zset2 2 "two":\n %s' % client.zadd('zset2', "two", 2.0)
    print 'zadd zset2 3 "three":\n %s' % client.zadd('zset2', "three", 3.0)
    weighted_set = {'zset1': 2, 'zset2':3}
    print 'zunionstore out 2  zset1 zset2 weights 2 3:\n %s' % client.zunionstore('out', weighted_set, aggregate='SUM')
    print 'zrange myzset 0 -1 withscores:\n %s' % client.zrange('out', 0, -1, withscores = True)

def scan_test(client):
    print 'command: scan';

    i = 0;
    while i <= 50:
        client.set('key'+ str(i), 'value'+str(i))
        i += 1

    print 'scan 0:\n '
    print client.scan(cursor=0)

def sscan_test(client):
    print 'command: sscan';
    print 'sadd myset 1 2 3 foo foobar feelsgood:\n %s' % client.sadd('myset', 1, 2, 3, 'foo', 'foobar', 'feelsgood')
    print 'sscan myset 0 match f*:\n ' 
    print client.sscan('myset', 0, match='f*')

def hscan_test(client):
    print 'command: hscan';
    mapping = {'name': 'Jake', 'age': 33}
    print 'hmset hash name Jake age 33:\n %s' % client.hmset('hash', mapping)
    print 'hscan hash 0 :\n ' 
    print client.hscan('hash', 0)

def zscan_test(client):
    print 'command: zscan';
    print 'zadd myzset 0 aaaa 0 b 0 c 0 d 0 e:\n %s' % client.zadd('myzset', 'aaaa', 0, 'b', 0, 'c', 0, 'd', 0, 'e', 0)
    print 'zadd myzset 0 foo 0 zap 0 zip 0 ALPHA 0 alpha:\n %s' % client.zadd('myzset', 'foo', 0, 'zap', 0, 'zip', 0, 'ALPHA', 0, 'alpha', 0)
    print 'zscan myzset:\n ' 
    print client.zscan('myzset', 0)












#call the specific method with function name
def call_test(func):
    flush_all()
    d = {'redis':redis_client,'proxy':proxy_client}
    for i in d: 
	    print '%s-->\t\t\t'% (i),
	    func(d[i])
	    print '\n'
	
    flush_all()

if __name__ == '__main__':
    #call_test(getrange_test)
    #call_test(getset_test)
    #call_test(hdel_test)
    #call_test(hexists_test)
    #call_test(hget_test)
    #call_test(hgetall_test)
    #call_test(hincrby_test)
    #call_test(hincrbyfloat_test)
    #call_test(hkeys_test)
    #call_test(hlen_test)
    #call_test(hmget_test)
    #call_test(hmset_test)
    #call_test(hset_test)
    #call_test(hsetnx_test)
    #call_test(hvals_test)
    #call_test(incr_test)
    #call_test(incrby_test)
    #call_test(incrbyfloat_test)
    #call_test(lindex_test)
    #call_test(linsert_test)
    #call_test(llen_test)
    #call_test(lpop_test)
    #call_test(lpush_test)
    #call_test(lpushx_test)
    #call_test(lrange_test)
    #call_test(lrem_test)
    #call_test(lset_test)
    #call_test(ltrim_test)
    #call_test(mget_test)
    #call_test(mset_test)
    #call_test(msetnx_test)
    #call_test(multi_test)
    #call_test(persist_test)
    #call_test(pexpire_test)
    #call_test(pexpireat_test)
    #call_test(psetex_test)
    #call_test(pttl_test)
    #call_test(randomkey_test)
    #call_test(rpop_test)
    #call_test(rpoplpush_test)
    #call_test(rpush_test)
    #call_test(rpushx_test)
    #call_test(sadd_test)
    #call_test(scard_test)
    #call_test(sdiff_test)
    #call_test(sdiffstore_test)
    #call_test(set_test)
    #call_test(setbit_test)
    #call_test(setex_test)
    #call_test(setnx_test)
    #call_test(setrange_test)
    #call_test(sinter_test)
    #call_test(sinterstore_test)
    #call_test(sismember_test)
    #call_test(smembers_test)
    #call_test(smove_test)
    #call_test(sort_test)
    #call_test(spop_test)
    #call_test(srandmember_test)
    #call_test(srem_test)
    #call_test(strlen_test)
    #call_test(sunion_test)
    #call_test(sunionstore_test)
    #call_test(ttl_test)
    #call_test(zadd_test)
    #call_test(zcard_test)
    #call_test(zcount_test)
    #call_test(zincrby_test)
    #call_test(zinterstore_test)
    #call_test(zlexcount_test)
    #call_test(zrange_test)
    #call_test(zrangebylex_test)
    #call_test(zrangebyscore_test)
    #call_test(zrank_test)
    #call_test(zrem_test)
    #call_test(zremrangebylex_test)
    #call_test(zremrangebyrank_test)
    #call_test(zremrangebyscore_test)
    #call_test(zrevrange_test)
    #call_test(zrevrangebyscore_test)
    #call_test(zrevrank_test)
    #call_test(zscore_test)
    #call_test(zunionstore_test)
    #call_test(scan_test)
    #call_test(sscan_test)
    call_test(hscan_test)
    #call_test(zscan_test)
