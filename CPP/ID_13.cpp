/*
 * ID_13.cpp
 *
 *  Created on: Feb 1, 2016
 *      Author: Luke
 */

#include <iostream>

using namespace std;

int main() {

	string largeNumb;
	long digit;
	long outdig;
	long sum;
	long cintotal;
	long goTill;

	cout << "Please tell me how many line of numbers are you going to input?" << endl;
	cin >> goTill;
	cout << "If you answered anything more that one, just paste all of it in." << endl << "Have fun putting in your large number";
	goTill = goTill++;
	for (cintotal = 0; cintotal < goTill; cintotal++){
	cin >> largeNumb;

	for (digit = 0; digit < largeNumb.size(); digit++) {
		largeNumb.at(digit) >= '0' && largeNumb.at(digit) <= '57';
		outdig = largeNumb.at(digit) - 48;
		sum = sum + largeNumb.at(digit);
		cout << outdig << " " << sum << endl;

	}
	}

	return 0;
}
