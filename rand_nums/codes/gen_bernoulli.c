#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

const int COUNT = 1000000;

int main() {
  srand(time(0));

  for (int i = 0; i < COUNT; i++) {
    int r = (rand() % 2) ? 1 : -1;
    printf("%d\n", r);
  }
  return 0;
}
