#include <stdio.h>
#include <stdbool.h>

#define MAX_N 100

int n;
int cols[MAX_N];

bool is_safe(int row, int col) {
    for (int i = 0; i < row; i++) {
        if (cols[i] == col || abs(cols[i] - col) == abs(i - row)) {
            return false;
        }
    }
    return true;
}

void print_solution() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (cols[i] == j) {
                printf("Q ");
            } else {
                printf(". ");
            }
        }
        printf("\n");
    }
    printf("\n");
}

void n_queens_util(int row) {
    if (row == n) {
        print_solution();
        return;
    }
    for (int col = 0; col < n; col++) {
        if (is_safe(row, col)) {
            cols[row] = col;
            n_queens_util(row + 1);
        }
    }
}

void n_queens() {
    n_queens_util(0);
}

int main() {
    printf("Enter the number of queens: ");
    scanf("%d", &n);
    n_queens();
    return 0;
}
