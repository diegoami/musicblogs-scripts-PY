import csv
import requests
import json
import re
import sys
import blogspot_tools 


def print_videos_in_blog(blog_id, apikey, fileout):
    print("Now parsing blog "+blog_id+" with key "+apikey)
    for blog_post in blogspot_tools.iterate_blog_posts(blog_id,apikey):
        title, video = blogspot_tools.retrieve_title_and_videos(blog_post, apikey)  
        fileout.write(title+":"+ video+'\n') 
        
        
if len(sys.argv) < 2:
    print("Usage : python list_youtube_videos.py <blogsfile.txt>")
    print("Each row must be in the form blogid,apikey")
    sys.exit(0)
else:
    filename= sys.argv[1]

fileoutname = 'videolist.txt'
if len(sys.argv) >= 3:
  fileoutname = sys.argv[2]
fileout =  open(fileoutname, 'w',encoding='utf-8')
with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) < 2:
            print("Each row must be in the form blogid,apikey")
            print("Skipping....")
        else:
        
            print_videos_in_blog(row[0], row[1], fileout)