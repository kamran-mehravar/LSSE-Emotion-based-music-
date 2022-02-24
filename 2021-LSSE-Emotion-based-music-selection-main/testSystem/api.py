from flask import Flask, Response, flash, request, redirect, send_from_directory
import pandas as pd
from time import time
app = Flask(__name__) # always use this

N_RUNS = 2

class TimeInterval:
    def __init__(self, mode):
        self.start = 0
        self.all_sys_intervals = []*50
        self.ing_string = []*50
        self.prep_string = [] * 50
        self.devel_string = [] * 50
        self.exe_string = [] * 50
        self.counter = 0
        self.next_time = 0
        self.ingestion_time = 0
        self.prep_time = 0
        self.devel_time = 0
        self.exe_time = 0
        self.mode = mode ## 0 Development, 1 Monitoring

    def save_test(self):
        file = open("time_report.txt", "w")
        file.write("SYSTEM RESPONSE TIME REPORT\n\n")
        tot_avg = 0
        ing_avg = 0
        prep_avg = 0
        devel_avg = 0
        exe_avg = 0
        for n in range(N_RUNS):
            file.write("The Segregation time is added to Development system time\n\n")
            file.write("Test " + str(n) + "\n")
            file.write("Total System Time: " + str(round(self.all_sys_intervals[n], 1)) + "s\n")
            tot_avg += self.all_sys_intervals[n]
            file.write("Ingestion Time:   " + str(round(self.ing_string[n], 1)) + "s\n")
            ing_avg += self.ing_string[n]
            file.write("Preparation Time: " + str(round(self.prep_string[n], 1)) + "s\n")
            prep_avg += self.prep_string[n]
            file.write("Development Time: " + str(round(self.devel_string[n], 1)) + "s\n")
            devel_avg += self.devel_string[n]
            file.write("Execution Time:   " + str(round(self.exe_string[n], 1)) + "s\n")
            exe_avg += self.exe_string[n]
        file.write("\nAverage Times for the Test Session - Samples Taken: " + str(N_RUNS) + "\n")
        file.write("Total System Time: " + str(round(tot_avg/N_RUNS, 1)) + "s\n")
        file.write("Ingestion:   " + str(round(ing_avg / N_RUNS, 1)) + "s\n")
        file.write("Preparation: " + str(round(prep_avg / N_RUNS, 1)) + "s\n")
        file.write("Development: " + str(round(devel_avg / N_RUNS, 1)) + "s\n")
        file.write("Execution:   " + str(round(exe_avg / N_RUNS, 1)) + "s\n")
        file.close()

    def get_mode(self):
        return self.mode

    def set_start(self, time):
        self.start = time

    def get_start(self):
        return self.start

    def set_parse(self, time):
        self.next_time = time

    def get_parse(self):
        return self.next_time

    def set_ingestion_time(self, time):
        self.ingestion_time = time

    def set_prep_time(self, time):
        self.prep_time = time

    def set_devel_time(self, time):
        self.devel_time = time

    def set_exe_time(self, time):
        self.exe_time = time

    def set_monitoring_time(self, time):
        self.monitoring_time = time

    def set_all_interval(self, interval):
        if self.counter < N_RUNS:
            self.all_sys_intervals.append(interval)
            self.ing_string.append(self.ingestion_time)
            self.prep_string.append(self.prep_time)
            self.devel_string.append(self.devel_time)
            self.exe_string.append(self.exe_time)
            print("Data: ", self.all_sys_intervals, "\nRun: ", self.counter)
            self.counter += 1
            if self.counter == N_RUNS:
                self.save_test()


@app.route("/testend", methods=['GET', 'POST'])
def test1():
    if request.method == 'GET':
        start_time = time()
        ti.set_start(start_time)
        print("\nNEW MONITORING/DEVEL TEST")
        #print("Start Time: ", round(ti.get_start(), 1))
    return Response("<h1Start Time Monitoring</h1>",status=200, mimetype='text/html')

@app.route("/testend/mon", methods=['GET', 'POST'])
def test2():
    if request.method == 'POST':
        end_time = time()
        interval = end_time - ti.get_start()
        print("\nTOTAL SYSTEM TIME (MONITORING MODE)", round(interval, 1))
        ti.set_all_interval(interval)

    return Response("<h1>Monitoring time ok</h1>",status=200, mimetype='text/html')

@app.route("/testend/exe", methods=['GET', 'POST'])
def test3():
    if request.method == 'POST' and ti.get_mode() == 0:
        t = ti.get_parse()
        exe_time = time() - t
        ti.set_exe_time(exe_time)
        end_time = time()
        interval = end_time - ti.get_start()
        print("\nExecution Time", round(exe_time, 1))
        print("\nTOTAL SYSTEM TIME (DEVEL MODE)", round(interval, 1))
        ti.set_all_interval(interval)
    return Response("<h1>Execution time ok</h1>",status=200, mimetype='text/html')

@app.route("/testend/dev", methods=['GET', 'POST'])
def test4():
    if request.method == 'POST' and ti.get_mode() == 0:
        t = ti.get_parse()
        dev_time = time() - t
        ti.set_parse(time())
        ti.set_devel_time(dev_time)
        print("\nDevel Time: ", round(dev_time, 1))
    return Response("<h1>PREPARATION SYSTEM OK</h1>",status=200, mimetype='text/html')

@app.route("/testend/pre", methods=['GET', 'POST'])
def test5():
    if request.method == 'POST' and ti.get_mode() == 0:
        t = ti.get_parse()
        prep_time = time() - t
        ti.set_parse(time())
        ti.set_prep_time(prep_time)
        print("\nPreparation Time: ", round(prep_time, 1))
    return Response("<h1>Preparation time ok</h1>",status=200, mimetype='text/html')

@app.route("/testend/ing", methods=['GET', 'POST'])
def test6():
    if request.method == 'POST' and ti.get_mode() == 0:
        t = ti.get_start()
        ing_time = time() - t
        ti.set_parse(time())
        ti.set_ingestion_time(ing_time)
        print("\nIngestion Time: ", round(ing_time, 1))
    return Response("<h1>Ingestion time ok</h1>",status=200, mimetype='text/html')

ti = TimeInterval(1) # 0 Devel, 1 Monitoring
app.run(port=5009)


