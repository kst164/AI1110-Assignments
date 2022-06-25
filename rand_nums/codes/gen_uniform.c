#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

const int COUNT = 1000000;

int main() {
  srand(time(0));

  for (int i = 0; i < COUNT; i++) {
    double r = (double) rand() / RAND_MAX;
    printf("%lf\n", r);
  }
  return 0;
}
