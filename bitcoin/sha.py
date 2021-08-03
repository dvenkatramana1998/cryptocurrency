from hashlib import sha256
max_nonce = 10000000
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number,transaction,previous_hash,prefix_zeros):
    prefix_str ='0'*prefix_zeros
    for nonce in range(max_nonce):
        text = str(block_number) + transaction + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"successfully mined bitcoins with nonce value:{nonce}")
            return new_hash
    raise BaseException (f"couldn't find correct has after trying {max_nonce} times")


if __name__=='__main__':
    transactions ='''
    ramana -> yash ->12,
    madhu -> sruthi ->32
    '''
    difficulty = 4 #no of zero we want in prefixe 
    import time
    start = time.time()
    new_hash = mine (5, transactions,'0000c3af42fc31103f1fdc0151fa747ff87349a4714df7cc52ea464e12dcd4e9',difficulty)
    total_time=str((time.time()-start))
    print(f"end mining.mining took :{total_time} seconds")
    print(new_hash)







    
