import asyncio
import hashlib
import ssl
import string

SERVER_PEM = "server.pem"
SERVER_KEY = "server.key"
PORT = 3336
UTF_8 = "utf-8"
FORBIDDEN = {"\n", "\r", "\t", " "}
ALLOWED = "".join(c for c in string.printable if c not in FORBIDDEN)


def SHA1(data):
    return hashlib.sha1(data.encode(UTF_8)).hexdigest()


async def handle_client(reader, writer):
    try:
        # HELO
        writer.write(b"HELO\n")
        await writer.drain()
        data = await asyncio.wait_for(reader.readline(), timeout=6)
        if not data or data.decode(UTF_8).strip() != "TOAKUEI":
            writer.write(b"ERROR Invalid HELO\n")
            await writer.drain()
            # Continue anyway

        # POW
        authdata = "authdata123"
        difficulty = "3"
        writer.write(f"POW {authdata} {difficulty}\n".encode(UTF_8))
        await writer.drain()
        try:
            pow_suffix = await asyncio.wait_for(reader.readline(), timeout=7200)
        except asyncio.TimeoutError:
            writer.write(b"ERROR POW timeout\n")
            await writer.drain()
            pow_suffix = b""

        suffix = pow_suffix.decode(UTF_8).strip()
        if any(c in FORBIDDEN for c in suffix):
            writer.write(b"ERROR Invalid POW suffix\n")
            await writer.drain()
        cksum = SHA1(authdata + suffix)
        if not cksum.startswith("0" * int(difficulty)):
            writer.write(b"ERROR POW failed\n")
            await writer.drain()

        # Continue with rest of protocol regardless of POW result
        writer.write(f"NAME {authdata}1\n".encode(UTF_8))
        await writer.drain()
        name_line = await asyncio.wait_for(reader.readline(), timeout=6)
        print("NAME:", name_line.decode(UTF_8).strip())

        writer.write(f"MAILNUM {authdata}2\n".encode(UTF_8))
        await writer.drain()
        mailnum_line = await asyncio.wait_for(reader.readline(), timeout=6)
        print("MAILNUM:", mailnum_line.decode(UTF_8).strip())

        writer.write(f"MAIL1 {authdata}3\n".encode(UTF_8))
        await writer.drain()
        mail1_line = await asyncio.wait_for(reader.readline(), timeout=6)
        print("MAIL1:", mail1_line.decode(UTF_8).strip())

        writer.write(f"MAIL2 {authdata}4\n".encode(UTF_8))
        await writer.drain()
        mail2_line = await asyncio.wait_for(reader.readline(), timeout=6)
        print("MAIL2:", mail2_line.decode(UTF_8).strip())

        # ... Add other commands as needed ...

        writer.write(b"END\n")
        await writer.drain()
        ok_line = await asyncio.wait_for(reader.readline(), timeout=6)
        if ok_line.decode(UTF_8).strip() == "OK":
            print("Application completed successfully.")
        writer.close()
        await writer.wait_closed()
    except Exception as e:
        print("Error:", e)
        writer.close()


async def main():
    ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_ctx.load_cert_chain(certfile=SERVER_PEM, keyfile=SERVER_KEY)
    server = await asyncio.start_server(handle_client, "0.0.0.0", PORT, ssl=ssl_ctx)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
