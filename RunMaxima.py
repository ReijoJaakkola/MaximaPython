import subprocess

#Insert path here to maxima.bat
cmd = []

#TODO: Determine buffer size.
process = subprocess.Popen(cmd, 4096, stdout=subprocess.PIPE)

#TODO: Communication without using shell.
output = process.communicate()

print(output)