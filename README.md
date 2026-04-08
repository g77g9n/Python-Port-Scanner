# Custom Python Port Scanner 

## Objective
The goal of this project was to engineer a custom network vulnerability scanner from scratch to understand how automated reconnaissance tools discover open ports and services on a target machine. 

## Skills Learned
- Network programming using Python's `socket` library.
- Understanding TCP/IP connections and port states (Open/Closed/Filtered).
- Exception handling for network timeouts and interruptions.
- Real-world application of reconnaissance tactics used by SOC Analysts and penetration testers. 

## Tools Used
- Python 3
- Visual Studio Code

## How It Works
The script utilizes the IPv4 address family and TCP streams to iterate through a specified range of network ports on a target IP. If the socket connection returns a `0` indicator, the tool successfully flags the port as open, replicating the foundational behavior of enterprise vulnerability scanners.
