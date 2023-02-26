mkdir redis-cluster
cd redis-cluster
mkdir 7000 7001 7002 7003 7004 7005

# create redis config files
cat >> ./7000/redis.conf << EOF
port 7000
daemonize yes
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
EOF

cat >> ./7001/redis.conf << EOF
port 7001
daemonize yes
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
EOF

cat >> ./7002/redis.conf << EOF
port 7002
daemonize yes
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
EOF

cat >> ./7003/redis.conf << EOF
port 7003
daemonize yes
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
EOF

cat >> ./7004/redis.conf << EOF
port 7004
daemonize yes
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
EOF

cat >> ./7005/redis.conf << EOF
port 7005
daemonize yes
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
EOF

# start redis servers
cd 7000 && redis-server redis.conf && cd ..
cd 7001 && redis-server redis.conf && cd ..
cd 7002 && redis-server redis.conf && cd ..
cd 7003 && redis-server redis.conf && cd ..
cd 7004 && redis-server redis.conf && cd ..
cd 7005 && redis-server redis.conf && cd ..

# create redis cluster
redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 --cluster-replicas 1 --cluster-yes
