# Week 11 - 쿠버네티스 설정과 상태 점검

## ConfigMap과 Secret
- ConfigMap으로 APP_TITLE, THEME_COLOR, REDIS_HOST, REDIS_PORT를 관리했다.
- Secret으로 Redis 비밀번호를 관리했다.
- Secret의 data는 base64 인코딩이며 암호화가 아니다.
- 실제 secret.yaml은 .gitignore로 제외하고 secret.yaml.example에는 CHANGE_ME를 넣었다.

## Redis와 환경변수
- Redis Deployment 1개와 ClusterIP Service를 배포했다.
- guestbook에 envFrom으로 ConfigMap과 Secret을 주입했다.
- Redis 연결 성공 로그를 확인했다.
- guestbook을 4개 Pod로 확장해도 Redis를 공유하므로 글이 유지됐다.

## 자원 제한
- requests: CPU 100m, Memory 64Mi
- limits: CPU 500m, Memory 128Mi
- 메모리 limit 초과 시 OOMKilled가 발생할 수 있다.

## ConfigMap 변경
- 제목을 New 방명록 (k8s), 색상을 #e11d48로 변경했다.
- rollout restart로 새 Pod에 환경변수를 적용했다.
- 이미지를 다시 빌드하지 않고 화면 설정을 변경했다.

## Probe 실험
- livenessProbe는 /healthz를 검사하며 실패하면 컨테이너를 재시작한다.
- readinessProbe는 /readyz를 검사하며 실패하면 Service 요청 대상에서 제외한다.
- Redis를 0개로 축소하자 /readyz가 503을 반환하고 guestbook이 0/1 Running이 됐다.
- Redis를 복구하자 guestbook이 자동으로 1/1 Running으로 회복했다.
- liveness 경로를 /devops로 잘못 설정하자 404로 실패했고 RESTARTS가 5까지 증가했다.
- deployment.yaml을 다시 apply하여 /healthz 설정으로 원복했다.

## 트러블슈팅 3단 루틴
1. kubectl get pods
2. kubectl describe pod <Pod이름>
3. kubectl logs <Pod이름>

CrashLoopBackOff일 때는 kubectl logs <Pod이름> --previous를 사용한다.

## 최종 상태
- guestbook: 4개 Pod 모두 1/1 Running
- redis: 1개 Pod 1/1 Running
- 방명록은 Redis를 공유 저장소로 사용한다.
