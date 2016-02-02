/*
 * ID_3.cpp
 *
 *  Created on: Jan 30, 2016
 *      Author: Luke
 */

#include <iostream>

using namespace std;
//I know i'm not going to use anything but standard

int MymainMAN() {

	long count;
	long sample;
	long prevPrime;

	cin >> sample;

	for (count = 1; sample >= count + 1; count++) {
		if (sample % count == 0) {
			if (sample % prevPrime){

				cout << count << " Dividable" << endl;
			}
			else{

			}


	}
	else {

		cout << count << " Not Dividable" << endl;

	}
}


return 0;
}

