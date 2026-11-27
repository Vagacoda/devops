# 방명록 DevOps 프로젝트

## 프로젝트 목표
기존 방명록 앱을 Docker와 Kubernetes로 실행하고, GitHub Actions와 Argo CD를 연결해 코드 변경이 새 이미지 배포까지 이어지는 과정을 확인했다.

## 진행 과정과 결과
1. Docker Compose로 방명록과 Redis를 실행하고 브라우저에서 동작을 확인했다.
2. Minikube에 방명록과 Redis를 배포하고 Argo CD가 GitHub의 `guestbook/k8s` 설정을 관리하도록 연결했다.
3. ConfigMap의 제목을 `202344076 방명록`, 색상을 파란색으로 바꿨다. web 복제 수는 4개에서 3개로, NodePort는 30080에서 30081로 바꿨다. PR을 `main`에 합친 뒤 Argo CD의 자동 동기화와 화면 반영을 확인했다.
4. 화면 문구를 `CI/CD`에서 `GitOps 배포`로 수정했다. GitHub Actions가 새 이미지 `ghcr.io/vagacoda/guestbook:1effe2d`를 빌드·푸시한 뒤, 배포 파일의 이미지 태그를 변경했다. Argo CD가 새 이미지를 배포했고 브라우저에서 변경된 문구를 확인했다.

## 오류와 해결
- **Redis 연결 실패:** 처음에는 한 web Pod가 Redis에 연결하지 못해 메모리 모드로 시작했다. `/readyz`가 503을 반환해 Pod가 `0/1`, Argo CD가 `Degraded`였다. 로그와 Pod 이벤트를 확인한 뒤 해당 Pod를 다시 생성했고, Redis 연결과 `Synced / Healthy` 상태를 확인했다.
- **Readiness Probe 경로 오류:** 실습을 위해 `/readyz`를 잘못된 경로로 바꿨다. 새 Pod가 `0/1`이 되었고 이벤트에서 HTTP 404를 확인했다. 경로를 `/readyz`로 되돌린 PR을 합친 뒤 web Pod 3개가 모두 `1/1 Running`, Argo CD가 `Synced / Healthy`로 복구됐다.

## 배운 점
Git에 코드가 올라가고 이미지가 만들어져도 Kubernetes가 자동으로 새 이미지를 쓰지는 않았다. 배포 파일의 이미지 태그를 Git에서 변경해야 Argo CD가 이를 감지해 배포했다. 또한 `Running`은 서비스 준비 완료와 다르므로 Pod의 준비 상태, 이벤트, 로그를 함께 확인해야 했다.

## 관련 기록
- 저장소: https://github.com/Vagacoda/devops
- 설정 변경 PR: https://github.com/Vagacoda/devops/pull/31
- Probe 오류 재현 PR: https://github.com/Vagacoda/devops/pull/32
- Probe 복구 PR: https://github.com/Vagacoda/devops/pull/33
- 화면 코드 변경 PR: https://github.com/Vagacoda/devops/pull/34

- 새 이미지 배포 PR: https://github.com/Vagacoda/devops/pull/36
