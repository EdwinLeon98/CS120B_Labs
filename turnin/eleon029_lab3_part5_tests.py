#      Author & Email: Edwin M. Leon Du, eleon029@ucr.edu
#      Partner(s) Name: 
#      Lab Section: 23
#      Assignment: Lab 3  Exercise 5
#      Exercise Description: Weigth sensor, combining input pins and output pins exercise tests
#
#      I acknowledge all content contained herein, excluding template or example
#      code, is my own original work.
#
# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
tests = [ {'description': 'PIND: 0xFF , PINB: 0x01 => PORTB: 0x02',    
    'steps': [ {'inputs': [('PIND',0xFF), ('PINB',0x01)], 'iterations': 5 } ],
    'expected': [('PORTB',0x02)],
    },
    {'description': 'PIND: 0x1B , PINB: 0x01 => PORTB: 0x04',
    'steps': [ {'inputs': [('PIND',0x1B), ('PINB',0x01)], 'iterations': 5 } ],
    'expected': [('PORTB',0x04)],
    },
    {'description': 'PIND: 0x01 , PINB: 0x01 => PORTB: 0x00',
    'steps': [ {'inputs': [('PIND',0x01), ('PINB',0x01)], 'iterations': 5 } ],
    'expected': [('PORTB',0x00)],
    },
    {'description': 'PIND: 0x23 , PINB: 0x00 => PORTB: 0x00',
    'steps': [ {'inputs': [('PIND',0x23), ('PINB',0x00)], 'iterations': 5 } ],
    'expected': [('PORTB',0x02)],
    },
    ]

#watch = ['cntavail']

# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
#watch = ['<function>::<static-var>','PORTB']

