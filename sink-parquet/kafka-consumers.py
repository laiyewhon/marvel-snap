from consumercard import start as startcards
from consumertags import start as starttags
from consumervariants import start as startvariants

from threading import Thread

import signal, sys

def shutdown(signal, frame):
    print('Shutting down')
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown)

t1 = Thread(target=startcards, daemon=True, name="cards-consumer")
t2 = Thread(target=starttags, daemon=True, name="tags-consumer")
t3 = Thread(target=startvariants, daemon=True, name="variants-consumer")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()