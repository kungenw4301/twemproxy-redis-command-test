##redis-command competability 
try to get if the redis command behave differently between single instance redis-server and twemproxy using redis-py

---

####Test Environment

|Module|Version|
|----------|------------|
|redis|2.8.12|
|twemproxy|0.3.0|
|python|2.7.5|
|redis-py|2.10.3|
|hiredis|0.1.4|


####Note

|Instance|Port|
|--------|-------|
|twemproxy| 6379|
|redis-server-1|6380|
|redis-server-2|6381|
|redis-server-3|6382|
|redis-server-4|6383|
|single redis instance|6384|


+ Most of the commands was tested by the code in command_test.py
