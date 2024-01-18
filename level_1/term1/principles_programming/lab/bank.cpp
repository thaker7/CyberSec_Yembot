#include <iostream>
#include <string>
using namespace std;
int main () {
	
	int pass ;
	string user;
	cout <<	"\t Sign in to your account :" <<endl <<endl ;
	cout <<	"Enter UserName: " ;	cin >>	user ;
	cout <<	"Enter Password: " ;	cin >>	pass ;
	
	if (user=="omer"	&&	pass==12345) {
		cout <<	"\t Welcome to your account √" <<endl <<endl;
		
		int select;	// Number process
		cout <<"Select the process you want to do: \n 1) Deposit money for your account→Enter 1\n 2) Query on the balance → Enter 2\n 3) Sign out  →  Enter 3" <<endl;
		cout <<	"The Select is: " ;	cin >>	select;
		
		int n=10000;	// Money before deposit
		int deposit ;
		
// 1) For Deposit Money
		if (select==1) {
			cout <<	"\nThere is now in your account: " <<	n <<endl<<endl ;
			cout <<	"Enter the money you want to deposit: " ;
			cin >> deposit;
			cout <<	"\t The deposit was successfully √" <<endl<<endl;
			
			cout <<	"The Select is (2 or 3): " ;	cin >>	select;
			// For Query on Money After Deposit
			if (select==2) {
  	    int total =	n + deposit ;
				cout <<	"The total value of your account now is: " << total	<<endl <<endl ;
			}
			// For Sign out ( EXIT )
			else if (select==3) {
    	  cout <<	"\n\t Successfully logged out √" <<endl <<endl ;
			}
		}
		
// 2) For Query on Money current ( Before Deposit )
		else if (select==2) {
			cout <<	"\nThere is now in your account: " << n	<<endl ;
			
			cout <<	"The Select is (1 or 3): " ;	cin >>	select;
			// For Deposit Money After Query
			if (select==1) {
				cout <<	"\nEnter the money you want to deposit: " ;
		  	cin >> deposit;
		  	int total =	n + deposit ;
		  	cout <<	"The total value of your account now is: " << total	<<endl <<endl;  	
			}
			// For Sign out ( EXIT )
			else if (select==3) {
		  	cout <<	"\n\t Successfully logged out √" <<endl <<endl ;
			}
		}
		
// 3) For Sign out ( EXIT → Out of the program)
		else if (select==3) {
			cout <<	"\n\t Successfully logged out √" <<endl <<endl ;
		}
	}
	
	else cout <<	"\n\t Error!! Try Again Please …" <<endl <<endl ;
	
	system("pause");
	return 0;
}