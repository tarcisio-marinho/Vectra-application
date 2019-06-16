import subprocess
terminal_output = subprocess.Popen("sudo ls", shell=True, stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE)
                                        
print(terminal_output.stdout.readlines())