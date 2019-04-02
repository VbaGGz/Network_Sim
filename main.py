from Packet import Packet
from Farme import Frame


def GenPacket(count):
    file = open("testfile.txt", "a")
    packet_cost = 100
    packet_error_cost = 10
    packet_total_cost = 0
    packets_failed = 0
    packets_succeeded = 0
    run_count = count
    packet_sent = 0
    while run_count > 0:
        packet_sent += 1
        packet = Packet()
        packet_total_cost += packet_cost
        packet_total_cost += packet_error_cost

        if not packet.packetErrorCheck:
            packets_failed += 1
        else:
            packets_succeeded += 1
            run_count -= 1

    file.write('\nSimulator Packets TCP Layer\n\n'
               'Total number of packets sent = {} '
               '\nTotal number of packets Failed = {} \n'
               'Percentage of Packet failure = {} \n'
               'Percentage of Packet Passed = {} \n'
               'Total number of packets passed = {} \n'
               'Total packet Cost = {} Cents'
               '\nAvenge Packet Cost = {} Cents'
               '\nAvenge Frame Cost = {} Cents\n'
               .format(packet_sent, packets_failed, packets_failed/packet_sent, 1 - packets_failed/packet_sent, packets_succeeded, packet_total_cost,
                       packet_total_cost / packets_succeeded, (packet_total_cost / packets_succeeded) / 10))
    file.close()


def GenFrame(count):
    file = open("testfile.txt", "a")
    frame_cost = 10
    frame_error_cost = 1.2
    frame_total_cost = 0
    frame_failed = 0
    frame_succeeded = 0
    run_count = count
    frame_sent = 0
    while run_count > 0:
        frame_sent += 1
        frame = Frame()
        frame_total_cost += frame_cost
        frame_total_cost += frame_error_cost

        if not frame.get_frame:
            frame_failed += 1
        else:
            frame_succeeded += 1
            run_count -= 1

    file.write('\nSimulator Frames DATA Link Layer\n\n'
               'Total number of Frames sent = {} '
               '\nTotal number of Frames Failed = {} \n'
               'Percentage of Frame failure = {} \n'
               'Percentage of Frame Passed = {} \n'
               'Total number of Frames passed = {} \n'
               'Total Frame Cost = {} Cents'
               '\nAvenge Frame Cost = {} Cents'
               '\nAvenge Packet Cost = {} Cents\n '
               .format(frame_sent, frame_failed, frame_failed/frame_sent, 1 - frame_failed/frame_sent, frame_succeeded, frame_total_cost, frame_total_cost / frame_succeeded,
                       (frame_total_cost / frame_succeeded) * 10))
    file.close()


GenPacket(100)
print('\n')
GenFrame(10000)
