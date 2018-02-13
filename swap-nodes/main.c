#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int val;
    struct node *left;
    struct node *right;
} node;

node *make(int val, node *left, node *right) {
    node *n = malloc(sizeof(node));
    n->val = val;
    n->left = left;
    n->right = right;
    return n;
}

void swapAtLevel(node *n, int k, int depth) {
    if (depth % k == 0) {
        node *tmp = n->left;
        n->left = n->right;
        n->right = tmp;
    }

    if (n->left)
        swapAtLevel(n->left, k, depth+1);
    if (n->right)
        swapAtLevel(n->right, k, depth+1);
}

char *printInOrder(node *n) {
    char *left = NULL, *mid, *right = NULL;
    if (n->left)
        left = printInOrder(n->left);
    asprintf(&mid, "%d", n->val+1);
    if (n->right)
        right = printInOrder(n->right);
    char *res;
    asprintf(&res, "%s%s%s%s%s", left ? left : "", left ? " " : "", mid, right ? " " : "", right ? right : "");
    if (left) free(left);
    if (right) free(right);
    return res;
}

int main() {
    int n;
    scanf("%d", &n);

    node *nodes[n];
    for (int i = 0; i < n; ++i)
        nodes[i] = make(i, NULL, NULL);

    for (int i = 0; i < n; ++i) {
        int l, r;
        scanf("%d %d", &l, &r);
        nodes[i]->left = (l == -1 ? NULL : nodes[l-1]);
        nodes[i]->right = (r == -1 ? NULL : nodes[r-1]);
    }

    int swaps;
    scanf("%d", &swaps);

    for (int i = 0; i < swaps; ++i) {
        int k;
        scanf("%d\n", &k);
        swapAtLevel(nodes[0], k, 1);
        printf("%s\n", printInOrder(nodes[0]));
    }
}
