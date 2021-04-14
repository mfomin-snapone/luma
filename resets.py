import telnetlib
import time

host = "192.168.0.102"
user = "araknis"
password = "SnapAV704"

wb_host = "192.168.0.145"
wb_port = 23
wb_timeout = 100


def reset_outlet():
    with telnetlib.Telnet(wb_host, wb_port, wb_timeout) as session:

        session.write(b"wattbox\n")
        session.write(b"SnapAV704\n")
        session.write(b"?Firmware\n")
        session.read_all()   

reset_outlet()
# session.write(b"!OutletSet=6,RESET,1")
# def reset_moip_switch():
#     tn = telnetlib.Telnet(wb_host)
#     tn.read_until(b"Username: ")
#     tn.write(b"araknis\n")
#     if password:
#         tn.read_until(b"Password: ")
#     tn.write(b"SnapAV704\n")
#     tn.write(b"?Firmware\n")

#     print(tn.read_all())


# reset_moip_switch()

# def network_port_reset():
#     tn = telnetlib.Telnet(host)
#     tn.read_until(b"Username: ")
#     tn.write(b"araknis\n")
#     if password:
#         tn.read_until(b"Password: ")
#     tn.write(b"SnapAV704\n")
#     time.sleep(1)
#     tn.write(b"configure\n")
#     time.sleep(1)
#     tn.write(b"interface GigabitEthernet 3\n")
#     time.sleep(1)
#     tn.write(b"shutdown\n")
#     time.sleep(10)
#     tn.write(b"no shutdown\n")
#     time.sleep(1)
#     tn.write(b"end\n")
#     time.sleep(1)
#     tn.write(b"exit\n")


# def network_port_on():
#     tn = telnetlib.Telnet(host)
#     tn.read_until(b"Username: ")
#     tn.write(b"araknis\n")
#     if password:
#         tn.read_until(b"Password: ")
#     tn.write(b"SnapAV704\n")
#     time.sleep(1)
#     tn.write(b"configure\n")
#     time.sleep(1)
#     tn.write(b"interface GigabitEthernet 3\n")
#     time.sleep(1)
#     tn.write(b"no shutdown\n")
#     time.sleep(1)
#     tn.write(b"end\n")
#     time.sleep(1)
#     tn.write(b"exit\n")


# def network_port_off():
#     tn = telnetlib.Telnet(host)
#     tn.read_until(b"Username: ")
#     tn.write(b"araknis\n")
#     if password:
#         tn.read_until(b"Password: ")
#     tn.write(b"SnapAV704\n")
#     time.sleep(1)
#     tn.write(b"configure\n")
#     time.sleep(1)
#     tn.write(b"interface GigabitEthernet 3\n")
#     time.sleep(1)
#     tn.write(b"shutdown\n")
#     time.sleep(1)
#     tn.write(b"end\n")
#     time.sleep(1)
#     tn.write(b"exit\n")


def poe_port_reset():
    tn = telnetlib.Telnet(host)
    tn.read_until(b"Username: ")
    tn.write(b"araknis\n")
    if password:
        tn.read_until(b"Password: ")
    tn.write(b"SnapAV704\n")
    time.sleep(1)
    tn.write(b"configure\n")
    time.sleep(1)
    tn.write(b"interface GigabitEthernet 3\n")
    time.sleep(1)
    tn.write(b"poe state disabled\n")
    time.sleep(5)
    tn.write(b"poe state enabled\n")
    time.sleep(1)
    tn.write(b"end\n")
    time.sleep(1)
    tn.write(b"exit\n")

