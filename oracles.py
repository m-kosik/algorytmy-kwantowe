from qiskit import QuantumCircuit

def simon_oracle(s):
    
    N = 2*len(s)
    qc = QuantumCircuit(N)
    
    least_1_found = False
    for idx, i in enumerate(s):
        
        # find least index where s is 1
        if i == "1" and not least_1_found:
            least_1_idx = idx
            least_1_found = True
        
        # copy contents of 1st register to second
        qc.cx(idx, idx + len(s))
        
    qc.barrier()

    #qc.x(least_1_idx)
    for idx, i in enumerate(s):
        if i == "1" and least_1_found:
            qc.cx(least_1_idx, idx + len(s))
    #qc.x(least_1_idx)
            
    return qc