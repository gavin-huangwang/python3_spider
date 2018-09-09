TESTER_CYCLE = 20
GETTER_CYCLE = 20
TEST_QIYONG = True
GETTER_QIYONG = True
API_QIYONG = True

from multiprocessing import Process
from test_proxy import Tester
from getter_save_db import Getter
from api import app
import time

class Schedler():
	def schedule_tester(self,cycle=TESTER_CYCLE):
		tester = Tester()
		while True:
			tester.run()
			time.sleep(cycle)
	
	def schedule_getter(self,cycle=GETTER_CYCLE):
		getter = Getter()
		while True:
			getter.run()
			time.sleep(cycle)
			
	def schedule_api(self):
		app.run(API_HOST, API_PORT)	
		
	def run(self):
		if TEST_QIYONG:
			tester_process = Process(target=self.schedule_tester)
			tester_process.start()
		
		if GETTER_QIYONG:
			getter_process = Process(target=self.schedule_getter)
			getter_process.start()
			
		if API_QIYONG:
			api_process = Process(target=self.schedule_api)
			api_process.start()	
