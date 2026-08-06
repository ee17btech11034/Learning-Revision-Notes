# Computer Networks (CN)
    - CN is a telecommunications network, which allows autonomous digital devices(nodes) to exchange data b/w each other using either wired or wireless connections to share resources (h/w or s/w) interconnected by a single technology eg internet.


## Goals of CN
    - Facilitating Communication:
        - Enabling swift and efficient communication between individuals and organizations.
        - Supports video conferencing, emails, instant messaging, etc.
    - Resource Sharing:
        - Allows users to share hardware and software resources.
        - Enables printer sharing, file sharing, etc.
    - Data Storage and Access:
        - Centralized storage systems that allow data access from any connected device.
        - Helps in easy data backup and recovery.
    - Cost Efficiency:
        - Reduces costs by sharing resources and avoiding duplication of hardware and software.
    - Reliability and Redundancy:
        - Enhances reliability through alternate paths and redundant systems in case of failures.
    
## Applications of CN
    - Business and commerce
    - Education
    - Healthcare
    - Entertainment

## Data Communication
    - These are the exchange of data b/w two devices via some transmission medium.
    - It has 5 components:
        - 1. Message: 
            - information (data) to be communicated e.g. text, audio, video.
        - 2. Sender:
            - device how sends the message (computer, phone, camera etc.)
        - 3. Receiver:
            - device how receives the message (computer, phone, television etc.)
        - 4. Transmission medium:
            – is the physical path by which a message travels from sender to receiver.
        - 5. Protocol:
            – Which includes Syntax, Semantics, Timing, De facto, De jure

## Transmission Mode
    - Data flow b/w two systems can be categorised into three types:
        - 1. Simple mode:
            - It is unidirectional. One device always sends and other device always receives.
            - Eg Radio
        - 2. Half-duplex mode:
            - Both devices can receive and sent the data but at one time only one will send and another will receive or vice versa.
            - eg walkie talkie
        - 3. Full-duplex mode:
            - Both devices can send and receive at the same time. It has 2 half-duplex.
            - Telephone network

## Network criteria
    - A network must be able to meet a certain number of criteria. The most important of these are:
        - 1. Delivery & Accuracy:
            - Must deliver the data to correct destination without any error.
        - 2. Performance:
             – Can be measured in many ways including transit time, response time, number of users, type of transmission medium, capabilities of connected hardware’s and efficiency of software.
        - 3. Reliability:
            – Is a measure of frequency of failure and the time taken to resolve from the failure.
        - 4. Security:
            – Includes protecting data from unauthorised access, protecting data from damage and development.

## types of Connections
    - 1. Point to point:
        - This connection provides a dedicated link b/w two devices.
        - Most connections use Cable or wire but other eg satellite links or microwave links.
    - 2. Multipoint / multidrop:
        - This connection is one in which more than two specific devices share a single link.


## Topology
    - Topology of a network is the geomatric representation of the relationship of all the links and linking devices to one another.

    - 1. Physical Topology:
        - Refers to a way where network is laid out physically.
        - Ex:
            - Point to point
            - bus
            - Ring
            - Tree
            - Mesh
            - Star
            - hybrid

        - 1. Mesh Topology:
            - in this, every device has a dedicated point-to-point link to every other device. We need ** n*(n-1)/2 **, duplex-mode links. n--> number of nodes.
            - Advantage:
                - No traffic problem
                - Robust
                - Privacy or security
                - Fault identification and fault isolation easy.
            - Disadvantage:
                - Installation and reconnection are difficult
                - The sheer bulk of wiring
                - Expensive
        - 2. Star Topology:
            - in this, each device has a dedicated point-to-point link only to central controller, usually called a hub. The devices are not directly linked to one another.
            - The Controller acts as an excahnge: If one device wants to send data to another, it sends the data to the controller, which then relays the data top other connected devices.
            - Advantages:
                - Less expensive than Mesh topology.
                - Easy to install and reconfigure and less costly
                - it is robust. if one link fails, only that link is affected
                - Easy fault identification and fault isolation
            - Disadvantage:
                - Dependency of the whole topology on one single point, the hub.
                - Often more cabling is required in this than some other topologies.
         - Bus Topology:
            - It is multipoint. One long cable acts as a backbone to link all the devices in a network.
            - Nodes are connected to the bus cable by drop lines and taps. 
            - A drop line is a connection running b/w the device and the main cable.
            - A tap is a connector that either splices into the main cable or punctures the sheathing of a cable to create a contact with the metallic core.
            - Advantage:
                - Easy to install
                - Uses less cabling than mesh or star.
            - Disadvantage:
                - Difficult reconnection and fault isolation
                - Difficult to add new devices to network
                - A fault or break in the bus cable stops all transmission.
        - Ring Topology:
                - In a ring topology, each device has a dedicated point-to-point connection with only the two devices on either side of it.
                - A signal is passed along the ring in one direction, from device to device, until it reaches its destination. Each device in the ring incorporates a repeater.
                - When a device receives a signal intended for another device, its repeater regenerates the bits and passes them along.
                - Advantage:
                    - A Ring is relatively easy to install and reconfigure.
                    - Fault isolation is simplified
                - Disadvantage:
                    - A break in the ring (such as disabled station) can disable the entire network.

## Networks
    - Local Area Network (LAN):
        - LAN is usually limited to a few kilometers of area.
        - It may be privately owned and could be a network inside an office on one of the floor of a building or a LAN could be a network consisting of the computers in an entire building.
    - Metropolitan Area Network (MAN):
        - MAN is of size between LAN and WAN.
        - It is larger than LAN but smaller than WAN.
        - It may comprise the entire network in a city like Mumbai.
    - Wide Area Network (WAN):
        - WAN is made of all the networks in a (geographically) large area.
        - The network in the entire state of UP could be a WAN.


## OSI Model
### Network Models
    - International Standard Organization (ISO) - proposed an open system interconnection (OSI) model that allows tow system to communicate regardless of their architecture.
    - The purpose of the OSI model is to show how to facilitate communication between different systems without requiring changes to the logic of the underlying hardware and software.
    - The OSI model is not a protocol; it is a model for understanding and designing a network architecture that is flexible, robust, and interoperable. It consists of seven separate but related layers, each of which defines a part of the process of moving information across a network.
    - OSI suggest the 7 layers that are "Directive principles" but to build those 7 layers we use protocols such as TCP/IP, etc.

#### Layered Architecture
    - 1. The OSI model is composed of seven ordered layers, within a single machine, each layer calls upon the services of the layer just below it and provide services to the layer above it.
    - 2. Between machines, layer x on one machine communicates with layer x on another machine. This communication is governed by an agreed-upon series of rules and conventions called protocols.
    - 3. The processes on each machine that communicate at a given layer are called peer-to-peer processes.

