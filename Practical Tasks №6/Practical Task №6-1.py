import time
class TrafficLight():
    color = 0
    def running(self):
        while True:
            print('Red')
            time.sleep(7)
            print('Yellow')
            time.sleep(2)
            print('Green')
            time.sleep(10)

traffic_light = TrafficLight()
traffic_light.running()
