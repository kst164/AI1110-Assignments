#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

const int COUNT = 1000000;

int main() {
  srand(time(0));

  for (int i = 0; i < COUNT; i++) {
    double u1 = (double) rand() / RAND_MAX;
    double u2 = (double) rand() / RAND_MAX;
    double t = u1 + u2;
    printf("%lf\n", t);
  }
  return 0;
}
