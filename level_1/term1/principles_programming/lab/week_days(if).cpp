#include <iostream>
using namespace std;

int main()
{
	int day_number;
	cout	<<	" Enter a Week Number: ";
	cin >> day_number;
	
	if (day_number==1)
	{ cout << " The Day is Saturday" <<	endl; }
	
	else if (day_number==2)
	{ cout << " The Day is Sunday" <<	endl; }
	
	else if (day_number==3)
	{ cout << " The Day is Monday" <<	endl; }
	
	else if (day_number==4)
	{ cout << " The Day is Tuesday" <<	endl; }
	
	else if (day_number==5)
	{ cout << " The Day is Wednesday" <<	endl; }
	
	else if (day_number==6)
	{ cout << " The Day is Thursday" <<	endl; }
	
	else if (day_number==7)
	{ cout << " The Day is Friday" <<	endl; }
	
	else
	cout << "!! Please Enter a week-number between (1-7) !!" <<	endl;

	system("pause");
	return 0;
}