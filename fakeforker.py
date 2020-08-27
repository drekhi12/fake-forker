"""
A python script to get as many forks as you want
"""
from mechanize import Browser
import random
import string
#List of email providers
emailDomains = ("@xyzrandomstring.com", "@abcrandomstring.com", "pqrrandomstring.com")
password = "helloworld123"
SUCCESSFULL_FAKERS = []
user = raw_input("Enter username: Crackexy") # Username whose repository you want to fork
repository = raw_input("Enter repository name: https://github.com/Crackexy/CrackBot")
numberOfForks = input("Number of forks? : 10")
for i in range(numberOfForks):
	username = 'a'+''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(9))
	email = username+random.choice(emailDomains)
	SUCCESSFULL_FAKERS.append(username)
	# Register user
	br = Browser()
	br.set_handle_robots(False)   # ignore robots
	br.set_handle_refresh(False)
	br.open("https://github.com/join?source=header-home")
	br.form = list(br.forms())[1]
	login_control = br.form.find_control("user[login]")
	if login_control.type == "text":
		login_control.value = username
	email_control = br.form.find_control("user[email]")
	if email_control.type == "text":
		email_control.value = email
	password_control = br.form.find_control("user[password]")
	if password_control.type == "password":
		password_control.value = password
	for control in br.form.controls:
		submit = control
	submit.readonly = False
	print("New user created")
	print username
	br.submit()
	response = br.open("https://github.com/" + user + "/" + repository)
	for link in br.links():
		print link
		print link.url
	br.follow_link(text="Fork", nr=0)
