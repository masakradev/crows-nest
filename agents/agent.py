import shutil

import requests


def df():
    freeGiB = round(shutil.disk_usage('/home').free / 1024 ** 3)

    if freeGiB < 50:
        status = 'Error'
    else:
        status = 'OK'

    status = 'Error'
    r = requests.post('http://127.0.0.1:5000/report',
                      json={"server_name": 'rademenes', "agent": 'df', "status": status, "desc": '/home ' + str(freeGiB) + ' GiB'})
    print(r.status_code)


if '__main__' == __name__:
    df()
    pass