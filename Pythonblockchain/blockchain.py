import hashlib
class Block:
    def __init__(self, previous_block, transaction_list):
        self.previous_block = previous_block
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list)+"-"+previous_block
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
t1 = "Anna sends 2 NC to Mike"
t2 = "Bob sends 23 NC to Mike"
t3 = "Danel sends 24 NC to Mike"
t4 = "Mike sends 4.3NC to Danel"

inital_block = Block("Initial String", [t1,t2])

print(inital_block.block_data)
print(inital_block.block_hash)

second_block = Block(inital_block.block_hash,[t3,t4])
print(second_block.block_data) 
print(second_block.block_hash)
