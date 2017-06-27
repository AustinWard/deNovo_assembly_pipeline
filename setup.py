#!/usr/bin/python
import sys
import os

genome_count = 0

if len(sys.argv) is not 2:
    print "Invalid input! Config is the only file accepted"

else:
    config_file = file.read(sys.argv[1])
    for line in config_file:
        if line is not "" or line[0] is not "#":
            line_split = line.split("=")

            if line_split[0] is "project_dir":
                project_dir = line_split[1]

                #change dir
                os.chdir(project_dir)

            elif line_split[0] is "genome":
                genome_count += 1

                #make genome directories
                os.mkdir("genome_" + str(genome_count))
                os.mkdir("genome_" + str(genome_count) + "/trimmed_reads")
                os.mkdir("genome_" + str(genome_count) + "/trimmed_reads/kmer")
                os.mkdir("genome_" + str(genome_count) + "/assemblies")

            elif line_split[0] is "VELVET" or "SOAP" or "SPADES":
                os.mkdir("genome_" + str(genome_count) + "/assemblies/" + line_split[1])

