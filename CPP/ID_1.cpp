/*
* ID_1.cpp
*
*  Created on: Jan 29, 2016
*      Author: Luke
*/

#include <iostream>

using namespace std;

int CHOWmain() {

    int in = 1;
    int sum;

    for (in = 1; in < 1000; in++) {

        if (in % 3 == 0 || in % 5 == 0) {
            cout << in << endl;

            sum = sum + in;

        }

    }

    cout << sum;

    return 0;
}
