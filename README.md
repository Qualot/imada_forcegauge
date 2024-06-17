# imada_forcegauge
ros node for IMADA forcegauge

# usage
```
 # to print data to standard output
 rosrun imada_forcegauge print.py --serial_port=<serial port>
 # to publish data to ROS network
 rosrun imada_forcegauge publish.py --serial_port=<serial port>
```
# udev file setup if needed (E.g. /dev/forcegauge)
```
rosrun imada_forcegauge forcegauge_udev_setup.sh              
```