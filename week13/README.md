# Week 13 - GitOps

## GitOps와 Argo CD
- Git에 원하는 Kubernetes 상태를 기록한다.
- Argo CD가 Git과 클러스터 상태를 비교하고 동기화한다.
- guestbook Application이 Synced, Healthy인 것을 확인했다.

## 실습 결과
- Git의 replicas를 4에서 2로 바꾸고 PR을 병합하자 Pod가 2개로 줄었다.
- kubectl로 replicas를 4로 바꾸자 self-heal이 Git의 2개로 되돌렸다.
- git revert를 PR로 병합해 replicas를 다시 4개로 복구했다.
- hello ConfigMap을 Git에 추가하자 자동 생성됐다.
- Git에서 hello.yaml을 삭제하자 prune으로 ConfigMap이 삭제됐다.
- 코드 변경 후 GitHub Actions가 이미지를 만들었다.
- 배포 YAML에 이미지 태그 057b46f를 기록하자 Argo CD가 자동 배포했다.
- 브라우저에서 CI/CD 제목과 Redis 연결을 확인했다.

## 모니터링
- metrics-server를 켜고 kubectl top pods로 CPU와 메모리를 확인했다.
- 메트릭은 시간에 따른 숫자, 로그는 발생한 사건의 기록이다.
