import port_scanner

def test_get_open_ports():
    print("Testing IP: 209.216.230.240")
    result = port_scanner.get_open_ports("209.216.230.240", [440, 445])
    print("Open ports:", result)

    print("\nTesting URL: www.stackoverflow.com")
    result = port_scanner.get_open_ports("www.stackoverflow.com", [79, 82])
    print("Open ports:", result)

    print("\nTesting URL with multiple ports: scanme.nmap.org")
    result = port_scanner.get_open_ports("scanme.nmap.org", [20, 80])
    print("Open ports:", result)

if __name__ == "__main__":
    test_get_open_ports()
