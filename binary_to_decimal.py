def binary_converter(dec_num):
    # splitting integer part and floating point part by '.' and store them in dec_whole and dec_dec
    dec_whole, dec_dec = map(str, dec_num.split('.'))
    # converting integer part to binary form using .format and store that in bin_whole
    bin_whole = '{:b}'.format(int(dec_whole))
    # store '' in binary decimal part and looping over decimal floating point until its gone or until we want
    bin_dec = ''
    while int(dec_dec) != 0 and len(bin_dec) < 5:
        if len(str(int(dec_dec)*2)) > len(dec_dec):
            bin_dec += '1'
            dec_dec = str(int(dec_dec) * 2)[1:]
        else:
            bin_dec += '0'
            dec_dec = str(int(dec_dec) * 2)
    # returning binary floating point number string
    return'{bin_whole}.{bin_dec}'.format(bin_whole=bin_whole, bin_dec=bin_dec)
# This is a comment for a birth commit
