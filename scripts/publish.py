#! /usr/bin/env python3
# coding: utf-8

import rospy
from forcegaugepublisher import ForceGaugePublisher
import sys
from absl import app
from absl import flags

FLAGS = flags.FLAGS
flags.DEFINE_string("serial_port", "/dev/forcegauge0", "Serial port")
flags.DEFINE_string("output_topic", "ForceGauge", "Output topic")

def main(argv):
    if FLAGS.serial_port is None:
        print("Serial port not provided. Usage: program --serial_port=<serial port> [--output_topic=<output topic>]")
        sys.exit(1)

    if FLAGS.output_topic is None:
        topicname = "ForceGauge"
    else:
        topicname = FLAGS.output_topic

    a = ForceGaugePublisher(topicname, FLAGS.serial_port)

    try:
        r = rospy.Rate(100)  # 100Hz
        while not rospy.is_shutdown():
            a.publish()
            r.sleep()

    except KeyboardInterrupt:
        del a
        sys.exit(0)

if __name__ == "__main__":
    app.run(main)
