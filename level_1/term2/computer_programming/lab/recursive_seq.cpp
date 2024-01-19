// Cyber Security
// Omer Khalid Bawazeer

#include <iostream>
#include <math.h>
using namespace std;
// Program to Print Numbers From num to 1

void recursive_seq(int num) // LOCAL
{
    for (int i = num; i >= 1; i--)
        cout << " " << i;
}

int main()
{
    int number;
    cout << "\n How Many Numbers to Print: ";
    cin >> number;
    cout << " The Numbers Printed From " << number << " to 1 is: ";
    recursive_seq(number);
    cout << "\n\n\t\t";

    return 0;
}

// Omer Khalid Bawazeer
// Cyber Security