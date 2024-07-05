import speedtest
import datetime
import csv
import time

s = speedtest.Speedtest(secure = True)

with open('test.csv', mode='w', newline='') as speedcsv:
    csv_writer = csv.DictWriter(speedcsv,
                                fieldnames=['time', 'downspeed', 'upspeed'])
    csv_writer.writeheader()
    while True:
        start = time.time()
        print('iterating')
        itime = datetime.datetime.now().strftime("%H:%M:%S")
        downspeed = round((round(s.download()) / 1048576), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)
        print(downspeed)
        print(upspeed)
        csv_writer.writerow({
            'time': itime,
            'downspeed': downspeed,
            "upspeed": upspeed
        })
        speedcsv.flush()
        end = time.time()
        extra_time = 60 - (end - start)
        time.sleep(extra_time)
