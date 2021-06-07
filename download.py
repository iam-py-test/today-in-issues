import requests
import json
import subprocess
import os
import sys
req = requests.get("https://api.github.com/repos/iam-py-test/my_filters_001/issues")
alli = json.loads(req.text)
if os.exists("today-in-issues"):
  os.chdir("today-in-issues")
  subprocess.run("git pull",shell=True)
  os.chdir("..")
else:
  subprocess.run("git clone https://github.com/iam-py-test/today-in-issues.git")
for issue in alli:
  print(issue)
