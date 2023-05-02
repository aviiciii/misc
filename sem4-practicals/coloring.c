#include <stdio.h>
#include <stdbool.h>

#define MAX_COLORS 2

int graph[3][3] = {
    {0, 1, 1},
    {1, 0, 1},
    {1, 1, 0}
};

int colors[3];

bool is_safe(int node, int color) {
    for (int i = 0; i < 3; i++) {
        if (graph[node][i] && colors[i] == color) {
            return false;
        }
    }
    return true;
}

bool graph_coloring_util(int node) {
    if (node == 3) {
        return true;
    }
    for (int color = 1; color <= MAX_COLORS; color++) {
        if (is_safe(node, color)) {
            colors[node] = color;
            if (graph_coloring_util(node + 1)) {
                return true;
            }
            colors[node] = 0;
        }
    }
    return false;
}

void graph_coloring() {
    if (graph_coloring_util(0)) {
        printf("Node 0: Color %d\n", colors[0]);
        printf("Node 1: Color %d\n", colors[1]);
        printf("Node 2: Color %d\n", colors[2]);
    } else {
        printf("The graph cannot be colored with %d colors.\n", MAX_COLORS);
    }
}

int main() {
    graph_coloring();
    return 0;
}
