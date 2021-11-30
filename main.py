import sys
from log_app import the_log_app,the_app,the_backup_database

# exit if not in main 
if __name__ != "__main__":	
	sys.exit()

# exit if does not have 2 value
sys.exit() if 2 > len(sys.argv) else print('Continue Request . . .')

# search app
if sys.argv[1] == "app" :
	print('App Ready')

	app = the_app();app.begin()

elif sys.argv[1] == "log":
	log = the_log_app();log.do_schedule()	

elif sys.argv[1] == "backup_database":
    backup_database = the_backup_database();backup_database.do_backup()

else:
	print('Your App Not found')