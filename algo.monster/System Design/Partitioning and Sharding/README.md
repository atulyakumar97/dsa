Run redis on docker

```docker
docker run -p 6379:6379 -it redis/redis-stack:latest
```

```bash
cat > redis-cluster.sh
# paste content of partition_cache_setup.sh and then CTRL+C
chmod +x redis-cluster.sh
./redis-cluster.sh
```
