# Networking basics #0

### Key Learning Areas
- OSI model
- LAN network
- WAN network
- Internet
- Mac address
- IP address
- TCP and UDP
- ping/ICMP

### Bash Script Tasks

#### Task 4: TCP and UDP ports
Write a Bash script that displays listening ports:

- That only shows listening sockets
- That shows the PID and name of the program to which each socket belongs

```

#!/usr/bin/env bash
netstat --listening --program

```

`netstat` command prints network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.
- By default, listening ports are usually omitted and therefore we use the flag option `--listening | -l` to show them only.
- The `--program | -p` option is used to show the PID and name of the program to which each socket belongs.

#### Task 5: Is the host on the network

Write a Bash script that pings an IP address passed as an argument.

Requirements:

- Accepts a string as an argument
- Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
- Ping the IP 5 times

```
#!/usr/bin/env bash
# Pings an IP address passed as an argument
if [ "$#" -eq 1 ]; then
	ping -c 5 "$1"
else
	echo "Usage: $0 {IP_ADDRESS}"
	exit 1
fi

```

- We first check whether the command lin arguments is equal to 1 meaning that the IP address was passed, If so, we ping the address 5 times using the `-c` flag option.
The `fi` is used in script to show the end of an if condition

- `ping` command sends ICMP request to a network host.
