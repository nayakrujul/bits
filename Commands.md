# List of commands in Bits

## Strings

The following commands push their respective character to the top of the stack

#### Starting with `0`

* 000000 = '\n'
* 000001 = 'a'
* 000010 = 'b'
* ...
* 011010 = 'z'
* 011011 = '.'
* 011100 = ','
* 011101 = '!'
* 011110 = '?'
* 011111 = ' '
  
#### Starting with `10`

* 1000000 = '\t'
* 1000001 = 'A'
* 1000010 = 'B'
* ...
* 1010110 = 'Z'
* 1011011 = '@'
* 1011100 = '£'
* 1011101 = '$'
* 1011110 = '"'
* 1011111 = '\''

## Numbers

#### Starting with `110`

The following commands push the digits to the top of the stack

* 1100000 = 0
* 1100001 = 1
* 1100010 = 2
* 1100011 = 3
* 1100100 = 4
* 1100101 = 5
* 1100110 = 6
* 1100111 = 7
* 1101000 = 8
* 1101001 = 9

The following commands take the first two numbers from the stack and perform the relevant operation

* 1101010 = + (addition)
* 1101011 = - (subtraction)
* 1101100 = * (multiplication)
* 1101101 = / (division)
* 1101110 = % (modulus)
* 1101111 = ^ (exponentiation)

## Miscellaneous

#### Starting with `1110`

The following commands are keywords

* 11100000 = print
* 11100001 = input
* 11100010 = for
* 11100011 = endfor
* 11100100 = while True
* 11100101 = break
* 11100110 = if
* 11100111 = else
* 11101000 = endif

The following commands are for comparisons

* 11101001 = >
* 11101010 = >=
* 11101011 = <
* 11101100 = <=
* 11101101 = ==
* 11101110 = !=

The following command pushes a string to the top of the stack

* 11101111 = '='

## Logic gates

#### Starting with `11110`

The following commands perform their respective logic gate

* 1111000 = and
* 1111001 = or
* 1111010 = xor
* 1111011 = not

## Other strings

#### Starting with `111110`

The following commands push their respective character to the top of the stack

* 1111100000 = "0"
* 1111100001 = "1"
* 1111100010 = "2"
* 1111100011 = "3"
* 1111100100 = "4"
* 1111100101 = "5"
* 1111100110 = "6"
* 1111100111 = "7"
* 1111101000 = "8"
* 1111101001 = "9"
* 1111101010 = "+"
* 1111101011 = "-"
* 1111101100 = "*"
* 1111101101 = "/"
* 1111101110 = ">"
* 1111101111 = "<"

## ASCII characters

#### Starting with `1111110`

The following commands push their respective character to the top of the stack

* 11111100000000 = chr(0)
* 11111100000001 = chr(1)
* ...
* 11111101111111 = chr(127)

## Other functions

#### Starting with `11111110`

The following commands are functions

* 111111100 = chr
* 111111101 = ord

## Variables

#### Starting with `111111110`

Bits has 4 variables: A, B, C, D. You can get and set them.

* 111111110000 = set A
* 111111110001 = set B
* 111111110010 = set C
* 111111110011 = set D
* 111111110100 = get A
* 111111110101 = get B
* 111111110110 = get C
* 111111110111 = get D
