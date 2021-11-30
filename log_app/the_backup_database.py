import os
import time
import datetime
import pipes
import smtplib
from email.message import EmailMessage

DB_HOST = 'localhost' 
DB_USER = 'root'
DB_USER_PASSWORD = 'root'
#DB_NAME = '/backup/dbnameslist.txt'
DB_NAME = 'role_laravel'
BACKUP_PATH = './backup'

# Getting current DateTime to create the separate backup folder like "20180817-123433".
DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME


# Checking if backup folder already exists or not. If not exists will create it.
try:
    os.stat(TODAYBACKUPPATH)
except:
    os.mkdir(TODAYBACKUPPATH)

class the_backup_database:
    def _send_mail(self):
        msg = EmailMessage()
        msg.set_content("Content")
        msg['Subject'] = f'The contents of '
        msg['From'] = "noreply@gmail.com"
        msg['To'] = "test@gmail.com"

     
        try:
            with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:        
                server.login("75999957ca7383", "95a016b68c6448")
                server.send_message(msg)
                server.quit()
                # server.sendmail(sender, receiver, message)
                # print(server)
                print("done send mail")
        except SMTPException:
            print("Terjadi Kesalahan")
        print("done")
    def do_backup(self):
        db = DB_NAME
        dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
        os.system(dumpcmd)
        self._send_mail()
        # zip
        # gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
        #os.system(gzipcmd)