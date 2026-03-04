import asyncio

HOST = '127.0.0.1'
PORT = 8080

clients = dict()

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info('peername')
    print(f"New client connected: {addr}")

    writer.write("Enter your nickname: ".encode())
    await writer.drain()

    data = await reader.read(1024)
    nickname = data.decode().strip()

    clients[writer] = nickname
    print(f"{nickname} joined the chat")

    for client in clients:
        if client != writer:
            client.write(f"{nickname} joined the chat\n".encode())
            await client.drain()

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break

            message = data.decode().strip()

            if message.startswith("/"):
                if message == "/users":
                    user_list = ", ".join(clients.values())
                    writer.write(f"Connected users: {user_list}\n".encode())
                    await writer.drain()
                elif message == "/exit":
                    break
                continue

            print(f"[{nickname}]: {message}")
            for client in clients:
                if client != writer:
                    client.write(f"[{nickname}]: {message}\n".encode())
                    await client.drain()

    finally:
        print(f"{nickname} disconnected")
        del clients[writer]
        for client in clients:
            client.write(f"{nickname} left the chat\n".encode())
            await client.drain()
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    print("Async chat server started!")
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
