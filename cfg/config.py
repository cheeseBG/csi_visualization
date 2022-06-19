'''
    Configuration of Extractor and plot parameters
'''


PLOT_PARAMETER = {

    'del_null_sub': True,  # Delete null subcarriers
    'del_pilot_sub': True,  # Delete pilot subcarriers

    'time': []
}


# csi_visualization is using Nexmon CSI extractor (RPi version)
EXTRACTOR_CONFIG = {
    'wifi_chip': 'bcm43455c0',  # Raspberry Pi B3+ / B4
    'band': '2.4GHz',  # 5GHz
    'bandwidth': '20MHz'  # 40, 80, 160
}


NULL_PILOT_SUBCARRIER = {
    'null_20': ['_' + str(x+32) for x in [-32, -31, -30, -29,
                                          31,  30,  29,  0]],

    'null_40': ['_' + str(x+64) for x in [-64, -63, -62, -61, -60, -59, -1,
                                          63,  62,  61,  60,  59,  1,  0]],

    'null_80': ['_' + str(x+128) for x in [-128, -127, -126, -125, -124, -123, -1,
                                           127,  126,  125,  124,  123,  1,  0]],

    'null_160': ['_' + str(x+256) for x in [-256, -255, -254, -253, -252, -251, -129, -128, -127, -5, -4, -3, -2, -1,
                                           255,  254,  253,  252,  251,  129,  128,  127,  5,  4,  3,  3,  1,  0]],

    'pilot_20': ['_' + str(x+32) for x in [-21, -7, 21,  7]],

    'pilot_40': ['_' + str(x+64) for x in [-53, -25, -11, 53,  25,  11]],

    'pilot_80': ['_' + str(x+128) for x in [-103, -75, -39, -11, 103,  75,  39,  11]],

    'pilot_160': ['_' + str(x+256)for x in [-231, -203, -167, -139, -117, -89, -53, -25,
                                            231,  203,  167,  139,  117, 89,  53,  25]]
}
