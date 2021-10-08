import requests
import re
import os

class downloader():
	def __init__(self, path="./download.txt"):
		self.path = path
		self.urls = []
		self.filenames = []

	def getName(self, r):
		raw_str = r.headers['Content-Disposition']
		filename = re.search('(?<=filename=).*(?=;)', raw_str).group()\
			.encode('raw_unicode_escape')\
			.decode()
		self.filenames.append(filename) 
	
	def downloadFile(self, r, idx, path=os.getcwd()):
		with open(os.getcwd() +r'\\' + self.filenames[idx], 'wb') as f:
			f.write(r.content)

	
def proto_download():
	counter = 0
	dwnldr = downloader()
	with open("download.txt") as f:
		dwnldr.urls = list(f.readlines())
	for url_str in dwnldr.urls:
		url = url_str[:-1]
		r = requests.get(url)
		dwnldr.getName(r)
		dwnldr.downloadFile(r, counter)
		counter += 1
	print(f"Successfully downloaded {counter} files...")

if __name__ == '__main__':
	proto_download()