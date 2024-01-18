
#include <iostream>
using namespace std;
int main()
{
	int day_number;
	cout	<<	" Enter a Week Number: ";
	cin >> day_number;
	
	switch (day_number)
	{
	case 1: cout << " The Day is Saturday" <<endl;
								break;
	
	case 2: cout << " The Day is Sunday" <<endl;
								break;
	
	case 3: cout << " The Day is Monday" <<endl;
								break;
	
	case 4: cout << " The Day is Tuesday" <<endl;
								break;
	
	case 5: cout << " The Day is Wednesday" <<endl;
								break;
	
	case 6: cout << " The Day is Thursday" <<endl;
								break;
	
	case 7: cout << " The Day is Friday" <<endl;
								break;
	
	default:
	cout << "!! Please Enter a week-number between (1-7) !!" <<	endl;	}
	
	system("pause");
	return 0;
}