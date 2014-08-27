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

def expireat_test(client):
    print 'command: expireat';
    print 'set mykey hello:\n %s' % client.set('mykey','hello')
    print 'exists myket:\n %s' % client.exists('mykey')
    print 'expireat mykey 1293840000:\n %s' % client.expireat('mykey', 1293840000)
    print 'exists mykey:\n %s' % client.exists('mykey')


if __name__ == '__main__':
    flush_all()
    d = {'redis':redis_client,'proxy':proxy_client}
    for i in d: 
	    print '%s-->\t'% (i),
	    expireat_test(d[i])
	    print '\n'
	
    flush_all()

