from whois import whois
from prettytable import PrettyTable
from nslookup import lookup, debug, reverse_lookup, DNS_lookup, reverse_dns, any_record, osa_record, a_record, mx_record, txt_record


# phase 1, whois lookup. 
def phase1():
	DOMAIN = input("Select DOMAIN: ")
	whois(DOMAIN)

# phase 2, all nslookup lookup.
def phase2():
	DOMAIN = input("Select a DOMAIN to scan with nslookup: ")

	print("Initiating a lookup...")
	lookup(DOMAIN)
	print("Initiating a debug...")
	debug(DOMAIN)
	print("Initiating a any record lookup...")
	any_record(DOMAIN)
	print("Initiating a osa record lookup...")
	osa_record(DOMAIN)
	print("Initiating a type a record lookup...")
	a_record(DOMAIN)
	print("Initiating mail service lookup...")
	mx_record(DOMAIN)
	print("Initiating a txt record lookup...")
	txt_record(DOMAIN)
#def phase3():

#	DOMAIN = input("Select a DOMAIN to scan with dig: ")
#	dig(DOMAIN)


print("Welcome to APRT. Select a phase to start.")
print("If you don't know what are the phases, type 'h'")

user_input = input("Select a Phase (1,2,3,a): ").upper()
if user_input == '1':
	phase1()
	print("For more info, we suggest looking up your domain with phase A or 2. Alternatively - in Shodan.io and DNSdumpster. Good luck in your recon:D")
elif user_input == '2':
	phase2()
	print("For more info, we suggest looking up your domain in Shodan.io and DNSdumpster. Good luck in your recon:D")

elif user_input == 'A':
	print("Lyosh")

elif user_input == 'H':
	print("Select phase 1 to use whois. Use phase 2 to use nslookup. Phase 3 looks up the domain with dig. Phase A (All), kind of self explanitory:)")

else:
	print("Sorry, not developed yet...*__*")



