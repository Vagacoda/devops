# 7주차: Docker Compose

## 학습 내용
- Compose 파일에 여러 컨테이너의 실행 설정을 작성했다.
- 방명록 서비스를 web, Redis, Nginx로 나누어 구성했다.
- 볼륨, 상태 확인, 컨테이너 수 조절 방법을 배웠다.

## 서비스 구성
- web: 방명록 애플리케이션 실행
- Redis: 방명록 데이터 저장
- Nginx: 외부 요청을 받아 web으로 전달

## 주요 명령어
~~~bash
docker compose up -d
docker compose ps
docker compose logs web
docker compose up -d --scale web=3
docker compose down
~~~

## 주요 개념
- 볼륨: 컨테이너가 삭제되어도 데이터를 보관하기 위해 사용한다.
- healthcheck: 서비스가 정상적으로 응답하는지 확인한다.
- depends_on: 서비스 간 실행 순서를 설정한다.
  service_healthy 조건을 사용하면 의존 서비스가 정상 상태가 될 때까지 기다린다.
- scale: 같은 서비스의 컨테이너를 여러 개 실행한다.

## 정리
Compose를 사용하면 여러 서비스를 하나의 설정 파일로 관리할 수 있다.
web을 3개로 실행할 수 있지만, 이후에도 정상 실행 개수를 3개로 유지하려면
상태를 확인하고 복구하는 방법이 추가로 필요하다.
