[clusters]
falco =
    ec2-52-16-208-252.eu-west-1.compute.amazonaws.com:8091
#    ec2-52-16-210-108.eu-west-1.compute.amazonaws.com:8091

[clients]
hosts =
    ec2-52-16-74-61.eu-west-1.compute.amazonaws.com
credentials = root:couchbase

[storage]
data = /data
index = /data

[credentials]
rest = Administrator:password
ssh = root:couchbase

[parameters]
Platform = AWS r3.4xl
OS = CentOS 6.6
CPU = 16 vCPU
Memory = 128 GB
Disk = Unknown
