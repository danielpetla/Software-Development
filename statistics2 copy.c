#include <stdio.h>
#include <stdlib.h>

// Define a structure to hold the dynamic array and its size
typedef struct {
    int *array;
    int size;
} DynamicArray;

// Function to read integers until the user enters 0, 
// dynamically resizing the array
DynamicArray read_array() {
    int capacity = 5; // Initial capacity
    int size = 0;     // Current number of elements
    int input_value;

    // Initial memory allocation
    int *values = malloc(capacity * sizeof(int));
    if (values == NULL) {
        perror("Failed to allocate initial memory");
        exit(EXIT_FAILURE);
    }

    printf("Enter integers, one at a time. Enter 0 to stop.\n");

    while (1) {
        printf("Enter value %d: ", size + 1);
        // Use an intermediate variable for input
        if (scanf("%d", &input_value) != 1) {
            // Handle non-integer input
            printf("Invalid input. Terminating input.\n");
            // Clear the input buffer for safety
            while (getchar() != '\n'); 
            break; 
        }

        // Check for the sentinel value (0)
        if (input_value == 0) {
            break; 
        }

        // Check if we need to resize the array (current size equals capacity)
        if (size == capacity) {
            capacity *= 2; // Double the capacity
            int *temp = realloc(values, capacity * sizeof(int));
            if (temp == NULL) {
                perror("Failed to reallocate memory");
                free(values); // Free the original block
                exit(EXIT_FAILURE);
            }
            values = temp;
        }

        // Store the value and increment the size
        values[size] = input_value;
        size++;
    }

    // Shrink the array to the exact size needed (optional but good practice)
    if (size > 0) {
        int *temp = realloc(values, size * sizeof(int));
        if (temp != NULL) {
            values = temp;
        }
    } else {
        // If no elements were read (only 0 was entered), free the initial block
        free(values);
        values = NULL;
    }

    // Return the array and its actual size
    DynamicArray result = {values, size};
    return result;
}

double compute_average(int *array, int size) {
    if (size == 0 || array == NULL) {
        return 0.0; // Avoid division by zero
    }
    
    long long sum = 0; // Use long long for sum to prevent overflow with large arrays
    for (int i = 0; i < size; i++){
        sum += array[i];
    }
    
    // Perform division using double-precision types for accurate average
    double avg = (double)sum / size;

    return avg;
}

int main() {
    // Call read_array which returns both the array pointer and its size
    DynamicArray result = read_array(); 
    
    int *array = result.array;
    int size = result.size;

    if (size > 0) {
        double avg = compute_average(array, size);
        printf("\nTotal elements read: %d\n", size);
        printf("Average: %.2lf\n", avg);
    } else {
        printf("\nNo elements were entered (only 0).\n");
    }

    // TASK: Free array only if memory was allocated (array is not NULL)
    free(array);
    // array = NULL; // Optional in main, but good practice
    
    return 0;
}