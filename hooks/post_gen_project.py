import subprocess

subprocess.call(["make", "install"])
subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", "Initial commit", "--no-verify"])
subprocess.call(["pre-commit", "install"])
