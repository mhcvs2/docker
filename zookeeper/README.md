https://cr.console.aliyun.com/?spm=5176.1971733.2.28.D928o9#/dockerImage/67336/versions

1. run standlone

docker run zookeeper:3.5.2

2. run cluster

docker-compose.yml <br>
docker-compose -p test up -d

3. search volume

docker inspect -f '{{range $mount := .Mounts}}{{if eq "/data" $mount.Destination}}{{$mount.Source}}{{end}}{{end}}' 139

docker inspect -f '{{range $mount := .Mounts}}{{if eq "/datalog" $mount.Destination}}{{$mount.Source}}{{end}}{{end}}' 139