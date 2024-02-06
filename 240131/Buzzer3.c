#include <stdio.h>
#include <wiringPi.h>

int main(void) {
	const int buzzer_pin = 1;

	wiringPiSetup();

	pinMode(buzzer_pin, PWM_OUTPUT);

	pwmSetClock(19);
	pwmSetMode(PWM_MODE_MS);

	int cnt;
	for(cnt=0; cnt<=2; cnt++) {
		pwmSetRange(1000000/262);
		pwmWrite(buzzer_pin, 1000000/262/2);
		delay(1000);
		pwmSetRange(1000000/294);
		pwmWrite(buzzer_pin, 1000000/294/2);
		delay(1000);
	}
	pwmWrite(buzzer_pin, 0);
}

