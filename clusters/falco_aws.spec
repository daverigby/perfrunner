[clusters]
falco =
    ec2-52-74-29-53.ap-southeast-1.compute.amazonaws.com:8091

#    ec2-52-74-0-228.ap-southeast-1.compute.amazonaws.com:8091

[clients]
hosts =
    ec2-52-74-34-149.ap-southeast-1.compute.amazonaws.com
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
