// program read ( length , width ) for user then calculate ( perimeter , area )

#include <iostream>
using namespace std ;
int main()
{
	int length , width , perimeter , area ;
	
	cout <<	"Enter The Length: " ;
	cin >>	length ;
	cout <<	"Enter The Width: " ;
	cin >>	width ;
	
	perimeter = 2 * ( length +width ) ;
  area = length * width  ;
  
	cout <<	"\nThe Perimeter = " << perimeter << endl ;
	cout <<	"The Area = " << area << endl ;
	
	system("pause") ;
	return 0 ;
}