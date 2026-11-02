# DevOps 10주차 — Kubernetes 배포와 서비스

## 1. 학습 목표
- Deployment, ReplicaSet, Pod의 구조 이해
- YAML을 이용한 선언형 배포
- Service를 통한 로드밸런싱
- Pod 자동 복구, 스케일링, 롤링 업데이트 및 롤백 실습

## 2. 핵심 개념

| 개념 | 설명 |
|---|---|
| Deployment | Pod의 개수, 이미지 버전, 배포 상태 관리 |
| ReplicaSet | 지정된 Pod 개수 유지 |
| Pod | 컨테이너가 실행되는 최소 배포 단위 |
| Service | 여러 Pod에 요청을 전달하는 고정 접속 창구 |
| Label / Selector | 레이블을 기준으로 Pod를 선택하고 연결 |
| Rolling Update | 서비스 중단을 최소화하며 순차적으로 버전 교체 |
| Rollback | 이전 배포 버전으로 복구 |

## 3. 주요 명령어

```bash
# 클러스터 실행 및 확인
minikube start --driver=docker
kubectl get nodes

# YAML 배포
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# 상태 확인
kubectl get deployments
kubectl get replicasets
kubectl get pods
kubectl get svc

# Pod 자동 복구 확인
kubectl delete pod <Pod이름>
kubectl get pods -w

# 스케일링
kubectl scale deployment guestbook --replicas=5

# 서비스 접속
kubectl port-forward svc/guestbook 8080:80

# 롤링 업데이트
kubectl set image deployment/guestbook web=ghcr.io/vagacoda/guestbook:v2
kubectl rollout status deployment/guestbook

# 롤백
kubectl rollout history deployment/guestbook
kubectl rollout undo deployment/guestbook
```

## 4. 실습 과정 및 결과

1. Minikube 클러스터 실행 및 Node Ready 확인
2. `deployment.yaml` 적용 → Pod 2개 생성
3. Pod 하나 삭제 → 새로운 Pod 자동 생성 확인
4. `service.yaml` 적용 → NodePort 30080 설정 및 브라우저 접속
5. Pod 개수를 2개 → 3개 → 5개로 확장
6. Service 요청에서 서로 다른 Pod hostname 확인 → 로드밸런싱 성공
7. Docker 이미지 v2 빌드 후 Minikube에 직접 로드
8. v1 → v2 롤링 업데이트 및 v2 → v1 롤백 성공

## 5. 실습 결과 및 느낀 점

Kubernetes의 Deployment와 Service를 사용하여 컨테이너를 배포하고 관리하였다. Pod 삭제 시 자동 복구되는 동작을 확인했으며, 스케일링과 로드밸런싱을 통해 여러 Pod가 요청을 처리하는 과정도 확인하였다.

또한 롤링 업데이트와 롤백을 실습하면서 서비스 운영 중 버전 변경과 복구가 가능한 구조를 이해하였다.

**실습 결과:** Deployment, Service, 자가 치유, 스케일링, 로드밸런싱, 롤링 업데이트 및 롤백 모두 성공.
