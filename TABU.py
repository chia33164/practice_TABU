import random

# input
Process_time = [10, 10, 13, 4, 9, 4, 8, 15, 7, 1, 9, 3, 15, 9, 11, 6, 5, 14, 18, 3]
Due_date = [50, 38, 49, 12, 20, 105, 73, 45, 6, 64, 15, 6, 92, 43, 78, 21, 15, 50, 150, 99]
Weights = [10, 5, 1, 5, 10, 1, 5, 10, 5, 1, 5, 10, 10, 5, 1, 10, 5, 5, 1, 5]

# initial seq to a random list from 1~20
seq = list(range(1,21))
seq = random.sample(seq, 20)

iteration = int(input("iteration times : "))
TABU_size = int(input("TABU_size : "))
TABU_list = []
doing_time = 0
waste_time = []
process_sum = 0
seq_num = 0
process_list = []
waste_sum = 0
final = 0
test_final = 10000000000000000000000000000
swap_index = 0
index = 0
tabu = False
final_seq = []

# parameter t is seq that only swap two of element
def testseq (t) :
    testseq_num = 0
    tprocess_sum = 0
    twaste_time = []
    twaste_sum = 0
    for x in t:
        testseq_num = t.index(x)
        while testseq_num >= 0 :
            tprocess_sum = tprocess_sum + Process_time[t[testseq_num]-1]
            testseq_num = testseq_num - 1

        testseq_num = t.index(x)
        twaste_time.append(max(tprocess_sum - Due_date[t[testseq_num]-1], 0))
        tprocess_sum = 0

    for x in seq :
        testseq_num = t.index(x)
        twaste_sum = twaste_sum + twaste_time[testseq_num]*Weights[x-1]

    return twaste_sum

def input_TABU () :
    tmp = []
    tmp.append(seq[index])
    tmp.append(seq[index+1])
    tmp.sort()
    if  len(TABU_list) < TABU_size :
        TABU_list.append(tmp)
    else :
        TABU_list.pop(0)
        TABU_list.append(tmp)

# first iteration
for x in seq:
    seq_num = seq.index(x)
    while seq_num >= 0 :
        process_sum = process_sum + Process_time[seq[seq_num]-1]
        seq_num = seq_num - 1
    seq_num = seq.index(x)
    waste_time.append(max(process_sum - Due_date[seq[seq_num]-1], 0))
    process_sum = 0
    
for x in seq :
    seq_num = seq.index(x)
    waste_sum = waste_sum + waste_time[seq_num]*Weights[x-1]

# initial final_seq use first iteration 
for x in seq :
    final_seq.append(x)

# initial final use first iteration 
final = waste_sum

# other iteration
while doing_time < (iteration-1) :
    doing_time = doing_time + 1
    while  swap_index < 19 :
        # check whether has tabu
        for x in TABU_list :
            if (seq[swap_index] in x) & (seq[swap_index + 1] in x) :
                # tabu
                tabu = True
                break
        if tabu :
            swap_index = swap_index + 1
            tabu = False
        else :
            # swap element
            seq[swap_index], seq[swap_index+1] = seq[swap_index+1], seq[swap_index]
            # get this seq's waste_sum
            waste_sum = testseq(seq)
            seq[swap_index], seq[swap_index+1] = seq[swap_index+1], seq[swap_index]
            # if waste_sum is better than this iteration's current optimum , save it
            if waste_sum < test_final :
                index = swap_index
                test_final = waste_sum

            swap_index = swap_index + 1

    input_TABU()
    # use optimum in this iteration to do next iteration
    seq[index], seq[index+1] = seq[index+1], seq[index]
    # if this iteration's optimum is better than global optimum, save it
    if test_final < final :
        final = test_final
        final_seq.clear()
        for x in seq :
            final_seq.append(x)
        
    index = 0
    test_final = 1000000000000
    swap_index = 0

print("Final   TABU  is ", TABU_list)
print("Optimum seq   is ", final_seq)
print("Optimum waste is ", final)
