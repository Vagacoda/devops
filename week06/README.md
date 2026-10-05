# DevOps Week06 - Dockerfile

## 1. 내 Docker 이미지

- GHCR v1: ghcr.io/vagacoda/guestbook:v1
- GHCR v2: ghcr.io/vagacoda/guestbook:v2

## 2. Dockerfile 명령어

- FROM: 기반 이미지를 지정함.
- WORKDIR: 컨테이너 내부 작업 디렉터리를 지정함.
- COPY: 호스트의 파일을 이미지 내부로 복사함.
- RUN: 이미지 빌드 과정에서 명령을 실행함.
- USER: 컨테이너를 실행할 사용자를 지정함.
- ENV: 이미지의 기본 환경변수를 설정함.
- EXPOSE: 컨테이너가 사용할 포트를 문서화함.
- CMD: 컨테이너가 시작될 때 실행할 명령을 지정함.

## 3. 빌드 캐시

Dockerfile의 각 단계는 레이어로 생성됨.  
변경되지 않은 레이어는 다음 빌드에서 CACHED 상태로 재사용됨.

requirements.txt를 소스 코드보다 먼저 COPY하도록 구성하였음.  
이를 통해 소스 코드만 변경된 경우 pip install 단계의 캐시를 재사용할 수 있도록 하였음.

## 4. 환경변수 우선순위

app.py 기본값 < Dockerfile ENV < docker run -e

- app.py 기본값: 코드 내부에 기본 설정값을 지정함.
- Dockerfile ENV: 이미지 빌드 시 기본 환경변수를 설정함.
- docker run -e: 컨테이너 실행 시 환경변수를 설정하며 가장 높은 우선순위로 적용됨.

## 5. 나만의 방명록

- 제목을 `Vagacoda DevOps 방명록`으로 변경하였음.
- 테마 색상을 변경하였음.
- 입력창의 문구를 변경하였음.
- 수정된 방명록을 `guestbook:v2` 이미지로 빌드하였음.
- 생성한 이미지를 GHCR에 push하였음.

## 6. docker run -e 테스트

이미지를 재빌드하지 않고 `THEME_COLOR` 환경변수를  
`docker run -e` 옵션으로 변경하여 테마 색상이 변경되는 것을 확인하였음.
