from mfrc import MFRC522
import time
 
reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)
 
def read_card_nr():
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            return str(card)

if __name__ == "__main__":
    while True:
        print(read_card_nr())
        time.sleep(1)
