import requests
import os
import subprocess
import array
import json


def check(url,response):
	d=url.split("//")[1]
	# for key,value in list(response.headers.items()):
	# 	print(key + " : " + value)     
	sc=response.headers['Set-Cookie']
	print(response.headers)
	# print()
	
	ans=[]

	li = sc.split(" ")
	newcookie=""
	
	# print()
	
	for x in range(len(li)):
		
		if 'expires' in li[x] or 'Expires' in li[x]:			
			li[x]=li[x].replace(',','')
			

			
		newcookie=newcookie+li[x]
	li = newcookie.split(",")
	
	for x in range(len(li)):
		diffc= li[x].split(";")


		dict1={}
		
		dict1['param']={}
		
		h=s=d=p=e=0


		for y in range(len(diffc)):
			
		
			if '=' not in diffc[y]:
				diffc[y]="="+diffc[y]
			

			if y==0:
				dict1['id']=diffc[y].split('=')[0]
				dict1['param']['value']=diffc[y].split("=",1)[1]

								
			if diffc[y].split('=')[1].lower() == 'httponly':
				h=1
				dict1['param']['HttpOnly']='Present'
		

			if diffc[y].split('=')[1].lower() == 'secure':
				s=1
				dict1['param']['Secure']='Present'
		

			if diffc[y].split('=')[0].lower() == 'domain':
				d=1
				dict1['param']['domain']= diffc[y].split("=")[1]
	

			if diffc[y].split('=')[0].lower() == 'path':
				p=1
				dict1['param']['path']= diffc[y].split("=")[1]
	

			if diffc[y].split('=')[0].lower() == 'expires':
				e=1
				exp=diffc[y].split("=",1)[1]
				exp= exp[:3]+", "+exp[3:]
				dict1['param']['expires']= exp
					
		
		if h==0:
			dict1['param']['HttpOnly']='Not Present'
		if s==0:
			dict1['param']['Secure']='Not Present'
		if d==0:
			dict1['param']['domain']= 'Not Present'
		if p==0:
			dict1['param']['path']= 'Not Present'
		if e==0:
			dict1['param']['expires']= 'Not Present'

		ans.append(dict1)
	

	# print()
	print("The Cookies are: ")
	print()
	i=0
	for x in ans:
		print("\033[1;37mid : "+"\033[1;36m"+x['id']+"\033[1;37m")
		print("Value : " +"\033[1;33m"+x['param']['value']+"\033[1;37m")
		if x['param']['expires']=='Not Present':
			print("Expires : " +"\033[1;31m"+x['param']['expires']+"\033[1;37m")
		else:
			print("Expires : " +"\033[1;32m"+x['param']['expires']+"\033[1;37m")
		
		if x['param']['path']=='Not Present':
			print("Path : " +"\033[1;31m"+x['param']['path']+"\033[1;37m")
		else:
			print("Path : " +"\033[1;32m"+x['param']['path']+"\033[1;37m")

		if x['param']['domain']=='Not Present':
			print("Domain : " +"\033[1;31m"+x['param']['domain']+"\033[1;37m")
		else:
			print("Domain: " +"\033[1;32m"+x['param']['domain']+"\033[1;37m")
		
		if x['param']['Secure']=='Not Present':
			print("Secure Flag : " +"\033[1;31m"+x['param']['Secure']+"\033[1;37m")
		else:
			print("Secure Flag : " +"\033[1;32m"+x['param']['Secure']+"\033[1;37m")

		if x['param']['HttpOnly']=='Not Present':
			print("HttpOnly Flag : " +"\033[1;31m"+x['param']['HttpOnly']+"\033[1;37m")
		else:
			print("HttpOnly Flag : " +"\033[1;32m"+x['param']['HttpOnly']+"\033[1;37m")

		
		i=i+1
		# try:
		# 	path1=path+"/cookies"+str(i)+".png"
		# 	import time
		# 	time.sleep(0.4)
		# 	command="scrot -e \'mv $f "+path1+"\'"
		# 	os.system(command)
		# except:
		# 	pass
		

		print()
		print()
		

	# print(ans)

def main():
	print("Enter the URL with https/http: ")
	url= input()
	print()
	res = requests.get(url)
	check(url,res)

if __name__ == "__main__":
    main()
