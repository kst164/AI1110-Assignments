#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

const int COUNT = 1000000;

int main() {
  srand(time(0));

  for (int i = 0; i < COUNT; i++) {
    double r = 0;
    for (int j = 0; j < 12; j++) {
      double t = (double) rand() / RAND_MAX;
      r += t;
    }
    r -= 6;
    printf("%lf\n", r);
  }
  return 0;
}
