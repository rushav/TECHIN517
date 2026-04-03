from scservo_sdk import PortHandler, PacketHandler

port = PortHandler("/dev/ttyACM0")
ph = PacketHandler(0)
port.openPort()

for baud in [1000000, 115200, 500000, 250000]:
    port.setBaudRate(baud)
    for i in range(0, 20):
        model, result, err = ph.ping(port, i)
        if result == 0:
            print(f"Found at baudrate={baud} ID={i} model={model}")

port.closePort()