import socket

SERVER_IP = "18.202.148.130"
PORT_LIST = [3336, 8083, 8446, 49155, 3481, 65532]
CLIENT_PEM = "../docs/client.pem"
SERVER_PEM = "../docs/server.pem"
CLIENT_KEY = "../docs/client.key"
PORT = 3336
QA_CHALLANGE = "../docs/qa-challenge-.pem"
UTF_8 = "utf-8"


def tls_socksect_server(server_ip, client_pem, client_key, server_ca, port=3336):
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=SERVER_PEM)
    context.load_cert_chain(certfile=client_pem, keyfile=client_key)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    # for port in ports:
    try:
        with socket.create_socksection((server_ip, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=None) as ssock:
                print(f"socksected to {server_ip}:{port}")
                # break
    except Exception as e:
        print(f"Failed to socksect to {server_ip}:{port}: {e}")


Inter_DATA = """-----BEGIN CERTIFICATE-----
MIIBITCByAIBATAKBggqhkjOPQQDAjAbMRkwFwYDVQQDDBBleGF0ZXN0LmR5bnUu
bmV0MB4XDTIyMDYxNzExNTMzMVoXDTI2MDYxNjExNTMzMVowHzEdMBsGA1UEAwwU
c3J2LmV4YXRlc3QuZHludS5uZXQwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQJ
GTDOY8f0i8R+k6sQpkaHw26zHhEwoxDw4GlhWGPQSnzUI5t6p0hY9XWjE8A0k0jH
exLk6OYn1/vNUI3tE9pzMAoGCCqGSM49BAMCA0gAMEUCIQDfmhm6zOfIl1JJOLMv
iT3ivAkYJfMU9XUBNVpYcK+fzQIgPMLA7Hk3ceDRdHjPzWsu8RvDa2BpnkaFaXqD
kzp7ttk=
-----END CERTIFICATE-----"""
import hashlib


def SHA1(data):
    return hashlib.sha1(data.encode("utf-8")).hexdigest()


import secrets
import string

FORBIDDEN = {"\n", "\r", "\t", " "}
# Use printable ASCII as a base, or expand to more Unicode if needed
ALLOWED = "".join(c for c in string.printable if c not in FORBIDDEN)


def random_string(length=8):
    return "".join(secrets.choice(ALLOWED) for _ in range(length))


def read_data(socks):
    while True:
        data = socks.read()
        if data:
            args = data.decode(UTF_8).strip().split(" ")
            if args[0] == "HELO":
                print("HELO received, sending TOAKUEI")
                ack = socks.write("TOAKUEI \n".encode(UTF_8))
                print("Data sent successfully")
            elif args[0] == "ERROR":
                print("ERROR: " + args[6:])
                break
            elif args[0] == "POW":
                print("POW received, processing...")
                authdata, difficulty = args[1], args[2]
                # while True:
                #     suffix = random_string()
                #     cksum_in_hex = SHA1(authdata + suffix)
                #     if cksum_in_hex.startswith("0" * int(difficulty)):
                #         socks.write((suffix + "\n").encode(UTF_8))
                #         print(f"Suffix sent: {suffix}")
                #         break
            elif args[0] == "END":
                print("END received, data submitted")
                socks.sendall(b"OK\n")
                break
            elif args[0] == "NAME":
                socks.write(SHA1(authdata + args[1]) + " " + "Kadhiresh Gajendiran\n")
            elif args[0] == "MAILNUM":
                socks.write(SHA1(authdata + args[1]) + " " + "2\n")
            elif args[0] == "MAIL1":
                socks.write(SHA1(authdata + args[1]) + " " + "kadhires89@gmail.com\n")
            elif args[0] == "MAIL2":
                socks.write(
                    SHA1(authdata + args[1]) + " " + "contact2kadhir@gmail.com\n"
                )
            elif args[0] == "SKYPE":
                socks.write(SHA1(authdata + args[1]) + " " + "kadhires89@gmail.com\n")
            elif args[0] == "BIRTHDATE":
                socks.write(SHA1(authdata + args[1]) + " " + "07.01.1989\n")
            elif args[0] == "COUNTRY":
                socks.write(SHA1(authdata + args[1]) + " " + "India\n")
            elif args[0] == "ADDRNUM":
                socks.write(SHA1(authdata + args[1]) + " " + "2\n")
            elif args[0] == "ADDRLINE1":
                socks.write(
                    SHA1(authdata + args[1])
                    + " "
                    + "13/1 second cross street,rajaji nagar,selaiyur,chennai-600073\n"
                )
            elif args[0] == "ADDRLINE2":
                socks.write(
                    SHA1(authdata + args[1])
                    + " "
                    + "2/90 pilliyar kovil street,kodungal,villupuram\n"
                )
    socks.close()


# tls_socksect_server(SERVER_IP, CLIENT_PEM, CLIENT_KEY, SERVER_PEM)
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(cafile=SERVER_PEM)
# context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile=SERVER_PEM)
# context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cadata=Inter_DATA)
context.load_cert_chain(certfile=CLIENT_PEM, keyfile=CLIENT_KEY)
context.check_hostname = False  # Disable hostname check (not secure)
context.verify_mode = ssl.CERT_REQUIRED
try:
    with socket.create_connection((SERVER_IP, 3336), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=SERVER_IP) as socks:
            read_data(socks)
except Exception as e:
    print(f"Failed to socksect to {SERVER_IP}:{PORT}: {e}")


# # break
