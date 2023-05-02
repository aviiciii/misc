#include <stdio.h>

#define MAX_CITIES 10
#define INF 99999

int min_cost = INF;
int n, visited[MAX_CITIES] = {0}, cost_matrix[MAX_CITIES][MAX_CITIES] = {{0}};

void tsp_branch_bound(int cost, int level, int node) {
    int i, j, temp;
    if (level == n && cost_matrix[node][0] != INF) {
        cost += cost_matrix[node][0];
        if (cost < min_cost)
            min_cost = cost;
        return;
    }
    for (i = 0; i < n; i++) {
        if (!visited[i] && cost_matrix[node][i] != INF) {
            visited[i] = 1;
            temp = cost_matrix[node][i];
            cost += temp;
            if (cost + (n - level) * temp < min_cost) // check if it's worth exploring
                tsp_branch_bound(cost, level + 1, i);
            visited[i] = 0;
            cost -= temp;
        }
    }
}

int main() {
    int i, j;
    printf("Enter the number of cities: ");
    scanf("%d", &n);
    printf("Enter the cost matrix:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &cost_matrix[i][j]);
            if (cost_matrix[i][j] == 0)
                cost_matrix[i][j] = INF;
        }
    }
    visited[0] = 1;
    tsp_branch_bound(0, 1, 0);
    printf("Minimum cost: %d\n", min_cost);
    return 0;
}
