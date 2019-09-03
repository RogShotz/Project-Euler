/*
 * ID_2.cpp
 *
 *  Created on: Jan 29, 2016
 *      Author: Luke
 */

#include <iostream>

using namespace std;

int ROmain() {

	int sum = 1;
	int prevsum = 1;
	int count = 1;

	for (count = 1; count <= 10; count++) {

		if (count == 1) {
			cout << sum << "+" << prevsum << "=" << endl; //1+1
			sum = sum + prevsum;

		}

		else {
			prevsum = prevsum + sum;
			cout << prevsum << "+" << sum << "=" << endl;
			sum = sum + prevsum;
			cout << sum << "+" << prevsum << "=" << endl; //2+3

		}

	}

	return 0;
}
