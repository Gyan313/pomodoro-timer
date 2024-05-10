import sys
import socket

def dns_lookup(domain_name):
    try:
        results = socket.getaddrinfo(domain_name,None,socket.AF_UNSPEC)
        ipv4_addresses = []
        ipv6_addresses = []

        for result in results:
            family,_,_,_,sockaddr = result
            # address of the socket
            address = sockaddr[0]

            if family == socket.AF_INET:
                ipv4_addresses.append(address)
            elif family == socket.AF_INET6:
                ipv6_addresses.append(address)
            
        print(f"DNS information for {domain_name}")
        print("IPV4 address: ")
        for ipv4_address in ipv4_addresses:
            print(ipv4_address)

        # TODO: on my pc ipv6 is disabled to till I didnt fix it. There is no Ipv6.
        print("\nIPV6 address: ")
        for ipv6_address in ipv6_addresses:
            print(ipv6_address)

    except socket.gaierror as e:
        print(f"Error: Cannot resolve the '{domain_name}': {e}")

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Please, enter the website you want dns lookup for.")
        sys.exit(1)
    
    website = sys.argv[1]
    dns_lookup(website)