#! /usr/bin/env python3
# coding: utf-8

"""
Imada の フォースゲージのドライバとなるクラス
"""

import serial
import time
from absl import app
from absl import flags

from forcegauge import ForceGauge

FLAGS = flags.FLAGS
flags.DEFINE_string("serial_port", None, "Serial port")
flags.DEFINE_integer("print_rate", 10, "Print rate in Hz")

def main(argv):
    if FLAGS.serial_port is None:
        print("Serial port not provided. Usage: program --serial_port=<serial port> [--print_rate=<print rate>]")
        sys.exit(1)

    a = ForceGauge(FLAGS.serial_port)
    rate = FLAGS.print_rate
    dt = 1.0 / rate

    try:
        while True:
            print(str(a.read()))
            time.sleep(dt)
    except KeyboardInterrupt:
        del a

if __name__ == "__main__":
    app.run(main)
