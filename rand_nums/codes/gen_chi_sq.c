#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

const int COUNT = 1000000;

double gen_gau() {
  double r = 0;
  for (int j = 0; j < 12; j++) {
    double t = (double) rand() / RAND_MAX;
    r += t;
  }
  r -= 6;
  return r;
}

int main() {
  srand(time(0));

  for (int i = 0; i < COUNT; i++) {
    double x1 = gen_gau();
    double x2 = gen_gau();
    double chi_sq = x1*x1 + x2*x2;
    printf("%lf\n", chi_sq);
  }

  return 0;
}
