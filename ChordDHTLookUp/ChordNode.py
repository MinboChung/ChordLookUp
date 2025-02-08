import hashlib
import bisect

class ChordNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.finger_table = []
    
    def __repr__(self):
        return f"Node({self.node_id})"
    
    def find_successor(self, key, nodes):
        """Finds the successor node responsible for the given key."""
        if key == self.node_id or key < nodes[0].node_id:
            return nodes[0], 1, [nodes[0]]
        
        visited_nodes = [self]
        hops = 1
        
        current = self
        while not (current.node_id <= key < nodes[(nodes.index(current) + 1) % len(nodes)].node_id):
            next_node = current.closest_preceding_node(key, nodes)
            if next_node == current:
                break
            visited_nodes.append(next_node)
            current = next_node
            hops += 1
        
        successor = nodes[(nodes.index(current) + 1) % len(nodes)]
        visited_nodes.append(successor)
        return successor, hops, visited_nodes
    
    def closest_preceding_node(self, key, nodes):
        """Find the closest preceding node before the given key."""
        for node in reversed(nodes):
            if self.node_id < node.node_id < key:
                return node
        return self

def hash_key(value, m_bits=8):
    """Hashes a given value to an m-bit space."""
    return int(hashlib.sha1(value.encode()).hexdigest(), 16) % (2**m_bits)

def chord_lookup(node_list, source_id, key):
    """Performs a lookup in the Chord network."""
    nodes = sorted([ChordNode(n) for n in node_list], key=lambda n: n.node_id)
    source_node = next(node for node in nodes if node.node_id == source_id)
    return source_node.find_successor(key, nodes)

if __name__=="__main__":
    # # Example Usage
    ...
    # node_ids = [10, 20, 40, 60, 80]
    # source_id = 10
    # key = 50

    # successor, hops, path = ChordNode.chord_lookup(node_ids, source_id, key)
    # print(f"Successor of key {key}: {successor}")
    # print(f"Number of hops: {hops}")
    # print(f"Path taken: {path}")
