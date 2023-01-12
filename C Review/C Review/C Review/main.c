//
//  main.c
//  C Review
//
//  Created by mystic on 2023/01/07.
//

#include <stdio.h>

char* createstr() {
    static char result[10] = "hello";
    return result;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    char* result = createstr();
    printf("%s", result);
    return 0;
}
