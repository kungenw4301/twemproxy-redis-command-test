import redis
import redis_reset

def flush_all():
    for port in [6380, 6381, 6382, 6383, 6384]:
        redis_reset.flush_each_instance(port)
    print;
proxy_pool = redis.ConnectionPool(host='localhost', port=6379)
redis_pool = redis.ConnectionPool(host='localhost', port=6384)

redis_client = redis.Redis(connection_pool = redis_pool)
proxy_client = redis.Redis(connection_pool = proxy_pool)

def discard_test(client):
    print 'command: discard';
    print 'set key1 hello:\n %s' % client.set('key1','hello')
    print 'get key1:\n %s' % (client.get('key1'))
    print 'multi:\n %s'% client.execute_command('multi')
    print 'set key1 world:\n %s' % client.set('key1','world')
    print 'discard:\n %s' % client.execute_command('discard')

    print 'get key1:\n %s' % client.get('key1')
    print 'set key1 world:\n %s' % client.set('key1','world')
    print 'get key1 world:\n %s' % client.get('key1')

if __name__ == '__main__':
    flush_all()
    d = {'redis':redis_client,'proxy':proxy_client}
    for i in d: 
	    print '%s-->\t'% (i),
	    discard_test(d[i])
	    print '\n'
	
    flush_all()

