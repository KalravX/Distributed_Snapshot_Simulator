# distributed_snapshot.py
# Chandy-Lamport Snapshot Simulator (tiny version)

processes = ['P1', 'P2', 'P3']
state = {p: 0 for p in processes}          # local state (message count)
channel = {p: [] for p in processes}       # recorded channel msgs
recorded = {p: False for p in processes}   # snapshot liya ya nahi

def send(sender, receiver, msg_type, value=None):
    """Message pass karo. Agar snapshot already liya hai, channel me record karo."""
    if recorded[sender] and msg_type == 'app':
        channel[sender].append(value)
    print(f"  {sender} --> {receiver}  [{msg_type}] {value if value is not None else ''}")

def snapshot_initiate(p):
    print(f"\n*** {p} initiates SNAPSHOT ***")
    recorded[p] = True
    # apne neighbours ko marker bhejo
    idx = processes.index(p)
    for nxt in [(idx + 1) % 3, (idx - 1) % 3]:
        send(p, processes[nxt], 'marker')

def receive_marker(p):
    if not recorded[p]:
        recorded[p] = True
        print(f"{p} received first MARKER -> records state = {state[p]}")
        idx = processes.index(p)
        for nxt in [(idx + 1) % 3, (idx - 1) % 3]:
            send(p, processes[nxt], 'marker')
    else:
        print(f"{p} received duplicate MARKER (ignore)")

# ---- Simulation ----
print("Initial states:", state)

# kuch normal messages pehle
state['P1'] += 1; send('P1', 'P2', 'app', 'msg1')
state['P2'] += 1; send('P2', 'P3', 'app', 'msg2')

# P1 snapshot start kare
snapshot_initiate('P1')

# markers propagate manually (simulate order)
receive_marker('P2')
# beech me ek message aa gaya -> ye channel state me record hoga
state['P1'] += 1; send('P1', 'P2', 'app', 'late_msg')
receive_marker('P3')
receive_marker('P1')   # P1 ko wapas marker aaya

# ---- Result ----
print("\n===== GLOBAL SNAPSHOT =====")
for p in processes:
    print(f"{p}: local_state={state[p]}, channel_state={channel[p]}")