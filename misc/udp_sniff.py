import os
import socket
from ctypes import *
import struct

class ip(Structure):
    _fields_ = [
        ("ip_hl",   c_ubyte, 4),
        ("ip_ver",  c_ubyte, 4),
        ("tos", c_ubyte),
        ("length",  c_ushort),
        ("id",  c_ushort),
        ("ip_offset",   c_ushort),
        ("ttl", c_ubyte),
        ("proto_num",   c_ubyte),
        ("chksum",  c_ubyte),
        ("ip_src",  c_uint32),
        ("ip_dst",  c_uint32)
    ]

    def __new__(self, sock_buff=None):
        return self.from_buffer_copy(sock_buff)

    def __init__(self, sock_buff=None):
        self.protocol_map = {1:"ICMP", 2:"TCP", 17:"UDP"}
        print(self.ip_src)
        self.src_addr = socket.inet_ntoa(struct.pack("<L", self.ip_src))
        self.dst_addr = socket.inet_ntoa(struct.pack("<L", self.ip_dst))

        try:
            self.proto = self.protocol_map[self.proto_num]
        except:
            self.proto = str(self.proto_num)

class icmp(Structure):
    _fields_ = [
        ("type", c_ubyte),
        ("code", c_ubyte),
        ("checksum", c_ubyte),
        ("unused", c_ubyte),
        ("next_hop_mtu", c_ubyte)
    ]

    def __new__(self, sock_buff):
        return self.from_buffer_copy(sock_buff)

    def __init__(self, sock_buff):
        pass

host = '192.168.1.2'

if os.name == 'nt':
    socket_proto = socket.IPPROTO_IP
else:
    socket_proto = socket.IPPROTO_ICMP

sniff = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_proto)
sniff.bind((host, 0))

sniff.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

if os.name == 'nt':
    sniff.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

try:
    while True:
        raw_buf = sniff.recvfrom(65535)[0]
        ip_header = ip(raw_buf[:32])
        
        print(" {}: {} -> {}".format(ip_header.proto, ip_header.src_addr, ip_header.dst_addr))
    
except KeyboardInterrupt:
    if os.name == 'nt':
        sniff.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

    exit(0)