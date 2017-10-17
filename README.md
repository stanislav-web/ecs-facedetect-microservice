### ECS-FACEDETECT-MICROSERVICE
_(SimpleHTTPServer as Foreground, Python Flask, MongoDb as main repository)_

[![Build Status](https://travis-ci.org/stanislav-web/ecs-facedetect-microservice.svg?branch=master)](https://travis-ci.org/stanislav-web/ecs-facedetect-microservice/builds/286316998) [![Coverage Status](https://coveralls.io/repos/github/stanislav-web/ecs-facedetect-microservice/badge.svg?branch=master)](https://coveralls.io/github/stanislav-web/ecs-facedetect-microservice?branch=master) [![GitHub license](https://img.shields.io/badge/license-AGPL-blue.svg)](https://raw.githubusercontent.com/stanislav-web/ecs-facedetect-microservice/master/LICENSE)


This assemblage implements REST images upload storage with face recognition.

![Nginx](https://images.sftcdn.net/images/t_optimized,f_auto/p/6dd52663-2bbf-48e0-a7cc-cdb043b326ef/1544311950/nginx-logo.png) &rightarrow; ![Python](http://crowdtest.org/img/test-icons/python.png) &rightarrow; ![Flask](http://python-cloud.com/img/128px/flask.png) &rightarrow; ![OpenResty Lua](https://keplerproject.github.io/wsapi/wsapi.png)
##### IMPLEMENTS
 - Nginx OpenResty as Background Proxy for Validate JWT
 - Python 3.6 Built-in WEB Server
 - PIL (Python Image Library)
 - Flask microframework for REST API
 
##### INSTALL

```bash
docker-compose up --build
```

##### RUN
```bash
POST http://localhost:88
```

##### CHECK MICROSERVICE STATUS
`http://localhost:88/status/`

```python
HTTP/1.1 200 OK
{
     "status": 200,
     "message": {
         "now":"01:52:51 GMT+0300 (EEST)",
         "revision":"62b1b88ef48bb3fe859b2bd374e64576f79e6cca",
         "version":"v1.1.2",
         "residentSet":"49.8 MB",
         "totalHeap":"30.4 MB",
         "usedHeap":"16.8 MB",
         "uptime":22.969
     }
 }
```