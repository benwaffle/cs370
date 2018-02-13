#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define PUSH 1
#define DELETE 2
#define PRMAX 3

#define MAX(a, b) (a > b ? a : b)

int getint() {
  int x;
  int ret = scanf("%d", &x);
  if (ret == 0 || ret == EOF)
    exit(0);
  return x;
}

void frame(int max, int val) {
  while (1) {
    int op = getint();
    if (op == PUSH) {
      int x = getint();
      frame(MAX(x, max), x);
    } else if (op == DELETE) {
      return;
    } else if (op == PRMAX) {
      printf("%d\n", max);
    }
  }
}

int main() {
  getint();

  while (1) {
    int op = getint();
    assert(op == PUSH);
    if (op == PUSH) {
      int x = getint();
      frame(x, x);
    }
  }
}
