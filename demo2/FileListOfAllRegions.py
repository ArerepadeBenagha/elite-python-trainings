import boto.ec2
regions = boto.ec2.regions()
print()
print(regions)
print(dir(regions.count))
print()
for region in regions:
    print(region.name)