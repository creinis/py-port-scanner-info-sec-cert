## Port Scanner

###### Technologies:
<p align="center">
<img src="https://img.icons8.com/color/75/000000/python.png" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
</p>

### Try it!

To run the Port Scanner application, follow the instructions in the Setup section below.

## Project Structure

- `port_scanner.py`: Contains the implementation of the port scanning functions.
- `test_ports.py`: Used for development and testing the functions.
- `README.md`: Provides an overview of the project and instructions for usage.

## Setup

### Prerequisites

- Python 3 installed

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/creinis/py-port-scanner-info-sec-cert.git
   cd port-scanner
   ```

2. (Optional) Install additional libraries if required:
   ```bash
   pip install requests
   ```

3. Run the Port Scanner script:
   ```bash
   python3 port_scanner.py
   ```

## Port Scanner

### Functionality

The Port Scanner tests the availability of specified ports on a given IP address or domain. It determines whether the ports are open or closed, and provides a list of ports and states.

### Functions

#### get_open_ports Function

This function performs a scan on a list of ports for a given IP address or domain. It checks if each port is open or closed and outputs the results.

### Practical Use Case

This tool is useful for network administrators, security professionals, and anyone interested in checking the status of network ports. It can help in diagnosing connectivity issues, ensuring network security, and understanding network configurations.

### Benefits

- **Port Status Reporting:** Provides clear information on the status of network ports.
- **Easy to Use:** Simple command-line interface for quick scans.
- **Network Analysis:** Helps in understanding and diagnosing network configurations and issues.

## How to Use

1. Call the `get_open_ports` function to perform a scan on the specified ports.

### Example Usage

```python
import port_scanner

# Scan ports for a given IP address
open_ports = port_scanner.scan_ports("www.stackoverflow.com", [80, 443])
print(f"Open ports: {open_ports}")
```

### Example Output

**Scan Results:**

```
Testing URL: www.stackoverflow.com
Hostname: www.stackoverflow.com, IP: 104.18.32.7
Port 80 is open
Port 443 is closed
Open ports: [80]
```

### Additional Information

- **IP Addresses and Domains:** Can be used to scan any valid IP address or domain.
- **Port Numbers:** Customize the list of ports to scan based on your needs.

---

#### This is a FreeCodeCamp Challenge for Information Security Certification
<p align="center">
<img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" width="250" height="75" alt="freeCodeCamp" style="margin: 0 15px; opacity: 0.6" />
</p>
