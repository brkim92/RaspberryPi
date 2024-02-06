#include <stdio.h>
#include <wiringPi.h>
#include <pthread.h>

void *t1_function(void *arg) {
    while (1) {
        printf("\tt1\n");
        delay(500);
    }
    return NULL;
}

int main(void) {
    wiringPiSetup();

    pthread_t t1;

    if (pthread_create(&t1, NULL, t1_function, NULL) != 0) {
        fprintf(stderr, "스레드 생성 오류\n");
        return 1;
    }

    while (1) {
        printf("main\n");
        delay(1000);
    }

    return 0;
}
