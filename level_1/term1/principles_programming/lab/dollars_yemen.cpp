//program calculated the amount in dollars and Yemen

#include <iostream>
using namespace std	;

int main()	{
	
	cout << "\n\n One Dollar = 1200 real Yemeni"	;
	
	int amount_of_dollar	;
	cout << "\n\n The amount of the dollar: "	;
	cin >> amount_of_dollar	;
	
	int amount_of_yemeni =	amount_of_dollar * 1200	;
	cout << "\n\n The amount of the yemeni : "  << amount_of_yemeni << endl	;
	
	system("pause")	;
	return 0	;
	
}