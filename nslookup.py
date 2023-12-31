import os 
import subprocess


# nslookup

def lookup(DOMAIN):
	command = f'nslookup {DOMAIN}'

	try:
		# Run the command
		subprocess.run(command, shell=True)

	except subprocess.CalledProcessError as e:
		print(f'Error {e}')

def debug(DOMAIN):
	command = f'nslookup -debug {DOMAIN}'

	try:
		# Run the command
		subprocess.run(command, shell=True)

	except subprocess.CalledProcessError as e:
		print(f'Error {e}')




def reverse_lookup(ip):
	command = f'nslookup {ip}'

	try:
		# Run the command
		subprocess.run(command, shell=True)

	except subprocess.CalledProcessError as e:
		print(f'Error {e}')



def DNS_lookup(DOMAIN, SERVER):
	command = f'nslookup {DOMAIN} {SERVER}'

	try:
		# Run the command
		subprocess.run(command, shell=True)

	except subprocess.CalledProcessError as e:
		print(f'Error {e}')



def reverse_dns(ip, SERVER):
	command = f'nslookup {DOMAIN} {SERVER}'

	try:
		# Run the command
		subprocess.run(command, shell=True)

	except subprocess.CalledProcessError as e:
		print(f'Error {e}')



def any_record(DOMAIN):
	command = f'nslookup -type=any {DOMAIN}'

	try:
		# Run the command
		subprocess.run(command, shell=True)

	except subprocess.CalledProcessError as e:
		print(f'Error {e}')



def osa_record(DOMAIN):
	command = f'nslookup -type=osa {DOMAIN}'

	try:
		# Run the command
		subprocess.run(command, shell=True)

	except subprocess.CalledProcessError as e:
		print(f'Error {e}')


def ns_record(DOMAIN):
	command = f'nslookup -type=ns {DOMAIN}'

	try:
		# Run the command
		subprocess.run(command, shell=True)

	except subprocess.CalledProcessError as e:
		print(f'Error {e}')



def a_record(DOMAIN):
	command = f'nslookup -type=a {DOMAIN}'

	try:
		# Run the command
		subprocess.run(command, shell=True)

	except subprocess.CalledProcessError as e:
		print(f'Error {e}')



def mx_record(DOMAIN):
	command = f'nslookup -type=mx {DOMAIN}'

	try:
		# Run the command
		subprocess.run(command, shell=True)

	except subprocess.CalledProcessError as e:
		print(f'Error {e}')



def txt_record(DOMAIN):
	command = f'nslookup -type=txt {DOMAIN}'

	try:
		# Run the command
		subprocess.run(command, shell=True)

	except subprocess.CalledProcessError as e:
		print(f'Error {e}')

