#include <iostream>
using namespace std;
int main()
{
	float degree;
	cout <<	"Enter Your Degree: ";
	cin >>	degree;
	
	if (degree <= 100 && degree >=	90)
	    cout << "Excellent" <<endl;
	
	else if (degree < 90 && degree >= 80)
	    cout << "Very Good" <<endl;
	
        else if (degree < 80 && degree >= 70)
	    cout << "Good" <<endl;
	
	else if (degree < 70 && degree >= 60)
	    cout << "Passable" <<endl;
	
	else if (degree < 60 && degree >= 50)
	    cout << "Weak" <<endl;
	
	else if (degree < 50 && degree >= 0)
	    cout << "Fail" <<endl;
	
	else
	    cout << " !!! Please Enter Your Degree correctly !!! " <<endl;
	
  system("pause");
   return 0;
}