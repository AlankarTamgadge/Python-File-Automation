import os,hashlib,time;
from sys import *;





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


def printResults(dict1):
	results = list(filter(lambda x: len(x) > 1,dict1.values()));

	if len(results)> 0:
		print("Dups Found");
		print("Dups Files are: ");
		count=0
		for result in results:
			for subresult in result:
				print("\t\t %s" %subresult);
				count+=1
				print(count)
	else:
		print("No dups found");



def main():
	try:
		arr = {};
		startTime = time.time();
		arr = findDup(argv[1]);
		printResults(arr);

		endTime = time.time();
		print("Took %s seconds to evaluate" %(endTime - startTime));
	
	except ValueError as VE:
		print("Error: Invalid Datatype of Input",VE);
	except Exception as E:
		print("Error: Invalid Input",E);






if __name__ == "__main__":
	main();