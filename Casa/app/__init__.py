from flask import Flask
from flask_apscheduler import APScheduler
from time import sleep
from app.config import *


scheduler = APScheduler()

@scheduler.task('interval', id='refresh_values', seconds=1, misfire_grace_time=100)
def refresh_values():
    for slave in slaves:
        slave.simulate()

# @scheduler.task('interval', id='do_job_2', seconds=5, misfire_grace_time=100)
# def job2():
#     print('Pause Job 1')
#     scheduler.pause_job('do_job_1')

#     sleep(3)

#     print('Restart Job 1')
#     scheduler.resume_job('do_job_1')


app = Flask(__name__)
app.config.from_object(Config())
from app import routes

scheduler.init_app(app)
scheduler.start()

if __name__ == "__main__":
    app.run()
