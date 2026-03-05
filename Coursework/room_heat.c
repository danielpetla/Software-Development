#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

bool check_if_covered(int **pipes, int *pipe_sizes, int n, int k, int *selected_indices) {

    bool *heated = calloc(n + 1, sizeof(bool));  // array to track if a room x is heated
    int total_covered = 0;

    for (int i = 0; i < k; i++) {
            int p_idx = selected_indices[i];  // which pipe is being observed

            for (int j = 0; j < pipe_sizes[p_idx]; j++) {
                int room = pipes[p_idx][j];
                if (!heated[room]) {
                    heated[room] = true;
                    total_covered++;
            }
        }
    }

    free(heated);
    return (total_covered == n);
}

bool find_solution(int **pipes, int *pipe_sizes, int m, int n, int k, int start_idx, int current_k, int *selected) {

    // base case: picked exactly 'k' pipes, check
    if (current_k == k) {
        return check_if_covered(pipes, pipe_sizes, n, k, selected);
    }

    // try picking the next pipe, starting from 'start_idx'
    for (int i = start_idx; i < m; i++) {
        selected[current_k] = i;  // Pick pipe 'i'

        // recursively try to pick the remaining pipes
        if (find_solution(pipes, pipe_sizes, m, n, k, i + 1, current_k + 1, selected)) {
            return true;  // found a winning combination, stop searching
        }
    }

    return false;  // no combination worked
}

int main(){
    int n, m, k;

    // getting initial configuration
    if (scanf("%d %d %d", &n, &m, &k) != 3)
        return 1;

    int **pipes = malloc(m * sizeof(int *));     // array pointer to the rooms of each pipe
    int *pipe_sizes = malloc(m * sizeof(int));  // array pointer to the number of rooms connected to a pipe


    for (int i = 0; i < m; i++) {
        int num_rooms;
        scanf("%d", &num_rooms);  // reading the number of rooms connected to the pipe

        pipe_sizes[i] = num_rooms;
        pipes[i] = malloc(num_rooms * sizeof(int));

        for (int j = 0; j < num_rooms; j++) {
            scanf("%d", &pipes[i][j]);  // reading the rooms numbers (e.g. room 1 and room 2)

        }

    }

    int *selected_indices = malloc(k * sizeof(int)); // array to hold current guess

    // start search
    if (find_solution(pipes, pipe_sizes, m, n, k, 0, 0, selected_indices)) {
            printf("Yes\n");
        } else {
            printf("No\n");
        }

        // cleanning up memory
        for (int i = 0; i < m; i++) {
            free(pipes[i]);
        }
        free(pipes);
        free(pipe_sizes);
        free(selected_indices);

        return 0;
}
