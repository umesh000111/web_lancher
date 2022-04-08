#Automation script which accept file name. Extract all URL's from
# that txt file and connect to that URL's
from sys import *
import webbrowser
import re
import urllib.error
import urllib.request

# Function : is_connected 
# Discription : request is a Python module for fetching URLs
# 
def is_connected():
    try:
        urllib.request.urlopen('http://google.com',timeout=5)
        return True
    except urllib.error.URLError as err:
        return False


def Find(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
    return url


def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            print(line)
            url = Find(line)
            print(url)
            for str in url:
                webbrowser.open(str,new=2)



def main():
    print("-------Automation Script by Paresh Chaudhari--------")
    print("Application Name: "+ argv[0])

    if(len(argv)!=2):
        print("Error: Invalid number of Argument")
        exit()

    if argv[1] =="-h":
        print("This script is used open URL which are written in one file")
        exit()

    if argv[1] =="-u":
        print("Usage : ApplicationName Name_OF_File")
        exit()
    
    try:
        connected = is_connected()

        if connected :
            WebLauncher(argv[1])
        else:
            print('Unable to connect to internet')

    except ValueError:
        print('Invalid datatype of input')
    except Exception as E:
        print('Error: Invalid input',E)

if __name__=="__main__":
    main()


