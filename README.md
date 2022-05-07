# nodeScanner_by-reflecting
a scanner to scan intermediate nodes between two devices using reflection

## Introduction
Most scanners for scanning intermediate nodes send packets with little TTL value(like `1`, `2`, etc.) and wait for replies from the nodes of TTL experiation to get their IP addresses. This strategy is quite simple and useful but does not work in special situations where the reply packets are blocked by a firewall and could not be recieved. The nodeScanner_by-reflecting tool provides a method for improving this strategy by giving a fake source IP address to the packets sent and reflects the replies to a third device so that replies would not be blocked and could be recieved.

## Requiration
The tool requires a device A for sending packets, a device B to be pinged, and a device C to recieve the packets reflected
Some requirations for those devices are shown below:
| Device      | Has To Be On | Could Be Runned Command On | Need Root Access | Have Python3 |
| ----------- | ------------ | -------------------------- | ---------------- | ------------ |
| Device A    | Yes          | Yes                        | Yes              | Yes          |
| Device B    | No           | No                         | ------           | ------       |
| Device C    | Yes          | Yes                        | Yes              | Yes          |

Other requiration: Device A should be able to send packets with fake IP addresses, and both Device C should able to be found by its IP address. (Some home computers don't satisfy these two requirements, so they have to be displayed here)

## How To Use
Two different programs need to be ran on device A and C at the same time.
1. Run `sudo python3 scan-nodes-between_reciever.py` on C. The program will start listening to packet on the internet and try to find reflected packets.
2. Run `sudo python3 scan-nodes-between_sender.py` on A. Input the IP addresses of B and C, as well as the maximum number of nodes to be considered and how many packets to be sent for each node.
3. Wait for the increase of messages about recieving packets on C to stop. Then press `Ctrl+C` to end the listening. The program will automatically print out all the packets recieved in the order of which node they are from.
     The output should look like this:
    ```

    node 0: recieved 0
    node 1: recieved 3
        packet from 1.1.1.1: TTL exceeded
        packet from 1.1.1.1: TTL exceeded
        packet from 1.1.1.1: TTL exceeded
    node 2: recieved 3
        packet from 2.2.2.1: TTL exceeded
        packet from 2.2.2.3: TTL exceeded
        packet from 2.2.2.3: TTL exceeded
    node 3: recieved 0
    node 4: recieved 2
        packet from 4.4.4.4: TTL exceeded
        packet from 4.4.4.4: TTL exceeded
    node 5: recieved 3
        packet from 1.2.3.4: common reply
        packet from 1.2.3.4: common reply
        packet from 1.2.3.4: common reply
    node 6: recieved 0
    node 7: recieved 0
    node 8: recieved 0
    ...
    ```
4. Wait for the program to print out all the data you want, then press `Ctrl+C` so that the program stops.
