#!/usr/bin/env python

import os
import sys
import subprocess
import readerandparser
# import geolocal

class BestPerformanceHit:

    def process_file(self, input_file, resource_to_download):
        while True:
            single_host = input_file.readline()
            if len(single_host) == 0:
                sys.exit()
            else:
                # self.__run_traceroute_paris_for_host(single_host, resource_to_download)

                list_host = single_host.split()
                reader = readerandparser.ReaderAndParser()
                reader.read(list_host, resource_to_download)
                reader.getHostFromPosition(6)
                reader.getTimeToHost(6)
                reader.getFullPathTime()
                reader.getSizeOfList()

                # geo = geolocal.GeoLocal()



    # Params:
    # host_address - address of the host where resource to download is located
    # resource_to_download - name of resource to download which should be located under host_address/resource_to_download
    # def __run_traceroute_paris_for_host(self, host_address, resource_to_download):
    #     traceroute_command = "{} {}".format("paris-traceroute", host_address).strip()
    #     traceroute_process= subprocess.Popen(traceroute_command, stdout=subprocess.PIPE, shell=True)
    #     traceroute_output = traceroute_process.stdout.read()
    #     print(traceroute_output)
    #     print(resource_to_download)
        #############################  PART 1  ##################################################################
        # Here is the place where traceroute_output should be processed and where appropriate object with data
        # should be returned
        # I see it as a class where are methods like
        # getHostFromPosition(0) - returns me first host on the path
        # getTimeToHost(0) - returns me the time which elapsed while
        # getFullPathTime() - returns the full time which was needed to go throw the whole path
        #########################################################################################################

        #############################  PART 2  ##################################################################
        # Here is the place for second part where having data delivered by upper object
        # there should be provided class which will return information about localization of this ip addresses
        # I think there might be returned something like city/country
        # but what we really need is distance in KM/m from the place where we are to decided which servers are closer
        #########################################################################################################


        #############################  PART 3  ##################################################################
        # At this point we have:
        # - time which was needed to access given endnode (server where we have desired resource)
        # - distance from point where we are do endnode (server where we have desired resource)
        #
        # Now is the point where having this data we should decide which of these servers is the best to download
        # resource. I think we should do the measurements regulary - let's say every 1 minute we make test and
        # live results should be printed
        #########################################################################################################


# This is outside the class
if len(sys.argv) < 3:
    print("BestPerformanceHit")
    print("Usage example: ./bestperformancehit.py servers.txt song.mp3")
    print("Paramaters: file.txt - input file where hosts which addresses are defined (in every line single address)")
    print("Paramaters: resource_name - resource name to download")
    sys.exit()

hosts_input_file_name = str(sys.argv[1])
if not hosts_input_file_name.endswith('.txt'):
    print("Input file must have '.txt' extension!")
    sys.exit()
hosts_input_file = open(hosts_input_file_name, 'r')

resource_to_download = str(sys.argv[2])
if resource_to_download is None:
    print("Resource name to download was not defined!")
    sys.exit()


k = BestPerformanceHit()
k.process_file(hosts_input_file, resource_to_download)