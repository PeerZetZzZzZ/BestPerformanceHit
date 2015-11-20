#!/usr/bin/env python

import subprocess

class ReaderAndParser:

    hostmaps = {}

    def read(self, list_host, resource_to_download):
         i = 0
         print(list_host)
         while i < len(list_host):
             print(list_host[i])
             self.save_to_file(self.__run_traceroute_paris_for_host(list_host[i], resource_to_download), list_host[i])
             i += 1

    def __run_traceroute_paris_for_host(self, host_address, resource_to_download):
        main_list = []
        traceroute = subprocess.Popen(["paris-traceroute " + host_address + "/" + resource_to_download], stdout=subprocess.PIPE, shell=True)
        out = traceroute.stdout.read()
        words = out.split()
        main_list.extend(self.parse(words))
        main_list.append('\n')
        print(main_list)
        return main_list

    def parse(self, words):
        i = 0
        n = 1
        li = []
        while i < len(words):
            if words[i].decode("utf-8") == str(n):
                li.append(words[i + 2].decode("utf-8"))
                li.append(words[i + 3].decode("utf-8"))
                self.hostmaps[words[i + 2].decode("utf-8")] = words[i + 3].decode("utf-8")
                n += 1
            i += 1
        print(li)
        return li

    def save_to_file(self, data, single_host):
        print(single_host)
        f = open("{}.txt".format(single_host[: -1]), 'w')
        f.write(" ".join(str(x) for x in data))
        f.close()

    def getHostFromPosition(self, position):
        print("getHostFromPosition")
        print(self.hostmaps.keys()[position])
        return self.hostmaps.keys()[position]

    def getTimeToHost(self, position):
        print("getTimeToHost")
        print(self.hostmaps.values()[position])
        return self.hostmaps.values()[position]

    def getFullPathTime(self):
        print("getFullPathTime")
        print(self.hostmaps.values()[len(self.hostmaps)-1])
        return self.hostmaps.values()[len(self.hostmaps)-1]

    def getSizeOfMap(self):
        print("getSizeOfMap")
        print(len(self.hostmaps))
        return len(self.hostmaps)
