import json
f=open("t.json")
j=json.load(f)
print(j)
print(j.resource.aws_instance.web.ami)
