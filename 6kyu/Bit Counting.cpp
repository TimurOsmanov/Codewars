// Write a function that takes an integer as input, and returns the number of bits that are equal
// to one in the binary representation of that number. You can guarantee that input is non-negative.
// Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
#include <iostream>
#include <string>
using namespace std;

unsigned int countBits(unsigned long long n)
{
    long long int_div = n / 2;
    int int_div_rest = n % 2;
    int counter = 0;
    if (int_div_rest == 1){
            counter += 1;
        }

    while (int_div != 0)
    {
        int_div_rest = int_div % 2;
        int_div /= 2;
        if (abs(int_div_rest) == 1){
            counter += 1;
        }
    }
    return counter;
}

int main ()
{
     unsigned long long input;
     cin >> input;
     cout << countBits(input);
    return 0;
}