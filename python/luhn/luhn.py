"""
Luhn

Given a number determine whether or not it is valid per the Luhn formula.

The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers and Canadian Social Insurance Numbers.

The task is to check if a given string is valid.

Validating a Number
Strings of length 1 or less are not valid. Spaces are allowed in the input, but they should be stripped before checking. All other non-digit characters are disallowed.

Example 1: valid credit card number
4539 1488 0343 6467
The first step of the Luhn algorithm is to double every second digit, starting from the right. We will be doubling

4_3_ 1_8_ 0_4_ 6_6_
If doubling the number results in a number greater than 9 then subtract 9 from the product. The results of our doubling:

8569 2478 0383 3437
Then sum all of the digits:

8+5+6+9+2+4+7+8+0+3+8+3+3+4+3+7 = 80
If the sum is evenly divisible by 10, then the number is valid. This number is valid!

Example 2: invalid credit card number
8273 1232 7352 0569
Double the second digits, starting from the right

7253 2262 5312 0539
Sum the digits

7+2+5+3+2+2+6+2+5+3+1+2+0+5+3+9 = 57
57 is not evenly divisible by 10, so this number is not valid.

Exception messages
Sometimes it is necessary to raise an exception. When you do this, you should 
include a meaningful error message to indicate what the source of the error is. 
This makes your code more readable and helps significantly with debugging. 
Not every exercise will require you to raise an exception, but for those that 
do, the tests will only pass if you include a message.

To raise a message with an exception, just write it as an argument to the 
exception type. For example, instead of raise Exception, you should write:

raise Exception("Meaningful message indicating the source of the error")


"""


class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        number = self.num_list(self.card_num)
        if number == False:
            return False
        total = 0
        
        for i in range(0, len(number), 2):
            
            if i % 2 == 0:
                number[i] = number[i] * 2
                if i > 9:
                    number[i] = number[i] - 9
        total += i
        if total % 10 == 0:
            return True 
        else:
            return False
                
    
    
    
    
    def num_list(self, card_num):
        
        card_num = card_num.strip() #removes any whitespace
        converted_num = []
        
        if len(card_num) < 2:
            return False
        else:
            for i in card_num:
                if i.isnumeric():
                    #faster than prepending to an array 
                    # (and then not having to reverse the array)
                    converted_num.append(int(i)) 
                    
                elif i != " ":
                    return False
                
        return converted_num
    
    
                