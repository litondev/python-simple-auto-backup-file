from shutil import copyfile
import datetime,os
from dotenv import load_dotenv

load_dotenv()

class the_log_app:
	# get main folder pwd
	folder = os.getcwd()	

	# list file logs
	list_file_logs = []

	# name folder python logs
	folder_python_logs = os.getenv("FOLDER_PYTHON_LOGS")

	# name folder backup inside folder_python_logs
	folder_backup = ""

	# name folder lows
	folder_logs = os.getenv("FOLDER_LOGS")

	# logs folder pwd
	folder_logs_pwd = os.getenv("FOLDER_LOGS_PWD") or os.getcwd()

	def __init__(self):
		# make folder depend on time
		now_str = datetime.datetime.now().strftime('%Y-%m-%d %H-%M')

		self.folder_backup = self.folder + self.folder_python_logs + now_str

		print("Folder Created") if os.path.isdir(self.folder_backup) else os.mkdir(self.folder_backup)

		# make list file from folder logs		
		for item_log in os.scandir(self.folder_logs_pwd + self.folder_logs):			
			self.list_file_logs.append(item_log.name) if item_log.is_file() else print("Is Not File")	

	def _send_mail(self,name,the_file):
		# send mail
		print("Sended : " + name)
		
	def _delete_log(self,name,the_file):		
		os.unlink(the_file) if os.path.isfile(the_file) else print("File : " + name + " Tidak Ditemukan")	
		print("Deleted : " + name)

	def _copy_log(self,name,the_file):
		# copyfile(the_file,self.folder_backup)
		print("Copyed : " + name)	

	def do_schedule(self):
		for item_log in self.list_file_logs:				
			the_file = self.folder_logs_pwd + self.folder_logs + item_log

			self._copy_log(item_log,the_file)

			self._delete_log(item_log,the_file)

			self._send_mail(item_log,the_file)	
		else:
			print("Done")