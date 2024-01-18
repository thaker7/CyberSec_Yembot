

#include <iostream>
using namespace std ;
int main() 
{
	
	int a , b , z , w , x=2 , y=3 ;
	a = (5 + x / z) + (y / 2.7*w) ;
	b =	4.5 * (x + 2.3*y)*(x + 2.3*y) / (z + w) ;
	
	cout << "\n Finds Value a = (5 + x / z) + (y / 2.7*w) " ;
	cout << "\n Finds Value b = 4.5 * (x + 2.3*y)*(x + 2.3*y) / (z + w) " ;
	
	cout <<	"\n\n Enter Value z : " ;
	cin >>	z ;
	cout <<	" Enter Value w : " ;
	cin >>	w ;
	
	cout << "\n The Value a = " << a ;
	cout << "\n The Value b = " << b <<	endl ;
	
	system("pause") ;
	return 0 ;
}