#include <stdio.h>

#define MAX_ITEMS 100

int n;
int weight[MAX_ITEMS], value[MAX_ITEMS];
int max_weight;
int max_value = -1;

void knapsack_branch_bound(int level, int cur_weight, int cur_value) {
    if (cur_weight > max_weight) {
        return;
    }
    if (cur_value > max_value) {
        max_value = cur_value;
    }
    if (level == n) {
        return;
    }
    knapsack_branch_bound(level + 1, cur_weight, cur_value);
    knapsack_branch_bound(level + 1, cur_weight + weight[level], cur_value + value[level]);
}

int main() {
    printf("Enter the number of items: ");
    scanf("%d", &n);
    printf("Enter the weight and value of each item:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &weight[i], &value[i]);
    }
    printf("Enter the maximum weight of the knapsack: ");
    scanf("%d", &max_weight);
    knapsack_branch_bound(0, 0, 0);
    printf("Maximum value: %d\n", max_value);
    return 0;
}
