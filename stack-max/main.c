#include <stdio.h>
#include <stdlib.h>

#define PUSH 1
#define DELETE 2
#define PRMAX 3

int getint() {
  int x;
  int ret = scanf("%d", &x);
  if (ret == 0 || ret == EOF)
    exit(0);
  return x;
}

void frame(int max) {
  for (;;) {
    int op = getint();
    if (op == PUSH) {
      int x = getint();
      frame(x > max ? x : max);
    } else if (op == DELETE) {
      return;
    } else if (op == PRMAX) {
      printf("%d\n", max);
    }
  }
}

int main() {
  getint();
  frame(-1);
}
