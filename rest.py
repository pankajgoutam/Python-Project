from plyer import notification
import time

if __name__ == '__main__':
	    while True:
		    notification.notify(
			    title="*** Take Rest ***",
			    message="Rest is vital for better mental health, increased concentration and memory, a healthier immune system, reduced stress, improved mood and even a better metabolism.",
			    app_icon="C:/notification/clock (1)ii.ico",
				timeout=5) 
		    time.sleep(20)


