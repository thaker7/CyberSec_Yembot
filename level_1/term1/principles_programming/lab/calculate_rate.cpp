// program Consisting four-degrees of materials

#include <iostream>
using namespace std ;

int main() {

float m1 , m2 , m3 , m4  ;

cout << " The First materials mark : "	;
cin >> m1	;
cout << "\n The Second materials mark : "	;
cin >> m2	;
cout << "\n The Third materials mark : "	;
cin >> m3	;
cout << "\n The Fourth materials mark : "	;
cin >> m4	;

float avg =	(m1 + m2 + m3 + m4) / 4	;
cout << "\n The Rate : " << avg <<	endl	;

system("pause")	;
return 0 ;
}