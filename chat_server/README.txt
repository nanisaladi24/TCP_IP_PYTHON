I tried to write code as detailed as possible.

Key points to understand from this code:
- This is not multi client support code as I didn't use iterative polling approach/ threads approach.
- I'm able to successfully listen on one port and hand off comm to another server port. 
- I wrote a detailed comment on using same source-IP/Port immediately without having issues with TIME_WAIT status.
- I understood that there's no way we can drop off a port immediately (which is in time_wait status). 
    Looks like it is possible in BSD (tcpdrop utility) but not many OS.
- By default when we accept a connection, it doesn't happen on different port of server but on same one. 
    It is upto developer's implementation to do handoff task to isolate listening port. 
    This is handy when multiple clients try to connect. Need to get more details on this.

server:
create->bind->accept->communicate->close

client:
create->connect->communicate->close

* The approach used here can be scaled by listening on one process (thread) and handling each connection with its own thread.
