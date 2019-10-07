# extracted from https://github.com/ptone/pyosc/blob/master/examples/knect-snd.py

from FoxDot.lib.OSC3 import OSCClient, OSCMessage

client = OSCClient()
client.connect( ("localhost", 7110) )

client.send( OSCMessage("/user/1", [1.0, 2.0, 3.0 ] ) )
client.send( OSCMessage("/user/2", [2.0, 3.0, 4.0 ] ) )
client.send( OSCMessage("/user/3", [2.0, 3.0, 3.1 ] ) )
client.send( OSCMessage("/user/4", [3.2, 3.4, 6.0 ] ) )

client.send( OSCMessage("/quit") )
