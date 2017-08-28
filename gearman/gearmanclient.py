import gearman

def check_request_status(job_request):
    if job_request.complete:
        print "Job %s finished!  Result: %s - %s" % (job_request.job.unique, job_request.state, job_request.result)
    elif job_request.timed_out:
        print "Job %s timed out!" % job_request.unique
    elif job_request.state == JOB_UNKNOWN:
        print "Job %s connection failed!" % job_request.unique

gm_client = gearman.GearmanClient(['localhost:4730'])

for i in range(3):
    job1 = gm_client.submit_job('append','hello world'+i)
    job2 = gm_client.submit_job('reverse','hello'+i)
    check_request_status(job1)
    check_request_status(job2)
