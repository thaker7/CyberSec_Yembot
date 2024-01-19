// Cyber Security
// Omer Khalid Bawazeer

#include <iostream>
using namespace std;
// Program to Calculate The Power of any Number

int recursive_pwr(int base, int exponent) // LOCAL
{
    if (exponent == 0)
        return 1;

    return base * recursive_pwr(base, exponent - 1);
}

int main()
{
    int num_1, num_2;
    cout << "\n Enter The Base Value: ";
    cin >> num_1;
    cout << " Enter The Exponent: ";
    cin >> num_2;
    cout << "\n The Result is: " << recursive_pwr(num_1, num_2) << "\n\n";

    return 0;
}

// Omer Khalid Bawazeer
// Cyber Security