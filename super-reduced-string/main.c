#include <stdio.h>
#include <stdbool.h>
#include <string.h>

void reduce(char *str) {
    for (int i = 0; str[i+1] != '\0'; ++i) {
        //printf("checking if str[%d] = '%c'  == str[%d] = '%c'\n", i, str[i], i+1, str[i+1]);
        if (str[i] == str[i+1]) {
            //printf("yes, memmove(%d, %d, %d)\n", i+1, i+3, strlen(&str[i+3])+1);
            memmove(&str[i], &str[i+2], strlen(&str[i+2])+1);
            //printf("new string: %s\n", str);
            i -= 2;
        }
    }
}

int main() {
    char str[101];
    fgets(str, 101, stdin);
    //printf("got [%s]\n", str);

    reduce(str);

    if (strlen(str) == 0)
        puts("Empty String");
    else
        puts(str);
}
