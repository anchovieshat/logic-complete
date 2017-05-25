def main():
    alpha = ['A', 'B', 'C', 'D', 'E']

    inputs = 3
    op_len = 2**(inputs)
    total_ops = 2**(op_len)

    state_table = []
    for in_state in range(op_len):
        state_str = ""
        for bit_pos in range(inputs):
            state_bit = ((1 << bit_pos) & in_state) >> bit_pos
            if state_bit == 1:
                state_str += alpha[bit_pos]
            else:
                state_str += ("~" + alpha[bit_pos])
        state_table.append(state_str)

    print(state_table)

    for op in range(total_ops):
        bitop_str = ""
        if op == 0:
            bitop_str = "nil"
        elif op == (total_ops - 1):
            bitop_str = "one"
        else:
            for bit_pos in range(op_len):
                op_bit = ((1 << bit_pos) & op) >> bit_pos
                if op_bit == 1:
                    bitop_str += state_table[len(state_table) - bit_pos - 1] + " + "

        if (bitop_str.endswith(" + ")):
            bitop_str = bitop_str[:-3]

        print(("{:0" + str(op_len) + "b}: {}").format(op, bitop_str))

    print("{} {}-ary ops".format(total_ops, inputs))

main()
