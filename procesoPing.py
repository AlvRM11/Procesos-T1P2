import subprocess

try:
    pingText = subprocess.getoutput(['ping -c 4 www.google.com']).split('\n')
    pingText = pingText[len(pingText) - 2].split(', ')

    print("\nPing Results:\n")

    for element in pingText:
        print(element)

except subprocess.CalledProcessError as e:
    print(e.output)