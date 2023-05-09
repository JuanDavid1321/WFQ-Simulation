[Readme en Español](README(es).md)

# WFQ Packet Scheduler Simulation
This repository contains a simulation of Weighted Fair Queuing (WFQ) implemented in Python. WFQ is a queue scheduling algorithm used in routers and switches to allocate bandwidth to different network traffic flows based on their assigned weights.

![graficaWFQ]([https://www.researchgate.net/publication/335465513/figure/fig2/AS:797186052866049@1567075374747/WFQ-Diagram-Representation.ppm](https://slideplayer.com/slide/4669640/15/images/10/Weighted+Fair+Queuing+%28WFQ%29.jpg))

## Code Description

The code simulates the WFQ process in four main components:

* Packet Generation: It generates packets randomly to simulate network traffic. The packets have features such as source and destination addresses, size, and traffic type.

* Packet Classification: It classifies the packets into multiple queues based on their assigned weights. Each queue has a relative priority based on its weight.

* Packet Transmission: It sends the classified packets according to a specific transmission algorithm. The order and quantity of packets sent from each queue may vary depending on the implementation.

* Packet Reception and Ordering: It simulates the reception of packets and orders them based on criteria such as queue priority or arrival time.

The code is executed through the simulate_wfq(num_packets) function, where num_packets is the number of packets to generate and simulate.

## Requirements

The code requires Python 3 and the following library:

* random: Used for generating random numbers.

## Usage

* Clone the repository or download the files to your local system.

* Make sure you have Python 3 installed on your system.

* Open a terminal or command prompt and navigate to the repository directory.

* Run the following command to start the simulation:

```
python app.py
```

* Enter the number of packets you want to generate when prompted.

* Observe the output showing packet reception.

## Contribution

This project has been developed as part of an academic course and does not accept external contributions. However, if you encounter any errors or issues with the application, you can report them through the issues in this repository.
