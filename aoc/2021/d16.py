from abc import ABC, abstractmethod

class Packet(ABC):

    @abstractmethod
    def get_sum_version(self):
        pass

    @abstractmethod
    def get_value(self):
        pass

class Literal(Packet):

    def __init__(self, version : int, type : int, value : int) -> None:
        super().__init__()
        self.version = version
        self.type = type
        self.value = value
    
    def get_sum_version(self):
        return self.version

    def get_value(self):
        return self.value

class Operator(Packet):

    def __init__(self, version : int, type : int, packets : list[Packet]) -> None:
        super().__init__()
        self.version = version
        self.type = type
        self.packets = packets

    def get_sum_version(self) -> int:
        return self.version + sum([packet.get_sum_version() for packet in self.packets])
    
    def get_value(self):
        vals = [packet.get_value() for packet in self.packets]
        if self.type == 0:
            return sum(vals)
        elif self.type == 1:
            mult = 1
            for val in vals:
                mult *= val
            return mult
        elif self.type == 2:
            return min(vals)
        elif self.type == 3:
            return max(vals)
        elif self.type == 5:
            return 1 if vals[0] > vals[1] else 0
        elif self.type == 6:
            return 1 if vals[0] < vals[1] else 0
        elif self.type == 7:
            return 1 if vals[0] == vals[1] else 0



with open("aoc/2021/d16.input") as file:
    line = file.readline()

    line = bin(int(line, 16))[2:]

def parse_to_packet(line : str, offset: int = 0) -> tuple[Packet, int]:
    version = int(line[offset:offset+3], 2)
    offset += 3
    type = int(line[offset:offset+3], 2)
    offset += 3

    if type == 4:
        bits = ""
        while True:
            read_bits = line[offset:offset+5]
            offset += 5
            bits += read_bits[1:]
            if read_bits[0] == "0":
                break
        return (Literal(version, type, int(bits, 2)), offset)
    else:
        packets = []
        length_id = line[offset]
        offset += 1
        if length_id == '0':
            bit_length = int(line[offset:offset+15], 2)
            offset += 15
            read_offset = offset

            while read_offset != offset + bit_length:
                packet, read_offset = parse_to_packet(line, read_offset)
                packets.append(packet)
            offset = read_offset
            return (Operator(version, type, packets), offset)
        else:
            packet_number = int(line[offset: offset+11], 2)
            offset += 11
            for _ in range(packet_number):
                packet, offset = parse_to_packet(line, offset)
                packets.append(packet)
            return (Operator(version, type, packets), offset)

packet = parse_to_packet(line)[0]
print(packet.get_sum_version())
print(packet.get_value())

