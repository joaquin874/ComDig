import adi

# Create device from specific uri address
sdr = adi.ad9361(uri="ip:192.168.0.1")
# Get data from transceiver
data = sdr.rx()