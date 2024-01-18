#include <iostream>
using namespace std;

int main () {
	
	int a = 0 ;
	cout << "\t  Writte Number \n\n";
	cout << "Enter Number : \t";
	cin >> a;

	if (a%2==0)
	cout << "\n The Number is Marride (divide by 2) \n";

        else
	cout << "\n The Number is Single (Not divide by 2) \n";
	
	system("pause");
	return 0;
}