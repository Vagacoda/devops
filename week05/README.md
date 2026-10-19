# 5주차: Docker 기본 사용

## 학습 내용
- 이미지와 컨테이너의 차이를 배웠다.
- hello-world 이미지로 Docker 실행을 확인했다.
- Nginx 컨테이너를 실행하고 웹 서버에 접속하는 실습을 했다.

## 주요 개념
- 이미지: 프로그램 실행에 필요한 파일과 설정을 담은 틀
- 컨테이너: 이미지를 바탕으로 만들어 실행하는 환경
- 포트 연결: 내 컴퓨터의 포트를 컨테이너 내부 포트와 연결하는 것

## 실습 명령어
~~~bash
docker --version
docker run --rm hello-world
docker run -d -p 8080:80 --name web nginx
docker ps
curl -I http://localhost:8080
~~~

`-d`는 백그라운드 실행, `--name web`은 컨테이너 이름 지정이다.
`-p 8080:80`은 내 컴퓨터의 8080번 포트를 컨테이너의 80번 포트에 연결한다.

## 정리
Docker를 사용하면 이미지를 바탕으로 필요한 프로그램을 실행할 수 있다.
실행 상태는 docker ps로 확인하고, 웹 서버의 응답은 브라우저나 curl로 확인한다.
