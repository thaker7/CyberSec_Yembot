// 7)	program do Swap between Two variable

#include <iostream>
using namespace std ;

int main()
{
int num1 , num2 , temp ;

cout <<	" Value Number 1: ";
cin >>	num1 ;

cout <<	" Value Number 2: ";
cin >>	num2 ;

temp = num1 ;
num1 = num2 ;
num2 = temp ;

cout <<	"\n \t After Swapping Values" << endl ;
cout <<	" Value of Number 1: " << num1 << endl ;
cout <<	" Value of Number 2: " << num2 << endl ;

system("pause")	;
return 0 ;
}