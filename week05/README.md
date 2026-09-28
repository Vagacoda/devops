cd ~/devops/week05
docker --version > docker-version.txt
docker info > docker-info.txt
docker run --rm hello-world > docker-run-hello-world.txt
docker run -d -p 8080:80 --name web nginx
curl -I http://localhost:8080 > curl-result.txt
docker ps > docker-ps.txt
