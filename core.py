from time import time

class Timer():
    def __init__(self, * args):
        self.timers = {}
        for item in args:
            self.timers.update({item:0})
        self.records = []

    def start(self,name):
        self.records.append([name,time()])
        return len(self.records) - 1

    def end(self,idx):
        name,start_time = self.records[idx]
        time_cost = time() - start_time
        self.timers[name] = self.timers[name] + time_cost
        return time_cost

    def output(self):
        for name in self.timers:
            print(name,'time:',self.timers[name],'s')
        return self.timers

    def add(self,name,x):
        self.timers[name] = self.timers[name] + x
        return self.timers[name]
