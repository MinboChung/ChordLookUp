from ChordDHTLookUp import ChordNode

if __name__=="__main__":    
    # Example Usage
    node_ids = [15, 26, 47, 48, 51, 69, 75, 106, 110, 127]
    source_id = 26
    key = 3

    successor, hops, path = ChordNode.chord_lookup(node_ids, source_id, key)
    print(f"Successor of key {key}: {successor}")
    print(f"Number of hops: {hops}")
    print(f"Path taken: {path}")
