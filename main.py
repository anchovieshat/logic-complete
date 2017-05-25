def main():
    alpha = ['A', 'B', 'C', 'D', 'E']

    inputs = 3
    bit_pad = 2**(inputs)

    state_table = []
    for in_state in range(bit_pad):
        comp_str = ""
        for bit_pos in range(inputs):
            sub_bit = ((1 << bit_pos) & in_state) >> bit_pos
            if sub_bit == 1:
                comp_str += alpha[bit_pos]
            else:
                comp_str += ("~" + alpha[bit_pos])
        state_table.append(comp_str)

    print(state_table)

    for op in range(2**bit_pad):
        comp_str = ""
        if op == 0:
            comp_str = "nil"
        elif op == ((2**bit_pad) - 1):
            comp_str = "one"
        else:
            for bit_pos in range(bit_pad):
                out_bit = ((1 << bit_pos) & op) >> bit_pos
                if out_bit == 1:
                    comp_str += state_table[len(state_table) - bit_pos - 1] + " + "

        if (comp_str.endswith(" + ")):
            comp_str = comp_str[:-3]

        print(("{:0" + str(2**inputs) + "b}: {}").format(op, comp_str))
    print("{} {}-ary ops".format(op+1, inputs))

main()
