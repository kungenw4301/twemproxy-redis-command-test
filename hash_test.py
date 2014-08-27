import subprocess;
char = map(chr, range(97, 123)); #for 'a' ~ 'z': 97 ~ 123 , for 'A' ~ 'Z': 65 ~ 91
# arr = [chr(i) for i in range(97, 123)];
for char_i in char:
    for j in range(0,1000):
#        print char_i + "%d" % (j),
#    print
        subprocess.call('~/Dev-intern/redis-2.8.12/src/redis-cli -h 0.0.0.0 -p 10000 set ' + char_i + str(j) + ' '+char_i+str(j) ,shell=True),
    print;
