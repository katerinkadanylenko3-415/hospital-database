import asyncio

HOST = '127.0.0.1'
PORT = 8080

async def send_message(writer):
    while True:
        message = await asyncio.to_thread(input)
        writer.write(f"{message}\n".encode())
        await writer.drain()
        if message == "/exit":
            print("You left the chat.")
            writer.close()
            await writer.wait_closed()
            break

async def receive_message(reader):
    while True:
        data = await reader.read(1024)
        if not data:
            break
        print(data.decode(), end="")

async def main():
    reader, writer = await asyncio.open_connection(HOST, PORT)

    nickname = input("Enter your nickname: ")
    writer.write(f"{nickname}\n".encode())
    await writer.drain()

    print("Connected to chat!")

    await asyncio.gather(
        send_message(writer),
        receive_message(reader)
    )

if __name__ == '__main__':
    asyncio.run(main())

