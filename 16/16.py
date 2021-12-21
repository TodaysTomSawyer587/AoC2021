"""This script solves both parts of 2021, Day 16"""


class Packet:
    """
    Represents a packet. Determining and reading relevant parts of the
    transmission are executed upon construction. Numerical value of the  
    packet can be obtained using the "value" property.
    """
    
    def __init__(self, transmission):
        """transmission is a string of 1s and 0s"""
        
        self.children = []
        self.bits = ''
        self.subpackets = 0
        self.subbits = 0
        
        self.index = self.read(transmission)
        # if not self.index:
        #     return
        
        for sp in range(self.subpackets):
            self.children.append(Packet(transmission[self.index:]))
            self.index += self.children[sp].index
            
        starting_index = self.index
        # breakpoint()
        while self.index < starting_index + self.subbits:
            self.children.append(Packet(transmission[self.index:]))
            self.index += self.children[-1].index
        
    def add_bits(self, bits):
        """Stores bits representing the value of literal numbers"""
        
        self.bits += bits
        
    @property
    def value(self):
        """Determines value of the packet depending on type and subpackets"""
        
        if self.type == 0:
            return sum([child.value for child in self.children])
        elif self.type == 1:
            out = 1
            for child in self.children:
                out *= child.value
            return out
        elif self.type == 2:
            return min([child.value for child in self.children])
        elif self.type == 3:
            return max([child.value for child in self.children])
        elif self.type == 4:
            return int(self.bits, 2)
        elif self.type == 5:
            return self.children[0].value > self.children[1].value
        elif self.type == 6:
            return self.children[0].value < self.children[1].value
        elif self.type == 7:
            return self.children[0].value == self.children[1].value
        
    @property
    def version_sum(self):
        """sum of packet's and all childrens' version numbers"""
        
        return self.version + sum(child.version_sum for child in self.children)
    
    def read(self, transmission):
        """iteratively read transmission (str of 1s and 0s)"""
        
        i = 0
        mode = 'version'
        while i < len(transmission):
            if mode == 'version':
                if '1' not in transmission[i:]:
                    return 0
                self.version = int(transmission[i:i+3], 2)
                # if not version:
                #     break
                i += 3
                mode = 'packet_type'
                # print(f'Version: {version}')
                continue
            elif mode == 'packet_type':
                self.type = int(transmission[i:i+3], 2)
                i += 3
                # print(f'Packet type: {packet_type}')
                if self.type == 4:
                    mode = 'literal_number'
                else:
                    mode = 'operator'
                continue
            elif mode == 'literal_number':
                self.add_bits(transmission[i+1:i+5])
                # print(f'LN chunk: {chunk}')
                if not int(transmission[i]):
                    return i + 5
                i += 5
            elif mode == 'operator':
                if int(transmission[i]):
                    self.subpackets = int(transmission[i+1:i+12], 2)
                    return i + 12
                    # print(f'Operator has {sub_packets} sub_packets')
                else:
                    self.subbits = int(transmission[i+1:i+16], 2)
                    return i + 16
                    # print(f'Operator has length {sp_length}')


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        #translate the hex input to binary
        raw_string = f.readline().strip()
        transmission = bin(int(raw_string, 16))[2:]
    
    leading_zeros = len(raw_string) * 4 - len(transmission)
    transmission = leading_zeros * '0' + transmission
    
    outer_packet = Packet(transmission)
    
    print(f'The sum of all version numbers is {outer_packet.version_sum}')
    print(f'The value of the transmission is {outer_packet.value}')