#include <stdio.h>
#include <stdbool.h>

#define MAX_SIZE 10

int n;
int preferences[MAX_SIZE][MAX_SIZE];
int men_match[MAX_SIZE];
int women_match[MAX_SIZE];
bool men_free[MAX_SIZE];

void stable_marriage() {
    for (int i = 0; i < n; i++) {
        men_free[i] = true;
        men_match[i] = -1;
        women_match[i] = -1;
    }
    int num_free_men = n;
    while (num_free_men > 0) {
        int m;
        for (m = 0; m < n; m++) {
            if (men_free[m]) {
                break;
            }
        }
        for (int i = 0; i < n && men_free[m]; i++) {
            int w = preferences[m][i];
            if (women_match[w] == -1) {
                women_match[w] = m;
                men_match[m] = w;
                men_free[m] = false;
                num_free_men--;
            } else {
                int m1 = women_match[w];
                if (preferences[w][m] < preferences[w][m1]) {
                    women_match[w] = m;
                    men_match[m] = w;
                    men_free[m] = false;
                    men_free[m1] = true;
                }
            }
        }
    }
}

int main() {
    printf("Enter the number of men/women (max 10): ");
    scanf("%d", &n);

    printf("Enter the preferences of men: \n");
    for (int i = 0; i < n; i++) {
        printf("Preferences of man %d: ", i+1);
        for (int j = 0; j < n; j++) {
            scanf("%d", &preferences[i][j]);
        }
    }

    printf("Enter the preferences of women: \n");
    for (int i = 0; i < n; i++) {
        printf("Preferences of woman %d: ", i+1);
        for (int j = 0; j < n; j++) {
            scanf("%d", &preferences[j][i]);
        }
    }

    stable_marriage();

    printf("Stable matching:\n");
    for (int i = 0; i < n; i++) {
        printf("Man %d matched with woman %d\n", i+1, men_match[i]+1);
    }

    return 0;
}
