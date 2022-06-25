#include <stdio.h>

int main() {
  int count = 0;
  double sum = 0;
  double sq_sum = 0;

  double val;

  while (scanf("%lf", &val) != EOF) {
    count += 1;
    sum += val;
    sq_sum += val * val;
  }

  double mean = sum / count;
  double sq_mean = sq_sum / count;
  double variance = sq_mean - mean * mean;

  printf("Mean    : %lf\n", mean);
  printf("Variance: %lf\n", variance);
  return 0;
}
