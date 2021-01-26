
# 도커 오케스트레이션 컨테이너 분리(DOCKER SWARM)

개념도 )

요청이 들어오면 매니저 노드를 통해서 각 워커 노드로 명령을 실행 

각 워커들은 컨테이너를 생성 실행 

![image-20210126165456279](C:\Users\lodics\AppData\Roaming\Typora\typora-user-images\image-20210126165456279.png)







실행 방법 

매니저 노드역활을 할 서버에 

```N
docker swarm init --advertise-addr ip4
```

출력 값으로 키 값이 나옴 

ex) 

```
docker swarm join --token  SWMTKN-1-4qnkzyig831ezxo4f84so53a71h5spvl5yisnyrbhpqiuzlaor-1st57o8wk
```

출력값을 워커노드에  입력

-- 클러스터 생성 

매니저 노드에서

```
docker stack deploy -c {도커컴퍼즈 파일} {스택명 }
```

해당 명령 수행 ) 매니저노드상에서 스택을 배포 ( 해당 명령시 스웜이 도커컴퍼즈 내에 있는 컨테이너를  적절하게  배분해줌  )

직접 설정할 려고 할 시 docker-compose에 deploy 옵션 추가 



ex)  정적으로 워커,매니저 노드에 할당함 

```yaml
version: '3.7'

services:
    web:
        image: wiss-module
        container_name: wiss-module-core      
        deploy:
            placement:
                constraints: [node.hostname == 153.lodics]
        volumes:
            - upload-data:/src/wiss/wiss/www/static/uploads
            - ./datadrive:/datadrive
            - ./wiss:/src/wiss/wiss
        command: wiss webserver -d
        ports:
            - 8000:8000
        deploy:
            placement:
              constraints: [node.role == 153.lodics]
    db:
        image: wiss-postgis
        container_name: wiss-db
        environment: 
            - POSTGRES_USER=wissuser
            - POSTGRES_PASSWORD=wiss2020
            - POSTGRES_MULTIPLE_DATABASES=wiss,test
        deploy:
            placement:
                constraints: [node.role == manager]
        volumes:
            - wiss-db:/var/lib/postgresql/data
        ports:
            - 5432:5432
    mq:
        image: rabbitmq
        container_name: wiss-mq
        deploy:
            placement:
                constraints: [node.hostname == 153.lodics]
        environment:
            - RABBITMQ_DEFAULT_USER=wiss
            - RABBITMQ_DEFAULT_PASS=mq2020
    worker:
        image: wiss-module
        container_name: wiss-module-worker
        depends_on:
            - mq
        deploy:
            placement:
                constraints: [node.hostname == 153.lodics]
        volumes:
            - ./datadrive:/datadrive
            - ./wiss:/src/wiss/wiss
        command: celery worker -A wiss -l info -n worker@%h
    scheduler:
        image: wiss-module
        container_name: wiss-module-scheduler
        depends_on:
            - mq
        deploy:
            placement:
                constraints: [node.hostname == 153.lodics]
        volumes:
            - ./wiss:/src/wiss/wiss
        command: celery beat -A wiss -l info
    geoserver:
        image: wiss-geoserver:2.17.2
        container_name: wiss-geoserver
        volumes:
            - geoserver-data:/opt/geoserver/data_dir
        ports:
            - "8080:8080"
        deploy:
            placement:
                constraints: [node.role == manager]
        env_file:
            - docker/env/geoserver.env
    visualizer:
        image: dockersamples/visualizer:stable
        ports:
          - "9999:8080"
        volumes:
          - "/var/run/docker.sock:/var/run/docker.sock"
        deploy:
            placement:
                constraints: [node.role == manager]
    front:
        image: next-wiss:2.0
        deploy:
            placement:
                constraints: [node.rolde == manager]
        ports:
         - "3000:3000"
volumes:
    wiss-db:
    geoserver-data:
    upload-data:
    visualizer:

```



152번을 매니저 노드 겸 워커 노드로 설정

64,153번을 워커 노드로 설정 64번 (네트워크 설정 문제 진행중 )





![image-20210126175742079](C:\Users\lodics\AppData\Roaming\Typora\typora-user-images\image-20210126175742079.png)
