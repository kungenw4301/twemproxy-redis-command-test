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
    print 'hset myhash field1 "foo"":\n %s' % client.hset('myhash','field1', 'foo')
    print 'hdel myhash field1":\n %s' % client.hdel('myhash', 'field1')
    print 'hdel myhash field2 :\n %s' % client.hdel('myhash', 'field2')

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
    call_test(hdel_test)
