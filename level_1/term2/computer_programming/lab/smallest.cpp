// Cyber Security
// Omer Khalid Bawazeer

#include <iostream>
#include <math.h>
using namespace std;
// Program to Search for The Smallest Value in Araay

int smallest(int array[], int size) // LOCAL
{
    int smaller = array[0];
    for (int i = 0; i < size; i++)
        if (array[i] < smaller)
        {
            smaller = array[i];
        }

    return smaller;
}

int main()
{
    const int size_ = 5;
    int array_[size_];

    cout << " Enter 5 Values for Array: ";
    for (int i = 0; i < size_; i++)
        cin >> array_[i];

    cout << "\n The Smallest Number in Array is: " << smallest(array_, size_) << "\n\n";
    return 0;
}

// Omer Khalid Bawazeer
// Cyber Security