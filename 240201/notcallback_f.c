#include <stdio.h>
#include <wiringPi.h>

int main(void) {
	const int button_pin = 3;
	const int led_pin = 1;
	int button_state = LOW;
	int last_button_state = LOW;

	if (wiringPiSetup() == -1)
		return 1;

	pinMode(button_pin, INPUT);
	pinMode(led_pin, OUTPUT);

	while (1) {
		button_state = digitalRead(button_pin);

		if (button_state == HIGH && last_button_state == LOW) {
			digitalWrite(led_pin, (digitalRead(led_pin) == HIGH) ? LOW : HIGH);
		}

		last_button_state = button_state;

		delay(100);
	}

	return 0;
}
