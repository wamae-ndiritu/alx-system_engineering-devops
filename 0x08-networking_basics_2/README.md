# Networking Basics #1

### Key Commands and Utilities
- ifconfig
- telnet
- nc
- cut

#### Task 0: Change your home IP
Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

- localhost resolves to 127.0.0.2
- facebook.com resolves to 8.8.8.8

```

#!/usr/bin/env bash
# Configures an Ubuntu server
if [ "$(id -u)" -ne 0 ]; then
	echo "./0-change_your_home_IP: Permission denied"
	exit 1
fi
sed -i 's/127.0.0.1/127.0.0.2/' /etc/hosts
echo "8.8.8.8 facebook.com" >> /etc/hosts

```

To update the hosts file we need to have the superuser priviledges and therefore we must check whether the current user is `su`.
- If `"$(id -u)" -ne 0` checks if the current user is not the `root user`.
- The `sed` is used to perfom text transformation on an input stream eg (file). Here we are using it to update the existing localhost IP address from `127.0.0.1` to `127.0.0.2`
- 's/127.0.0.1/127.0.0.2/': This is the substitution command in sed. It searches for the pattern 127.0.0.1 and replaces it with `127.0.0.2`.

- Since there was no any entry for the domain facebook.com, we add redirects the new IP address to the hosts file.

#### Task 1: Show attached IPs
Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

```

#!/usr/bin/env bash
# Use ifconfig to get active IPv4 IPs and filter out localhost (127.0.0.1)
ifconfig | awk '/inet / {print $2}'

``` 
`ifconfig`: (interface configuration) is used to view and configure network interfaces on a Unix-like system.

`|`: (pipe operator). The output of ifconfig will be passed as input to the next command.

awk '/inet / {print $2}': This is an AWK command used to process the input received from ifconfig.

`awk`: In this context, AWK is used to filter and manipulate text-based data.

`/inet /`: This is a regular expression pattern. It matches lines containing the text "inet". In the context of ifconfig output, lines containing "inet" indicate IP address information.

`{print $2}`: This is the action associated with the pattern. When a line matches the pattern (contains "inet"), AWK will print the second field of that line. Fields in AWK are separated by whitespace (spaces or tabs). In the context of IP address information, the second field usually contains the IP address.

#### Task 2: Port listening on localhost
Write a Bash script that listens on port 98 on localhost

```
nc -l 98
```

`nc` is used for TCP connections, sending UDP Packets, listening to an abitraru TCP and UDP ports, port scanning. Both in IPv4 and IPv6
`-l` - it specify that we want to listen on the port

> To test this connection, we can open a new terminal window and use `telnet` to create an interactive communication with another this host:

```
telnet localhost 98
```

- On the new terminal, is we type any text, the text will be received on the terminal that was previously opened (The one listening).
