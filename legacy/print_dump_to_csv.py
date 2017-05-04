import argparse
import csv
import pickle
from datetime import datetime

datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

parser = argparse.ArgumentParser()

parser.add_argument('--inputfile')
parser.add_argument('--outputfile')
parser.add_argument('--debug')


args = parser.parse_args()
debug = False if args.debug == None else True   


with open(args.inputfile, 'rb') as handle:
    videoMap = pickle.load(handle)

    with open(args.outputfile, 'w', encoding='utf-8') as whandle:
        writer = csv.writer(whandle)
        for key, (title, videoId, lastOk ) in sorted(videoMap.items(), key=lambda x: x[1][2]):
            writer.writerow([key, title, videoId, lastOk ])