import asyncio
import secrets
import ssl
import string

CLIENT_PEM = "../docs/client.pem"
SERVER_PEM = "../docs/server.pem"
CLIENT_KEY = "../docs/client.key"
SERVER_IP = "18.202.148.130"
PORT = 8083
UTF_8 = "utf-8"
FORBIDDEN = {"\n", "\r", "\t", " "}
ALLOWED = "".join(c for c in string.printable if c not in FORBIDDEN)


def SHA1(data):
    data = "00000000202f79bfc3455b83264ba40c4310c483"
    return data
    # return hashlib.sha1(data.encode("utf-8")).hexdigest()


def random_string(length=1):
    return "".join(secrets.choice(ALLOWED) for _ in range(length))


async def async_tls_connect():
    ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_ctx.load_verify_locations(cafile=SERVER_PEM)
    ssl_ctx.load_cert_chain(certfile=CLIENT_PEM, keyfile=CLIENT_KEY)
    ssl_ctx.check_hostname = False
    ssl_ctx.verify_mode = ssl.CERT_REQUIRED

    reader, writer = await asyncio.open_connection(
        SERVER_IP,
        PORT,
        ssl=ssl_ctx,
        server_hostname=SERVER_IP,
        ssl_handshake_timeout=10,
    )
    print(f"Connected to {SERVER_IP}:{PORT} with TLS")
    return reader, writer


async def read_data(reader, writer, shutdown_event):
    authdata = ""
    cksum_in_hex = ""
    while True:
        data = await reader.readline()
        if data:
            args = data.decode(UTF_8).strip().split(" ")
            if args[0] == "HELO":
                print("HELO received, sending TOAKUEI")
                writer.write("TOAKUEI \n".encode(UTF_8))
                await writer.drain()
                print("Data sent successfully")
            elif args[0] == "ERROR":
                print("ERROR: " + " ".join(args[1:]))
                break
            elif args[0] == "POW":
                authdata, difficulty = args[1], args[2]
                print(f"{authdata} and {difficulty}")
                while True:
                    suffix = random_string()
                    cksum_in_hex = SHA1(authdata + suffix)
                    if cksum_in_hex.startswith("0" * int(difficulty)):
                        # writer.write((suffix + "\n").encode(UTF_8))
                        # await writer.drain()  # Signal to shutdown other tasks
                        print(f"Suffix sent: {cksum_in_hex}")
                        # shutdown_event.set()
                        break
            elif args[0] == "END":
                print("END received, data submitted")
                writer.write(b"OK\n")
                await writer.drain()
                shutdown_event.set()
                break
            elif args[0] == "NAME":
                writer.write(
                    (SHA1(authdata + args[1]) + " " + "Kadhiresh Gajendiran\n").encode(
                        UTF_8
                    )
                )
                await writer.drain()
            elif args[0] == "MAILNUM":
                writer.write((SHA1(authdata + args[1]) + " " + "2\n").encode(UTF_8))
                await writer.drain()
            elif args[0] == "MAIL1":
                writer.write(
                    (SHA1(authdata + args[1]) + " " + "kadhires89@gmail.com\n").encode(
                        UTF_8
                    )
                )
                await writer.drain()
            elif args[0] == "MAIL2":
                writer.write(
                    (
                        SHA1(authdata + args[1]) + " " + "contact2kadhir@gmail.com\n"
                    ).encode(UTF_8)
                )
                await writer.drain()
            elif args[0] == "SKYPE":
                writer.write(
                    (SHA1(authdata + args[1]) + " " + "kadhires89@gmail.com\n").encode(
                        UTF_8
                    )
                )
                await writer.drain()
            elif args[0] == "BIRTHDATE":
                writer.write(
                    (SHA1(authdata + args[1]) + " " + "07.01.1989\n").encode(UTF_8)
                )
                await writer.drain()
            elif args[0] == "COUNTRY":
                writer.write((SHA1(authdata + args[1]) + " " + "India\n").encode(UTF_8))
                await writer.drain()
            elif args[0] == "ADDRNUM":
                writer.write((SHA1(authdata + args[1]) + " " + "2\n").encode(UTF_8))
                await writer.drain()
            elif args[0] == "ADDRLINE1":
                writer.write(
                    (
                        SHA1(authdata + args[1])
                        + " 13/1 second cross street,rajaji nagar,selaiyur,chennai-600073\n"
                    ).encode(UTF_8)
                )
                await writer.drain()
            elif args[0] == "ADDRLINE2":
                writer.write(
                    (
                        SHA1(authdata + args[1])
                        + " 2/90 pilliyar kovil street,kodungal,villupuram\n"
                    ).encode(UTF_8)
                )
                await writer.drain()
    writer.close()
    await writer.wait_closed()
    return cksum_in_hex


# Example usage
async def main(shutdown_event):
    try:
        reader, writer = await async_tls_connect()
        match_data = await read_data(reader, writer, shutdown_event)
        return match_data
    except (
        ssl.SSLError,
        FileNotFoundError,
        ConnectionRefusedError,
        TimeoutError,
        OSError,
    ) as e:
        print(f"Connection or SSL error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
