import gearman
import time

gm_worker = gearman.GearmanWorker(['localhost:4730'])

def task_listener_reverse(gearman_worker, gearman_job):
    print 'Reversing string: ' + gearman_job.data
    return gearman_job.data[::-1]


def task_listener_append(gearman_worker, gearman_job):
    print 'Append string: ' + gearman_job.data
    time.sleep(3)  #do some hard work
    return gearman_job.data + 'append message by gearman'

# gm_worker.set_client_id is optional
gm_worker.set_client_id('python-worker')
#gm_worker.register_task('reverse', task_listener_append)
gm_worker.register_task('reverse', task_listener_reverse)
#gm_worker.register_task('append', task_listener_append)
gm_worker.register_task('append', task_listener_append2)

# Enter our work loop and call gm_worker.after_poll() after each time we timeout/see socket activity
gm_worker.work()
