import os,hashlib,time,urllib.request,smtplib;
from email import encoders;
from email.mime.text import MIMEText;
from email.mime.base import MIMEBase;
from email.mime.multipart import MIMEMultipart;

from sys import *;
import sched;

def findDup(path):
	flag = os.path.isabs(path);

	if flag==False:
		flag=os.path.abspath(path);
	
	exists=os.path.isdir(path);

	dups = {};

	if exists:
		for dirName, Subdir, fileList in os.walk(path):
			print("current folder is : "+ dirName);
			for files in fileList:
				path = os.path.join(dirName,files);
				file_hash = hashfile(path);

				if file_hash in dups:
					dups[file_hash].append(path);
				else:
					dups[file_hash] = [path];
		return dups;
	else:
		print("invalid path");

def hashfile(path,blocksize = 1024):
    afile = open(path,'rb');
    hasher = hashlib.md5();
    buf = afile.read(blocksize);
    while len(buf) > 0:
        hasher.update(buf);
        buf = afile.read(blocksize);
    afile.close();
    return hasher.hexdigest();



def deleteFiles(dict1):
	results = list(filter(lambda x : len(x) > 1,dict1.values()));

	icnt = 0;

	if len(results) >0:
		mylog = open("MyLog.txt",'r+');
		for result in results:
			for subresult in result:
				icnt+=1;
				if icnt>=2:
					mylog.write(subresult+'\n')
					os.remove(subresult);
			icnt = 0;
	
	else:
		print("No dups Found");
	result=[];

def main():
	try:
		arr = {};
		startTime = time.time();
		arr = findDup(argv[1]);
		deleteFiles(arr);


		endTime = time.time();
		print("Took %s seconds to evaluate" %(endTime - startTime));
	
	except ValueError as VE:
		print("Error: Invalid Datatype of Input",VE);
	except Exception as E:
		print("Error: Invalid Input",E);

if __name__ == "__main__":
	main();
