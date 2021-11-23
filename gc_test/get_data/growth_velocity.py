# weight for age
from typing import List

data_girl = {
    '0': {'weight50': 3.2, 'weight25': 2.9, 'weight15': 2.8, 'weight5': 2.5, 'weight3': 2.4, 'weight1': 2.3, 'gram/day': 14},
    '1': {'weight50': 3.3, 'weight25': 3.0, 'weight15': 2.9, 'weight5': 2.6, 'weight3': 2.5, 'weight1': 2.3, 'gram/day': 29},
    '2': {'weight50': 3.6, 'weight25': 3.2, 'weight15': 3.1, 'weight5': 2.8, 'weight3': 2.7, 'weight1': 2.5, 'gram/day': 39},
    '3': {'weight50': 3.8, 'weight25': 3.5, 'weight15': 3.3, 'weight5': 3.0, 'weight3': 2.9, 'weight1': 2.7, 'gram/day': 39},
    '4': {'weight50': 4.1, 'weight25': 3.7, 'weight15': 3.5, 'weight5': 3.3, 'weight3': 3.1, 'weight1': 2.9, 'gram/day': 35},
    '5': {'weight50': 4.3, 'weight25': 4.0, 'weight15': 3.8, 'weight5': 3.5, 'weight3': 3.3, 'weight1': 3.1, 'gram/day': 35},
    '6': {'weight50': 4.6, 'weight25': 4.2, 'weight15': 4.0, 'weight5': 3.7, 'weight3': 3.5, 'weight1': 3.3, 'gram/day': 27},
    '7': {'weight50': 4.8, 'weight25': 4.4, 'weight15': 4.2, 'weight5': 3.8, 'weight3': 3.7, 'weight1': 3.5, 'gram/day': 27},
    '8': {'weight50': 5.0, 'weight25': 4.6, 'weight15': 4.4, 'weight5': 4.0, 'weight3': 3.9, 'weight1': 3.7, 'gram/day': 27},
    '9': {'weight50': 5.2, 'weight25': 4.7, 'weight15': 4.5, 'weight5': 4.2, 'weight3': 4.1, 'weight1': 3.8, 'gram/day': 24},
    '10': {'weight50': 5.4, 'weight25': 4.9, 'weight15': 4.7, 'weight5': 4.3, 'weight3': 4.2, 'weight1': 4.0, 'gram/day': 24},
    '11': {'weight50': 5.5, 'weight25': 5.1, 'weight15': 4.8, 'weight5': 4.5, 'weight3': 4.3, 'weight1': 4.1, 'gram/day': 24},
    # '12': {'weight50': 5.7, 'weight25': 5.2, 'weight15': 5.8, 'weight5': 4.6, 'weight3': 4.5, 'weight1': 4.2, 'gram/day': 24},
    '12': {'weight50': 5.8, 'weight25': 5.4, 'weight15': 5.1, 'weight5': 4.7, 'weight3': 4.6, 'weight1': 4.3, 'gram/day': 24},
    '13': {'weight50': 5.8, 'weight25': 5.4, 'weight15': 5.1, 'weight5': 4.7, 'weight3': 4.6, 'weight1': 4.3, 'gram/day': 24},
    '14': {'weight50': 5.8, 'weight25': 5.4, 'weight15': 5.1, 'weight5': 4.7, 'weight3': 4.6, 'weight1': 4.3, 'gram/day': 24},
    '15': {'weight50': 5.8, 'weight25': 5.4, 'weight15': 5.1, 'weight5': 4.7, 'weight3': 4.6, 'weight1': 4.3, 'gram/day': 24},
    '16': {'weight50': 6.4, 'weight25': 5.9, 'weight15': 5.6, 'weight5': 5.2, 'weight3': 5.2, 'weight1': 4.8, 'gram/day': 19},
    '17': {'weight50': 6.4, 'weight25': 5.9, 'weight15': 5.6, 'weight5': 5.2, 'weight3': 5.2, 'weight1': 4.8, 'gram/day': 19},
    '18': {'weight50': 6.4, 'weight25': 5.9, 'weight15': 5.6, 'weight5': 5.2, 'weight3': 5.2, 'weight1': 4.8, 'gram/day': 19},
    '19': {'weight50': 6.4, 'weight25': 5.9, 'weight15': 5.6, 'weight5': 5.2, 'weight3': 5.2, 'weight1': 4.8, 'gram/day': 19},
    '20': {'weight50': 6.9, 'weight25': 6.4, 'weight15': 6.1, 'weight5': 5.6, 'weight3': 5.5, 'weight1': 5.2, 'gram/day': 16},
    '21': {'weight50': 6.9, 'weight25': 6.4, 'weight15': 6.1, 'weight5': 5.6, 'weight3': 5.5, 'weight1': 5.2, 'gram/day': 16},
    '22': {'weight50': 6.9, 'weight25': 6.4, 'weight15': 6.1, 'weight5': 5.6, 'weight3': 5.5, 'weight1': 5.2, 'gram/day': 16},
    '23': {'weight50': 6.9, 'weight25': 6.4, 'weight15': 6.1, 'weight5': 5.6, 'weight3': 5.5, 'weight1': 5.2, 'gram/day': 16},
    '24': {'weight50': 7.3, 'weight25': 6.7, 'weight15': 6.4, 'weight5': 6.0, 'weight3': 5.8, 'weight1': 5.5, 'gram/day': 13},
    '25': {'weight50': 7.3, 'weight25': 6.7, 'weight15': 6.4, 'weight5': 6.0, 'weight3': 5.8, 'weight1': 5.5, 'gram/day': 13},
    '26': {'weight50': 7.3, 'weight25': 6.7, 'weight15': 6.4, 'weight5': 6.0, 'weight3': 5.8, 'weight1': 5.5, 'gram/day': 13},
    '27': {'weight50': 7.3, 'weight25': 6.7, 'weight15': 6.4, 'weight5': 6.0, 'weight3': 5.8, 'weight1': 5.5, 'gram/day': 13},
    '28': {'weight50': 7.6, 'weight25': 7.0, 'weight15': 6.7, 'weight5': 6.3, 'weight3': 6.1, 'weight1': 5.8, 'gram/day': 11},
    '29': {'weight50': 7.6, 'weight25': 7.0, 'weight15': 6.7, 'weight5': 6.3, 'weight3': 6.1, 'weight1': 5.8, 'gram/day': 11},
    '30': {'weight50': 7.6, 'weight25': 7.0, 'weight15': 6.7, 'weight5': 6.3, 'weight3': 6.1, 'weight1': 5.8, 'gram/day': 11},
    '31': {'weight50': 7.6, 'weight25': 7.0, 'weight15': 6.7, 'weight5': 6.3, 'weight3': 6.1, 'weight1': 5.8, 'gram/day': 11},
    '32': {'weight50': 7.9, 'weight25': 7.3, 'weight15': 7.0, 'weight5': 6.6, 'weight3': 6.3, 'weight1': 6.0, 'gram/day': 10},
    '33': {'weight50': 7.9, 'weight25': 7.3, 'weight15': 7.0, 'weight5': 6.6, 'weight3': 6.3, 'weight1': 6.0, 'gram/day': 10},
    '34': {'weight50': 7.9, 'weight25': 7.3, 'weight15': 7.0, 'weight5': 6.6, 'weight3': 6.3, 'weight1': 6.0, 'gram/day': 10},
    '35': {'weight50': 7.9, 'weight25': 7.3, 'weight15': 7.0, 'weight5': 6.6, 'weight3': 6.3, 'weight1': 6.0, 'gram/day': 10},
    '36': {'weight50': 8.2, 'weight25': 7.6, 'weight15': 7.3, 'weight5': 6.8, 'weight3': 6.6, 'weight1': 6.2, 'gram/day': 9},
    '37': {'weight50': 8.2, 'weight25': 7.6, 'weight15': 7.3, 'weight5': 6.8, 'weight3': 6.6, 'weight1': 6.2, 'gram/day': 9},
    '38': {'weight50': 8.2, 'weight25': 7.6, 'weight15': 7.3, 'weight5': 6.8, 'weight3': 6.6, 'weight1': 6.2, 'gram/day': 9},
    '39': {'weight50': 8.2, 'weight25': 7.6, 'weight15': 7.3, 'weight5': 6.8, 'weight3': 6.6, 'weight1': 6.2, 'gram/day': 9},
    '40': {'weight50': 8.5, 'weight25': 7.8, 'weight15': 7.5, 'weight5': 7.0, 'weight3': 6.8, 'weight1': 6.4, 'gram/day': 8},
    '41': {'weight50': 8.5, 'weight25': 7.8, 'weight15': 7.5, 'weight5': 7.0, 'weight3': 6.8, 'weight1': 6.4, 'gram/day': 8},
    '42': {'weight50': 8.5, 'weight25': 7.8, 'weight15': 7.5, 'weight5': 7.0, 'weight3': 6.8, 'weight1': 6.4, 'gram/day': 8},
    '43': {'weight50': 8.5, 'weight25': 7.8, 'weight15': 7.5, 'weight5': 7.0, 'weight3': 6.8, 'weight1': 6.4, 'gram/day': 8},
    '44': {'weight50': 8.7, 'weight25': 8.0, 'weight15': 7.7, 'weight5': 7.1, 'weight3': 7.0, 'weight1': 6.6, 'gram/day': 7},
    '45': {'weight50': 8.7, 'weight25': 8.0, 'weight15': 7.7, 'weight5': 7.1, 'weight3': 7.0, 'weight1': 6.6, 'gram/day': 7},
    '46': {'weight50': 8.7, 'weight25': 8.0, 'weight15': 7.7, 'weight5': 7.1, 'weight3': 7.0, 'weight1': 6.6, 'gram/day': 7},
    '47': {'weight50': 8.7, 'weight25': 8.0, 'weight15': 7.7, 'weight5': 7.1, 'weight3': 7.0, 'weight1': 6.6, 'gram/day': 7},
    '48': {'weight50': 8.9, 'weight25': 8.2, 'weight15': 7.9, 'weight5': 7.3, 'weight3': 7.1, 'weight1': 6.8, 'gram/day': 7},
    '49': {'weight50': 8.9, 'weight25': 8.2, 'weight15': 7.9, 'weight5': 7.3, 'weight3': 7.1, 'weight1': 6.8, 'gram/day': 7},
    '50': {'weight50': 8.9, 'weight25': 8.2, 'weight15': 7.9, 'weight5': 7.3, 'weight3': 7.1, 'weight1': 6.8, 'gram/day': 7},
    '51': {'weight50': 8.9, 'weight25': 8.2, 'weight15': 7.9, 'weight5': 7.3, 'weight3': 7.1, 'weight1': 6.8, 'gram/day': 7},
    '52': {'weight50': 9.2, 'weight25': 8.4, 'weight15': 8.1, 'weight5': 7.5, 'weight3': 7.3, 'weight1': 6.9, 'gram/day': 7},
    '53': {'weight50': 9.2, 'weight25': 8.4, 'weight15': 8.1, 'weight5': 7.5, 'weight3': 7.3, 'weight1': 6.9, 'gram/day': 7},
    '54': {'weight50': 9.2, 'weight25': 8.4, 'weight15': 8.1, 'weight5': 7.5, 'weight3': 7.3, 'weight1': 6.9, 'gram/day': 7},
    '55': {'weight50': 9.2, 'weight25': 8.4, 'weight15': 8.1, 'weight5': 7.5, 'weight3': 7.3, 'weight1': 6.9, 'gram/day': 7},
    '56': {'weight50': 9.4, 'weight25': 8.6, 'weight15': 8.3, 'weight5': 7.7, 'weight3': 7.5, 'weight1': 7.1, 'gram/day': 7},
    '57': {'weight50': 9.4, 'weight25': 8.6, 'weight15': 8.3, 'weight5': 7.7, 'weight3': 7.5, 'weight1': 7.1, 'gram/day': 7},
    '58': {'weight50': 9.4, 'weight25': 8.6, 'weight15': 8.3, 'weight5': 7.7, 'weight3': 7.5, 'weight1': 7.1, 'gram/day': 7},
    '59': {'weight50': 9.4, 'weight25': 8.6, 'weight15': 8.3, 'weight5': 7.7, 'weight3': 7.5, 'weight1': 7.1, 'gram/day': 7},
    '60': {'weight50': 9.6, 'weight25': 8.8, 'weight15': 8.5, 'weight5': 7.9, 'weight3': 7.7, 'weight1': 7.3, 'gram/day': 7},
    '61': {'weight50': 9.6, 'weight25': 8.8, 'weight15': 8.5, 'weight5': 7.9, 'weight3': 7.7, 'weight1': 7.3, 'gram/day': 7},
    '62': {'weight50': 9.6, 'weight25': 8.8, 'weight15': 8.5, 'weight5': 7.9, 'weight3': 7.7, 'weight1': 7.3, 'gram/day': 7},
    '63': {'weight50': 9.6, 'weight25': 8.8, 'weight15': 8.5, 'weight5': 7.9, 'weight3': 7.7, 'weight1': 7.3, 'gram/day': 7},
    '64': {'weight50': 9.8, 'weight25': 9.0, 'weight15': 8.7, 'weight5': 8.1, 'weight3': 7.8, 'weight1': 7.4, 'gram/day': 7},
    '65': {'weight50': 9.8, 'weight25': 9.0, 'weight15': 8.7, 'weight5': 8.1, 'weight3': 7.8, 'weight1': 7.4, 'gram/day': 7},
    '66': {'weight50': 9.8, 'weight25': 9.0, 'weight15': 8.7, 'weight5': 8.1, 'weight3': 7.8, 'weight1': 7.4, 'gram/day': 7},
    '67': {'weight50': 9.8, 'weight25': 9.0, 'weight15': 8.7, 'weight5': 8.1, 'weight3': 7.8, 'weight1': 7.4, 'gram/day': 7},
    '68': {'weight50': 10.0, 'weight25': 9.2, 'weight15': 8.8, 'weight5': 8.2, 'weight3': 8.0, 'weight1': 7.6, 'gram/day': 6},
    '69': {'weight50': 10.0, 'weight25': 9.2, 'weight15': 8.8, 'weight5': 8.2, 'weight3': 8.0, 'weight1': 7.6, 'gram/day': 6},
    '70': {'weight50': 10.0, 'weight25': 9.2, 'weight15': 8.8, 'weight5': 8.2, 'weight3': 8.0, 'weight1': 7.6, 'gram/day': 6},
    '71': {'weight50': 10.0, 'weight25': 9.2, 'weight15': 8.8, 'weight5': 8.2, 'weight3': 8.0, 'weight1': 7.6, 'gram/day': 6},
    '72': {'weight50': 10.2, 'weight25': 9.4, 'weight15': 9.0, 'weight5': 8.4, 'weight3': 8.2, 'weight1': 7.8, 'gram/day': 6},
    '73': {'weight50': 10.2, 'weight25': 9.4, 'weight15': 9.0, 'weight5': 8.4, 'weight3': 8.2, 'weight1': 7.8, 'gram/day': 6},
    '74': {'weight50': 10.2, 'weight25': 9.4, 'weight15': 9.0, 'weight5': 8.4, 'weight3': 8.2, 'weight1': 7.8, 'gram/day': 6},
    '75': {'weight50': 10.2, 'weight25': 9.4, 'weight15': 9.0, 'weight5': 8.4, 'weight3': 8.2, 'weight1': 7.8, 'gram/day': 6},
    '76': {'weight50': 10.4, 'weight25': 9.6, 'weight15': 9.2, 'weight5': 8.6, 'weight3': 8.3, 'weight1': 7.9, 'gram/day': 6},
    '77': {'weight50': 10.4, 'weight25': 9.6, 'weight15': 9.2, 'weight5': 8.6, 'weight3': 8.3, 'weight1': 7.9, 'gram/day': 6},
    '78': {'weight50': 10.4, 'weight25': 9.6, 'weight15': 9.2, 'weight5': 8.6, 'weight3': 8.3, 'weight1': 7.9, 'gram/day': 6},
    '79': {'weight50': 10.4, 'weight25': 9.6, 'weight15': 9.2, 'weight5': 8.6, 'weight3': 8.3, 'weight1': 7.9, 'gram/day': 6},
    '80': {'weight50': 10.6, 'weight25': 9.8, 'weight15': 9.4, 'weight5': 8.7, 'weight3': 8.5, 'weight1': 8.1, 'gram/day': 6},
    '81': {'weight50': 10.6, 'weight25': 9.8, 'weight15': 9.4, 'weight5': 8.7, 'weight3': 8.5, 'weight1': 8.1, 'gram/day': 6},
    '82': {'weight50': 10.6, 'weight25': 9.8, 'weight15': 9.4, 'weight5': 8.7, 'weight3': 8.5, 'weight1': 8.1, 'gram/day': 6},
    '83': {'weight50': 10.6, 'weight25': 9.8, 'weight15': 9.4, 'weight5': 8.7, 'weight3': 8.5, 'weight1': 8.1, 'gram/day': 6},
    '84': {'weight50': 10.9, 'weight25': 10.0, 'weight15': 9.6, 'weight5': 8.9, 'weight3': 8.7, 'weight1': 8.2, 'gram/day': 6},
    '85': {'weight50': 10.9, 'weight25': 10.0, 'weight15': 9.6, 'weight5': 8.9, 'weight3': 8.7, 'weight1': 8.2, 'gram/day': 6},
    '86': {'weight50': 10.9, 'weight25': 10.0, 'weight15': 9.6, 'weight5': 8.9, 'weight3': 8.7, 'weight1': 8.2, 'gram/day': 6},
    '87': {'weight50': 10.9, 'weight25': 10.0, 'weight15': 9.6, 'weight5': 8.9, 'weight3': 8.7, 'weight1': 8.2, 'gram/day': 6},
    '88': {'weight50': 11.1, 'weight25': 10.2, 'weight15': 9.8, 'weight5': 9.1, 'weight3': 8.8, 'weight1': 8.4, 'gram/day': 6},
    '89': {'weight50': 11.1, 'weight25': 10.2, 'weight15': 9.8, 'weight5': 9.1, 'weight3': 8.8, 'weight1': 8.4, 'gram/day': 6},
    '90': {'weight50': 11.1, 'weight25': 10.2, 'weight15': 9.8, 'weight5': 9.1, 'weight3': 8.8, 'weight1': 8.4, 'gram/day': 6},
    '91': {'weight50': 11.1, 'weight25': 10.2, 'weight15': 9.8, 'weight5': 9.1, 'weight3': 8.8, 'weight1': 8.4, 'gram/day': 6},
    '92': {'weight50': 11.3, 'weight25': 10.4, 'weight15': 9.9, 'weight5': 9.2, 'weight3': 9.0, 'weight1': 8.5, 'gram/day': 6},
    '93': {'weight50': 11.3, 'weight25': 10.4, 'weight15': 9.9, 'weight5': 9.2, 'weight3': 9.0, 'weight1': 8.5, 'gram/day': 6},
    '94': {'weight50': 11.3, 'weight25': 10.4, 'weight15': 9.9, 'weight5': 9.2, 'weight3': 9.0, 'weight1': 8.5, 'gram/day': 6},
    '95': {'weight50': 11.3, 'weight25': 10.4, 'weight15': 9.9, 'weight5': 9.2, 'weight3': 9.0, 'weight1': 8.5, 'gram/day': 6},
    '96': {'weight50': 11.5, 'weight25': 10.6, 'weight15': 10.1, 'weight5': 9.4, 'weight3': 9.2, 'weight1': 8.7, 'gram/day': 6},

}

data_boy = {
    '0': {'weight50': 3.3, 'weight25': 3.0, 'weight15': 2.9, 'weight5': 2.6, 'weight3': 2.5, 'weight1': 2.3, 'gram/day': 21},
    '1': {'weight50': 3.5, 'weight25': 3.2, 'weight15': 3.0, 'weight5': 2.7, 'weight3': 2.6, 'weight1': 2.4, 'gram/day': 33},
    '2': {'weight50': 3.8, 'weight25': 3.4, 'weight15': 3.2, 'weight5': 3.0, 'weight3': 2.8, 'weight1': 2.7, 'gram/day': 46},
    '3': {'weight50': 4.1, 'weight25': 3.7, 'weight15': 3.5, 'weight5': 3.2, 'weight3': 3.1, 'weight1': 2.9, 'gram/day': 46},
    '4': {'weight50': 4.4, 'weight25': 4.0, 'weight15': 3.8, 'weight5': 3.5, 'weight3': 3.4, 'weight1': 3.2, 'gram/day': 40},
    '5': {'weight50': 4.7, 'weight25': 4.3, 'weight15': 4.1, 'weight5': 3.7, 'weight3': 3.6, 'weight1': 3.4, 'gram/day': 40},
    '6': {'weight50': 4.9, 'weight25': 4.5, 'weight15': 4.3, 'weight5': 4.0, 'weight3': 3.8, 'weight1': 3.6, 'gram/day': 34},
    '7': {'weight50': 5.2, 'weight25': 4.8, 'weight15': 4.5, 'weight5': 4.2, 'weight3': 4.1, 'weight1': 3.8, 'gram/day': 34},
    '8': {'weight50': 5.4, 'weight25': 5.0, 'weight15': 4.7, 'weight5': 4.4, 'weight3': 4.3, 'weight1': 4.0, 'gram/day': 34},
    '9': {'weight50': 5.6, 'weight25': 5.2, 'weight15': 4.9, 'weight5': 4.6, 'weight3': 4.4, 'weight1': 4.2, 'gram/day': 27},
    '10': {'weight50': 5.8, 'weight25': 5.4, 'weight15': 5.1, 'weight5': 4.8, 'weight3': 4.6, 'weight1': 4.4, 'gram/day': 27},
    '11': {'weight50': 6.0, 'weight25': 5.6, 'weight15': 5.3, 'weight5': 4.9, 'weight3': 4.8, 'weight1': 4.5, 'gram/day': 27},
    # '12': {'weight50': 6.2, 'weight25': 5.7, 'weight15': 5.5, 'weight5': 5.1, 'weight3': 4.9, 'weight1': 4.7, 'gram/day': 27},
    '12': {'weight50': 6.4, 'weight25': 5.9, 'weight15': 5.6, 'weight5': 5.2, 'weight3': 5.1, 'weight1': 4.8, 'gram/day': 24},
    '13': {'weight50': 6.4, 'weight25': 5.9, 'weight15': 5.6, 'weight5': 5.2, 'weight3': 5.1, 'weight1': 4.8, 'gram/day': 24},
    '14': {'weight50': 6.4, 'weight25': 5.9, 'weight15': 5.6, 'weight5': 5.2, 'weight3': 5.1, 'weight1': 4.8, 'gram/day': 24},
    '15': {'weight50': 6.4, 'weight25': 5.9, 'weight15': 5.6, 'weight5': 5.2, 'weight3': 5.1, 'weight1': 4.8, 'gram/day': 24},
    '16': {'weight50': 7.0, 'weight25': 6.5, 'weight15': 6.2, 'weight5': 5.8, 'weight3': 5.6, 'weight1': 5.4, 'gram/day': 20.5},
    '17': {'weight50': 7.0, 'weight25': 6.5, 'weight15': 6.2, 'weight5': 5.8, 'weight3': 5.6, 'weight1': 5.4, 'gram/day': 20.5},
    '18': {'weight50': 7.0, 'weight25': 6.5, 'weight15': 6.2, 'weight5': 5.8, 'weight3': 5.6, 'weight1': 5.4, 'gram/day': 20.5},
    '19': {'weight50': 7.0, 'weight25': 6.5, 'weight15': 6.2, 'weight5': 5.8, 'weight3': 5.6, 'weight1': 5.4, 'gram/day': 20.5},
    '20': {'weight50': 7.5, 'weight25': 7.0, 'weight15': 6.7, 'weight5': 6.2, 'weight3': 6.1, 'weight1': 5.8, 'gram/day': 17.4},
    '21': {'weight50': 7.5, 'weight25': 7.0, 'weight15': 6.7, 'weight5': 6.2, 'weight3': 6.1, 'weight1': 5.8, 'gram/day': 17.4},
    '22': {'weight50': 7.5, 'weight25': 7.0, 'weight15': 6.7, 'weight5': 6.2, 'weight3': 6.1, 'weight1': 5.8, 'gram/day': 17.4},
    '23': {'weight50': 7.5, 'weight25': 7.0, 'weight15': 6.7, 'weight5': 6.2, 'weight3': 6.1, 'weight1': 5.8, 'gram/day': 17.4},
    '24': {'weight50': 7.9, 'weight25': 7.4, 'weight15': 7.1, 'weight5': 6.6, 'weight3': 6.4, 'weight1': 6.1, 'gram/day': 14},
    '25': {'weight50': 7.9, 'weight25': 7.4, 'weight15': 7.1, 'weight5': 6.6, 'weight3': 6.4, 'weight1': 6.1, 'gram/day': 14},
    '26': {'weight50': 7.9, 'weight25': 7.4, 'weight15': 7.1, 'weight5': 6.6, 'weight3': 6.4, 'weight1': 6.1, 'gram/day': 14},
    '27': {'weight50': 7.9, 'weight25': 7.4, 'weight15': 7.1, 'weight5': 6.6, 'weight3': 6.4, 'weight1': 6.1, 'gram/day': 14},
    '28': {'weight50': 8.3, 'weight25': 7.7, 'weight15': 7.4, 'weight5': 6.9, 'weight3': 6.7, 'weight1': 6.4, 'gram/day': 12},
    '29': {'weight50': 8.3, 'weight25': 7.7, 'weight15': 7.4, 'weight5': 6.9, 'weight3': 6.7, 'weight1': 6.4, 'gram/day': 12},
    '30': {'weight50': 8.3, 'weight25': 7.7, 'weight15': 7.4, 'weight5': 6.9, 'weight3': 6.7, 'weight1': 6.4, 'gram/day': 12},
    '31': {'weight50': 8.3, 'weight25': 7.7, 'weight15': 7.4, 'weight5': 6.9, 'weight3': 6.7, 'weight1': 6.4, 'gram/day': 12},
    '32': {'weight50': 8.6, 'weight25': 8.0, 'weight15': 7.7, 'weight5': 7.2, 'weight3': 7.0, 'weight1': 6.7, 'gram/day': 10},
    '33': {'weight50': 8.6, 'weight25': 8.0, 'weight15': 7.7, 'weight5': 7.2, 'weight3': 7.0, 'weight1': 6.7, 'gram/day': 10},
    '34': {'weight50': 8.6, 'weight25': 8.0, 'weight15': 7.7, 'weight5': 7.2, 'weight3': 7.0, 'weight1': 6.7, 'gram/day': 10},
    '35': {'weight50': 8.6, 'weight25': 8.0, 'weight15': 7.7, 'weight5': 7.2, 'weight3': 7.0, 'weight1': 6.7, 'gram/day': 10},
    '36': {'weight50': 8.9, 'weight25': 8.3, 'weight15': 7.9, 'weight5': 7.4, 'weight3': 7.2, 'weight1': 6.9, 'gram/day': 9},
    '37': {'weight50': 8.9, 'weight25': 8.3, 'weight15': 7.9, 'weight5': 7.4, 'weight3': 7.2, 'weight1': 6.9, 'gram/day': 9},
    '38': {'weight50': 8.9, 'weight25': 8.3, 'weight15': 7.9, 'weight5': 7.4, 'weight3': 7.2, 'weight1': 6.9, 'gram/day': 9},
    '39': {'weight50': 8.9, 'weight25': 8.3, 'weight15': 7.9, 'weight5': 7.4, 'weight3': 7.2, 'weight1': 6.9, 'gram/day': 9},
    '40': {'weight50': 9.2, 'weight25': 8.5, 'weight15': 8.2, 'weight5': 7.7, 'weight3': 7.5, 'weight1': 7.1, 'gram/day': 9},
    '41': {'weight50': 9.2, 'weight25': 8.5, 'weight15': 8.2, 'weight5': 7.7, 'weight3': 7.5, 'weight1': 7.1, 'gram/day': 9},
    '42': {'weight50': 9.2, 'weight25': 8.5, 'weight15': 8.2, 'weight5': 7.7, 'weight3': 7.5, 'weight1': 7.1, 'gram/day': 9},
    '43': {'weight50': 9.2, 'weight25': 8.5, 'weight15': 8.2, 'weight5': 7.7, 'weight3': 7.5, 'weight1': 7.1, 'gram/day': 9},
    '44': {'weight50': 9.4, 'weight25': 8.7, 'weight15': 8.4, 'weight5': 7.9, 'weight3': 7.7, 'weight1': 7.3, 'gram/day': 8},
    '45': {'weight50': 9.4, 'weight25': 8.7, 'weight15': 8.4, 'weight5': 7.9, 'weight3': 7.7, 'weight1': 7.3, 'gram/day': 8},
    '46': {'weight50': 9.4, 'weight25': 8.7, 'weight15': 8.4, 'weight5': 7.9, 'weight3': 7.7, 'weight1': 7.3, 'gram/day': 8},
    '47': {'weight50': 9.4, 'weight25': 8.7, 'weight15': 8.4, 'weight5': 7.9, 'weight3': 7.7, 'weight1': 7.3, 'gram/day': 8},
    '48': {'weight50': 9.6, 'weight25': 9.0, 'weight15': 8.6, 'weight5': 8.1, 'weight3': 7.8, 'weight1': 7.5, 'gram/day': 8},
    '49': {'weight50': 9.6, 'weight25': 9.0, 'weight15': 8.6, 'weight5': 8.1, 'weight3': 7.8, 'weight1': 7.5, 'gram/day': 8},
    '50': {'weight50': 9.6, 'weight25': 9.0, 'weight15': 8.6, 'weight5': 8.1, 'weight3': 7.8, 'weight1': 7.5, 'gram/day': 8},
    '51': {'weight50': 9.6, 'weight25': 9.0, 'weight15': 8.6, 'weight5': 8.1, 'weight3': 7.8, 'weight1': 7.5, 'gram/day': 8},
    '52': {'weight50': 9.9, 'weight25': 9.2, 'weight15': 8.8, 'weight5': 8.2, 'weight3': 8.0, 'weight1': 7.6, 'gram/day': 8},
    '53': {'weight50': 9.9, 'weight25': 9.2, 'weight15': 8.8, 'weight5': 8.2, 'weight3': 8.0, 'weight1': 7.6, 'gram/day': 8},
    '54': {'weight50': 9.9, 'weight25': 9.2, 'weight15': 8.8, 'weight5': 8.2, 'weight3': 8.0, 'weight1': 7.6, 'gram/day': 8},
    '55': {'weight50': 9.9, 'weight25': 9.2, 'weight15': 8.8, 'weight5': 8.2, 'weight3': 8.0, 'weight1': 7.6, 'gram/day': 8},
    '56': {'weight50': 10.1, 'weight25': 9.4, 'weight15': 9.0, 'weight5': 8.4, 'weight3': 8.2, 'weight1': 7.8, 'gram/day': 8},
    '57': {'weight50': 10.1, 'weight25': 9.4, 'weight15': 9.0, 'weight5': 8.4, 'weight3': 8.2, 'weight1': 7.8, 'gram/day': 8},
    '58': {'weight50': 10.1, 'weight25': 9.4, 'weight15': 9.0, 'weight5': 8.4, 'weight3': 8.2, 'weight1': 7.8, 'gram/day': 8},
    '59': {'weight50': 10.1, 'weight25': 9.4, 'weight15': 9.0, 'weight5': 8.4, 'weight3': 8.2, 'weight1': 7.8, 'gram/day': 8},
    '60': {'weight50': 10.3, 'weight25': 9.6, 'weight15': 9.2, 'weight5': 8.6, 'weight3': 8.4, 'weight1': 8.0, 'gram/day': 8},
    '61': {'weight50': 10.3, 'weight25': 9.6, 'weight15': 9.2, 'weight5': 8.6, 'weight3': 8.4, 'weight1': 8.0, 'gram/day': 8},
    '62': {'weight50': 10.3, 'weight25': 9.6, 'weight15': 9.2, 'weight5': 8.6, 'weight3': 8.4, 'weight1': 8.0, 'gram/day': 8},
    '63': {'weight50': 10.3, 'weight25': 9.6, 'weight15': 9.2, 'weight5': 8.6, 'weight3': 8.4, 'weight1': 8.0, 'gram/day': 8},
    '64': {'weight50': 10.5, 'weight25': 9.8, 'weight15': 9.4, 'weight5': 8.8, 'weight3': 8.5, 'weight1': 8.1, 'gram/day': 8},
    '65': {'weight50': 10.5, 'weight25': 9.8, 'weight15': 9.4, 'weight5': 8.8, 'weight3': 8.5, 'weight1': 8.1, 'gram/day': 8},
    '66': {'weight50': 10.5, 'weight25': 9.8, 'weight15': 9.4, 'weight5': 8.8, 'weight3': 8.5, 'weight1': 8.1, 'gram/day': 8},
    '67': {'weight50': 10.5, 'weight25': 9.8, 'weight15': 9.4, 'weight5': 8.8, 'weight3': 8.5, 'weight1': 8.1, 'gram/day': 8},
    '68': {'weight50': 10.7, 'weight25': 10.0, 'weight15': 9.6, 'weight5': 8.9, 'weight3': 8.7, 'weight1': 8.3, 'gram/day': 8},
    '69': {'weight50': 10.7, 'weight25': 10.0, 'weight15': 9.6, 'weight5': 8.9, 'weight3': 8.7, 'weight1': 8.3, 'gram/day': 8},
    '70': {'weight50': 10.7, 'weight25': 10.0, 'weight15': 9.6, 'weight5': 8.9, 'weight3': 8.7, 'weight1': 8.3, 'gram/day': 8},
    '71': {'weight50': 10.7, 'weight25': 10.0, 'weight15': 9.6, 'weight5': 8.9, 'weight3': 8.7, 'weight1': 8.3, 'gram/day': 8},
    '72': {'weight50': 10.9, 'weight25': 10.1, 'weight15': 9.7, 'weight5': 9.1, 'weight3': 8.9, 'weight1': 8.4, 'gram/day': 8},
    '73': {'weight50': 10.9, 'weight25': 10.1, 'weight15': 9.7, 'weight5': 9.1, 'weight3': 8.9, 'weight1': 8.4, 'gram/day': 8},
    '74': {'weight50': 10.9, 'weight25': 10.1, 'weight15': 9.7, 'weight5': 9.1, 'weight3': 8.9, 'weight1': 8.4, 'gram/day': 8},
    '75': {'weight50': 10.9, 'weight25': 10.1, 'weight15': 9.7, 'weight5': 9.1, 'weight3': 8.9, 'weight1': 8.4, 'gram/day': 8},
    '76': {'weight50': 11.1, 'weight25': 10.3, 'weight15': 9.9, 'weight5': 9.3, 'weight3': 9.0, 'weight1': 8.6, 'gram/day': 8},
    '77': {'weight50': 11.1, 'weight25': 10.3, 'weight15': 9.9, 'weight5': 9.3, 'weight3': 9.0, 'weight1': 8.6, 'gram/day': 8},
    '78': {'weight50': 11.1, 'weight25': 10.3, 'weight15': 9.9, 'weight5': 9.3, 'weight3': 9.0, 'weight1': 8.6, 'gram/day': 8},
    '79': {'weight50': 11.1, 'weight25': 10.3, 'weight15': 9.9, 'weight5': 9.3, 'weight3': 9.0, 'weight1': 8.6, 'gram/day': 8},
    '80': {'weight50': 11.3, 'weight25': 10.5, 'weight15': 10.1, 'weight5': 9.4, 'weight3': 9.2, 'weight1': 8.7, 'gram/day': 8},
    '81': {'weight50': 11.3, 'weight25': 10.5, 'weight15': 10.1, 'weight5': 9.4, 'weight3': 9.2, 'weight1': 8.7, 'gram/day': 8},
    '82': {'weight50': 11.3, 'weight25': 10.5, 'weight15': 10.1, 'weight5': 9.4, 'weight3': 9.2, 'weight1': 8.7, 'gram/day': 8},
    '83': {'weight50': 11.3, 'weight25': 10.5, 'weight15': 10.1, 'weight5': 9.4, 'weight3': 9.2, 'weight1': 8.7, 'gram/day': 8},
    '84': {'weight50': 11.5, 'weight25': 10.8, 'weight15': 10.3, 'weight5': 9.6, 'weight3': 9.3, 'weight1': 8.9, 'gram/day': 8},
    '85': {'weight50': 11.5, 'weight25': 10.8, 'weight15': 10.3, 'weight5': 9.6, 'weight3': 9.3, 'weight1': 8.9, 'gram/day': 8},
    '86': {'weight50': 11.5, 'weight25': 10.8, 'weight15': 10.3, 'weight5': 9.6, 'weight3': 9.3, 'weight1': 8.9, 'gram/day': 8},
    '87': {'weight50': 11.5, 'weight25': 10.8, 'weight15': 10.3, 'weight5': 9.6, 'weight3': 9.3, 'weight1': 8.9, 'gram/day': 8},
    '88': {'weight50': 11.8, 'weight25': 10.9, 'weight15': 10.5, 'weight5': 9.8, 'weight3': 9.5, 'weight1': 9.0, 'gram/day': 7},
    '89': {'weight50': 11.8, 'weight25': 10.9, 'weight15': 10.5, 'weight5': 9.8, 'weight3': 9.5, 'weight1': 9.0, 'gram/day': 7},
    '90': {'weight50': 11.8, 'weight25': 10.9, 'weight15': 10.5, 'weight5': 9.8, 'weight3': 9.5, 'weight1': 9.0, 'gram/day': 7},
    '91': {'weight50': 11.8, 'weight25': 10.9, 'weight15': 10.5, 'weight5': 9.8, 'weight3': 9.5, 'weight1': 9.0, 'gram/day': 7},
    '92': {'weight50': 12.0, 'weight25': 11.1, 'weight15': 10.6, 'weight5': 9.9, 'weight3': 9.7, 'weight1': 9.2, 'gram/day': 7},
    '93': {'weight50': 12.0, 'weight25': 11.1, 'weight15': 10.6, 'weight5': 9.9, 'weight3': 9.7, 'weight1': 9.2, 'gram/day': 7},
    '94': {'weight50': 12.0, 'weight25': 11.1, 'weight15': 10.6, 'weight5': 9.9, 'weight3': 9.7, 'weight1': 9.2, 'gram/day': 7},
    '95': {'weight50': 12.0, 'weight25': 11.1, 'weight15': 10.6, 'weight5': 9.9, 'weight3': 9.7, 'weight1': 9.2, 'gram/day': 7},
    '96': {'weight50': 12.2, 'weight25': 11.3, 'weight15': 10.8, 'weight5': 10.1, 'weight3': 9.8, 'weight1': 9.3, 'gram/day': 7},
}

def velocity(dict):

    gen = dict.get('gender')
    if gen == 0:
        gender = "girl"
    else:
        gender = "boy"
    age = str(int(dict.get('age')))
    weight = float(dict.get('weight'))
    st=''
    sta = ''
    stb = ''

    if gender == "girl":
        weight_for_age = data_girl[age]

        # print(children)
        if weight < weight_for_age['weight15']:
           # print("Child is in RED Zone")
           # print(f"Weight for LIGHT GREEN Zone: {weight_for_age['weight25']}")
           # print(f"Average weight of a child in this age group: {weight_for_age['weight50']}")
           zone = 'RED'
           wlg = weight_for_age['weight25']
           avg = weight_for_age['weight50']


        if weight >= weight_for_age['weight25']:
           # print("Child is in LIGHT GREEN Zone")
           # print(f"Weight for LIGHT GREEN Zone: {weight_for_age['weight25']}")
           # print(f"Average weight of a child in this age group: {weight_for_age['weight50']}")
           zone = 'LIGHT GREEN'
           wlg = weight_for_age['weight25']
           avg = weight_for_age['weight50']
        if weight_for_age['weight25'] > weight >= weight_for_age['weight15']:
           # print("Child is in YELLOW Zone")
          #  print(f"Weight for LIGHT GREEN Zone: {weight_for_age['weight25']}")
          #  print(f"Average weight of a child in this age group: {weight_for_age['weight50']}")
           zone = 'YELLOW'
           wlg = weight_for_age['weight25']
           avg = weight_for_age['weight50']

        if weight >= weight_for_age['weight50']:
            print("Child is in DARK GREEN Zone")
            print(f"Weight for LIGHT GREEN Zone: {weight_for_age['weight25']}")
            print(f"Average weight of a child in this age group: {weight_for_age['weight50']}")
            zone = 'DARK GREEN'
            wlg = weight_for_age['weight25']
            avg = weight_for_age['weight50']


    else:
        weight_for_age = data_boy[age]

        # print(children)
        if weight < weight_for_age['weight15']:
           # print("Child is in RED Zone")
           # print(f"Weight for LIGHT GREEN Zone: {weight_for_age['weight25']}")
           # print(f"Average weight of a child in this age group: {weight_for_age['weight50']}")
           zone = 'RED'
           wlg = weight_for_age['weight25']
           avg = weight_for_age['weight50']

        if weight_for_age['weight50'] > weight >= weight_for_age['weight25']:
          #  print("Child is in LIGHT GREEN Zone")
          #  print(f"Weight for LIGHT GREEN Zone: {weight_for_age['weight25']}")
          #  print(f"Average weight of a child in this age group: {weight_for_age['weight50']}")
          zone = 'LIGHT GREEN'
          wlg = weight_for_age['weight25']
          avg = weight_for_age['weight50']

        if weight_for_age['weight25'] > weight >= weight_for_age['weight15']:
            #print("Child is in YELLOW Zone")
            #print(f"Weight for LIGHT GREEN Zone: {weight_for_age['weight25']}")
            #print(f"Average weight of a child in this age group: {weight_for_age['weight50']}")
            zone = 'YELLOW'
            wlg = weight_for_age['weight25']
            avg = weight_for_age['weight50']

        if weight >= weight_for_age['weight50']:
           # print("Child is in DARK GREEN Zone")
            #print(f"Weight for LIGHT GREEN Zone: {weight_for_age['weight25']}")
            #print(f"Average weight of a child in this age group: {weight_for_age['weight50']}")
           zone = 'DARK GREEN'
           wlg = weight_for_age['weight25']
           avg = weight_for_age['weight50']


    if gender == "girl":
        weight_for_age = data_girl[age]

        # print(children)
        if weight < weight_for_age['weight1']:
            per="Child is below the 1 percentile zone"
           # s.append("Child is below the 1 percentile zone"+'<br>')

        if weight_for_age['weight1'] <= weight < weight_for_age['weight3']:
            per = "Child is between 1 to 3 percentile zone"
           # s.append("Child is between 1 to 3 percentile zone"+'<br>')

        if weight_for_age['weight3'] <= weight < weight_for_age['weight5']:
            per ="Child is between 3 to 5 percentile zone"
          #  s.append("Child is between 3 to 5 percentile zone" + '<br>')

        if weight_for_age['weight5'] <= weight < weight_for_age['weight15']:
            per ="Child is between 5 to 15 percentile zone"
          #  s.append("Child is between 5 to 15 percentile zone" + '<br>')

        if weight_for_age['weight15'] <= weight < weight_for_age['weight25']:
            per ="Child is between 15 to 25 percentile zone"
          #  s.append("Child is between 15 to 25 percentile zone" + '<br>')

        if weight_for_age["weight25"] <= weight < weight_for_age['weight50']:
            per ="Child is between 25 to 50 percentile zone"
         #   s.append("Child is between 25 to 50 percentile zone" + '<br>')

        if weight >= weight_for_age['weight50']:
            per ="Child is above the 50 percentile zone"
           # s.append("Child is above the 50 percentile zone" + '<br>')

    elif gender == "boy":
        weight_for_age = data_boy[age]

        # print(children)
        if weight < weight_for_age['weight1']:
            per ="Child is below the 1 percentile zone"
           # s.append("Child is below the 1 percentile zone" + '<br>')

        if weight_for_age['weight1'] <= weight < weight_for_age['weight3']:
            per ="Child is between 1 to 3 percentile zone"
         # s.append("Child is between 1 to 3 percentile zone" + '<br>')

        if weight_for_age['weight3'] <= weight < weight_for_age['weight5']:
            per ="Child is between 3 to 5 percentile zone"
           # s.append("Child is between 3 to 5 percentile zone" + '<br>'

        if weight_for_age['weight5'] <= weight < weight_for_age['weight15']:
            per ="Child is between 5 to 15 percentile zone"
           # s.append("Child is between 5 to 15 percentile zone" + '<br>')

        if weight_for_age['weight15'] <= weight < weight_for_age['weight25']:
            per ="Child is between 15 to 25 percentile zone"
          #  s.append("Child is between 15 to 25 percentile zone" + '<br>')

        if weight_for_age["weight25"] <= weight < weight_for_age['weight50']:
             per ="Child is between 25 to 50 percentile zone"
           # s.append("Child is between 25 to 50 percentile zone" + '<br>')

        if weight >= weight_for_age['weight50']:
            per ="Child is above the 50 percentile zone"
           # s.append("Child is above the 50 percentile zone" + '<br>')

    for i in range(13 - int(age)):
        new_age = int(age) + i + 1
        new_weight = weight + ((i + 1) * 7 * 0.045)
        weight_3month = weight + ((12 - int(age)) * 7 * 0.045)
        if gender == 'boy':
            st = 'Child is healthy'
            sta=''
            stb=''
            if weight < data_boy[age]['weight25']:
                if new_weight >= data_boy[str(new_age)]['weight25']:
                    #print(
                     #   f"A healthy born child gains around {data_girl[age]['gram/day']} gram per day when he is {age} weeks old")
                    #print(
                     #   f"If the child gains 45 gram per day, he will reach LIGHT GREEN zone at age of {int(age) + i + 1} weeks")
                    #print(f"If the child gains 45 gram per day, at age of 3 months, he will be {weight_3month} kg")
                    st="A healthy born child gains around "+str(data_boy[age]['gram/day'])+" gram per day when he is "+str(age)+" weeks old"
                    sta="If the child gains 45 gram per day, he will reach LIGHT GREEN zone at age of "+str(int(age) + i + 1)+ " weeks"
                    stb="If the child gains 45 gram per day, at age of 3 months, he will be "+ str(weight_3month) +" kg"
                    break
        if gender == 'girl':
            st='Child is healthy'
            sta=''
            stb=''
            if weight < data_girl[age]['weight25']:
                if new_weight >= data_girl[str(new_age)]['weight25']:
                  #  print(
                  #      f"A healthy born child gains around {data_girl[age]['gram/day']} gram per day when he is {age} weeks old")
                  #  print(
                  #      f"If this child gains 45 gram per day, he will reach LIGHT GREEN zone at age of {int(age) + i + 1} weeks")
                 #   print(f"If the child gains 45 gram per day, at age of 3 months, she will be {weight_3month} kg")
                    st = "A healthy born child gains around " + str(data_girl[age]['gram/day']) + " gram per day when she is " + str(age) + " weeks old"
                    sta = "If the child gains 45 gram per day, she will reach LIGHT GREEN zone at age of " + str(int(age) + i + 1) + " weeks"
                    stb = "If the child gains 45 gram per day, at age of 3 months, she will be " + str( weight_3month) + " kg"
                    break

    for i in range(13 - int(age)):
        new_age = int(age) + i + 1
        new_weight = weight + ((i + 1) * 7 * 0.050)
        weight_3month = weight + ((12 - int(age)) * 7 * 0.050)
        if gender == 'boy':
            if weight < data_boy[age]['weight25']:
                if new_weight >= data_boy[str(new_age)]['weight25']:

                    b1= "If the child gains 50 gram per day, he will reach LIGHT GREEN zone at age of " +str(int(age) + i + 1)+" weeks"
                    b2= "If the child gains 50 gram per day, at age of 3 months, he will be "+str(weight_3month) +"kg"
                    break
        if gender == 'girl':
            if weight < data_girl[age]['weight25']:
                if new_weight >= data_girl[str(new_age)]['weight25']:
                    b1= "If this child gains 50 gram per day, she will reach LIGHT GREEN zone at age of "+str(int(age) + i + 1)+" weeks"
                    b2= "If the child gains 50 gram per day, at age of 3 months, she will be "+ str(weight_3month)+" kg"
                    break

    new_weight = weight + ((12 - int(age)) * 7 * 0.030)
    if gender == 'boy':
        a="If the child gains 30 gram per day, at age of 3 months, he will be "+str(new_weight)+" kg"
        b="Average weight of a boy child at age of 3 months is 6.2 kg "
        c="Weight for light green zone of a boy child at age of 3 months is 5.7 kg "

    elif gender == 'girl':
        #print(f"If the child gains 30 gram per day, at age of 3 months, she will be {new_weight} kg")
        #print(f"Average weight of a girl child at age of 3 months is 5.7 kg ")
        #print(f"Weight for light green zone of a girl child at age of 3 months is 5.2 kg ")
        a = "If the child gains 30 gram per day, at age of 3 months, she will be " + str(new_weight) + " kg"
        b = "Average weight of a girl child at age of 3 months is 5.7 kg "
        c = "Weight for light green zone of a girl child at age of 3 months is5.2 kg "

    new_weight = weight + ((12 - int(age)) * 7 * 0.040)
    if gender == 'boy':
        a1 = "If the child gains 40 gram per day, at age of 3 months, he will be " + str(new_weight) + " kg"
       # b = "Average weight of a boy child at age of 3 months is 6.2 kg "
       # c = "Weight for light green zone of a boy child at age of 3 months is 5.7 kg "

    elif gender == 'girl':
        a1 = "If the child gains 30 gram per day, at age of 3 months, she will be " + str(new_weight) + " kg"
      #  b = "Average weight of a girl child at age of 3 months is 5.7 kg "
       # c = "Weight for light green zone of a girl child at age of 3 months is5.2 kg "

        op='Zone: '+ zone + '<br>'+ 'Weight gain to reach Light Green (Safe) Zone: ' + str(wlg) + '<br>' + 'Average weight of child in the age group: ' + str(avg) + '<br>'
        op1=per+'<br>'+ st + '<br>' + sta + '<br>' + stb + '<br>' +  a + '<br>' + a1 + '<br>' + b +'<br>' + c
        oo=op+op1
        return oo

    # c=to reach average weight for his age group at age of ----- done
    # also put percentile ------ done
    # standard deviation, (muw or suw) (suw < - 3)
    # not just 45 gram, also 50 gram, 40 gram, standard notation
    # growth faultering 25 gram


