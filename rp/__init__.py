import time
import random
import GPUtil 
import psutil
import cpuinfo
import os_release
from os import environ
from pypresence import Presence

# from some random gist, i lost the link :(
def pretty_time_delta(seconds):
    sign_string = '-' if seconds < 0 else ''
    seconds = abs(int(seconds))
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    if days > 0:
        return '%s %dd %dh %dm %ds' % (sign_string, days, hours, minutes, seconds)
    elif hours > 0:
        return '%s %dh %dm %ds' % (sign_string, hours, minutes, seconds)
    elif minutes > 0:
        return '%s %dm %ds' % (sign_string, minutes, seconds)
    else:
        return '%s %ds' % (sign_string, seconds)

def main():
  client_id = '888093222457442354'
  RPC = Presence(client_id)
  RPC.connect()

  gpu = GPUtil.getGPUs()[0]
  os = os_release.current_release()
  cpu = cpuinfo.get_cpu_info()['brand_raw']
  
  while True:
    cpu_per = round(psutil.cpu_percent(), 1) 
    mem_per = round(psutil.virtual_memory().percent, 1)

    choices = [
      f"CPU: {cpu}",
      f"GPU: {gpu.name}",
      f"OS: {os.pretty_name}",
      f"Shell: {environ['SHELL']}",
      f"CPU Usage: {str(cpu_per)}%",
      f"Memory Usage: {str(mem_per)}%",
      f"Uptime: {pretty_time_delta(time.time() - psutil.boot_time())}"
    ]

    RPC.update(state=random.choice(choices))
    time.sleep(3)