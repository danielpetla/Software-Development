#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct {
    int length;
    char *text;
} Word;

int main() {
    int n, m;

    // getting the inital input
    if (scanf("%d %d", &n, &m) != 2)
        return 1;

    // memmory pointer to each n line and their contents
    char **n_grid = malloc(n * sizeof(char*));  // pointer to an array of pointers to arrays of strings

    // pointer to each m lines and their contents
    Word *word_list = malloc(m * sizeof(Word));

    // storing the contents of each of the n lines
    for (int i = 0; i < n; i++) {
        n_grid[i] = malloc((n + 1) * sizeof(char));  // in the position i of the array ther is a poiter to another array
        scanf("%s", n_grid[i]);  // reading and storing the strings
        }

    // storing the words and their sizes of each m line
    for (int i = 0; i < m; i++) {
        scanf("%d ", &word_list[i].length);

        word_list[i].text = malloc((word_list[i].length + 1) * sizeof(char));  // (+1 for the null terminator)
        scanf("%s", word_list[i].text);  // storing word
        }


    int total_mistakes = 0;

    // algorithm loop for every word
    for (int w = 0; w < m; w++) {
            int word_len = word_list[w].length;
            char *word_str = word_list[w].text;
            int min_mistake = 100;  // just initializing

            // the impossible case
            if (word_len > n) {
                printf("-1\n");
                goto cleanup;

            }

        // Left -> right
        for (int r = 0; r < n; r++) {  // r = row
            for (int c = 0; c <= n - word_len; c++) {  // c = column -> NOTE: c "range" changes beacuse different moviment requiers different space
                int mismatch = 0;
                for (int k = 0; k < word_len; k++) {  // k will "travel" trough the words and grid
                    if (tolower(n_grid[r][c + k]) != tolower(word_str[k])) mismatch++;
                }
                if (mismatch < min_mistake) min_mistake = mismatch;
            }
        }

        // Top -> bottom
        for (int r = 0; r <= n - word_len; r++) {  // r = row
            for (int c = 0; c < n; c++) {  // c = column
                int mismatch = 0;
                for (int k = 0; k < word_len; k++) {  // k will "travel" trough the words and grid
                    if (tolower(n_grid[r + k][c]) != tolower(word_str[k])) mismatch ++;
                }
                if (mismatch < min_mistake) min_mistake = mismatch;
            }
        }

        // Diagonal: left_top -> right_bot
        for (int r = 0; r <= n - word_len; r++) {  // r = row
            for (int c = 0; c <= n - word_len; c++) {  // c = column
                int mismatch = 0;
                for (int k = 0; k < word_len; k++) {  // k will "travel" trough the words and grid
                    if (tolower(n_grid[r + k][c + k]) != tolower(word_str[k])) mismatch ++;
                }
                if (mismatch < min_mistake) min_mistake = mismatch;

        }
        }

        // Diagonal: left_bot -> right_top
        for (int r = word_len - 1; r < n; r++) {  // r = row
            for (int c = 0; c <= n - word_len; c++) {  // c = column
                int mismatch = 0;
                for (int k = 0; k < word_len; k++) {  // k will "travel" trough the words and grid
                    if (tolower(n_grid[r - k][c + k]) != tolower(word_str[k])) mismatch ++;
                }
                if (mismatch < min_mistake) min_mistake = mismatch;
            }
        }

        total_mistakes += min_mistake;  // adding the minimun mistakes of each word
      }  // end of the algorithm loop


    printf("%d\n", total_mistakes);
    

    // free memmory
cleanup:
    for (int i = 0; i < n; i++) free(n_grid[i]);
    free(n_grid);

    for (int j = 0; j < m; j++) free(word_list[j].text);
    free(word_list);
    return 0;
}
