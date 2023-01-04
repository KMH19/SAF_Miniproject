## SAF_Miniproject
Miniproject source code for the software and automation frameworks course on the fifth semester of robotics engineering at AAU (Aalborg University) <br /><br /><br />

### Server (TCP-XML)
Server side TCP/IP handler which communicates with the PLC using a network socket and parses received XML formatting with the use of the xml.sax parser api.

### Client (PLC)
State machine design which handles execution of hardware functions via the festo PLC and communicates with the TCP/IP server using XML formatting. <br /><br /><br />

## How to run?
0. Adapt the main.py IP setting to match the server machine IP (line 19)<br />
1. Execute the main.py to initatite the TCP/IP server.<br />
2. Adapt the ST_client_code.txt IP setting to match the server machine IP (line 30)<br />
3. Run the ST_client_code.txt on a standard Festo CP Factory straight transportation module.<br />
4. The events are logged to server_log.txt
