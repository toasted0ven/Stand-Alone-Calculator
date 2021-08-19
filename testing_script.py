# Testing script for the calculator


from calc_interface import *

test = {
    'decoder': True,
    'text_to_list': False
    }


decoder_test_set = {
    25: ['5', '^', '2'],
    0.49948135551: ['(', '(', 'sin', '(', '0.523', ')', ')', ')'],
    35: ['(', '(', '5', 'x', '7', ')', ')'],
    3: ['exp', '(', '1.09861228867', ')'],
    14: ['(', '(', '5', '-', '1', ')', 'x', '(', '6', '+', '1', ')', ')', '/', '(', '1', '+', '1', ')'],
    26: ['1', '+', '(', '5', 'x', '5', ')'],
    1: ['(', '7', 'x', '3', 'x', '5', '/', '4', ')', '^', '0'],
    5: ['sqrt', '(', '25', ')'],
    4: ['16', '^', '0.5'],
    7: ['(', '1', '+', '1', ')', 'x', '(', '1', '+', '1', ')', '+', '(', '4', '-', '1', ')', 'x', '1']
    }

def test_decoder():
    test_records = []
    print("Running tests for decoder")
    for i in decoder_test_set:
        try:
            ans = decoder(decoder_test_set[i])
            if ans == i:
                print('True')
                test_records.append([i, True])
            else:
                print(f'Error testing decoder using inputs: {i}, {decoder_test_set[i]}')
                print(f'expected output is {i}, output received {ans}')
                test_records.append([i, False])
        except:
            print('an error occured')
            test_records.append([i, 'error'])
    print("Summary of results for decoder")
    for a in test_records:
        print(f'Test {a[0]}, {a[1]}')





if __name__ == '__main__':
    if test['decoder']:
        test_decoder()
    if test['text_to_list']:
        test_text_to_list()
