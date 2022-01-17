def binary_converter (dec_num):
    dec_whole,dec_dec = map(str,dec_num.split('.'))
    bin_whole = '{:b}'.format(int(dec_whole))
    bin_dec = ''
    while int(dec_dec) != 0 and len(bin_dec) < 5:
        if len(str(int(dec_dec)*2)) > len(dec_dec):
            bin_dec += '1'
            dec_dec = str(int(dec_dec) * 2)[1:]
        else:
            bin_dec += '0'
            dec_dec = str(int(dec_dec) * 2)
    return('{bin_whole}.{bin_dec}'.format(bin_whole = bin_whole , bin_dec = bin_dec))
print(binary_converter(input()))