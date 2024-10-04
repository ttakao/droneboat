import requests 
import time 
import json 
import threading 
GOPRO_BASE_URL = "http://10.5.5.9:8080/" 

def request_cmd(cmd):
	response = requests.get(GOPRO_BASE_URL+cmd, timeout=10) 
	response.raise_for_status() 
	resp = response.json() 
	print( json.dumps(resp) ) 
	
def request_alive(): 
	while True: 
		resp = requests.get(GOPRO_BASE_URL+"/gopro/camera/keep_alive") 
		resp = resp.json() 
		print("Keep Alive") 
		time.sleep(3) 
		
if __name__ == '__main__': 
	thread_A = threading.Thread(target=request_alive) 
	thread_A.start() 
	# photo mode. 
	request_cmd("/gopro/camera/presets/set_group?id=1001") 
	time.sleep(10) 
	request_cmd("/gopro/camera/shutter/start") # push shutter
	time.sleep(3) 
	# request_cmd("/gopro/camera/shutter/stop") # release 
	
	thread_A.join() # wait until thread_A