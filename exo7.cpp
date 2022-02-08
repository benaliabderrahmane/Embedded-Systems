#include <SenseHat.h>
#include <iostream>
#include <string>

using namespace std;

int main() {
	SenseHat sense;
	float x,y,z;
	int theta;
	sense.Effacer();
	sense << setcouleur(carte.ConvertirRGB565(0,100,0));
	while(1){
		sense.ObtenirAcceleration(x,y,z);
		if(x < -0.8) {theta = 270;}
		if(x > 0.8 ) {theta = 90;}
		if(y < -0.8) {theta = 180;}
		if(y > 0.8 ) {theta = 0;}
		
		cout << "Temperature : " << sense.ObtenirTemperature() << endl;
		sense << setrotation(theta) << "I am sending" << flush;
		sleep(1);
		}
		return 0;
		}
