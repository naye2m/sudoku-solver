#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define GREEN ""
#define YELLOW ""
#define RED ""
#define RESET ""
#define N 9
unsigned char typedef sC;
sC **problemB;
sC **solvedB;
int count;
sC **createSCArray(int m, int n);
void destroySCArray(sC **arr);
bool isSafe(int r, int c, int n);
bool findUnassigned(int *r, int *c);
bool solveSudoku();
int ati(char a);
int main(int argc, char **argv)
{
    char *codeName = argv[0];
    if (argc != 2)
    {
        printf("Usage:%s <81chars_sudoku_string_withoutspace> OR [row1, row2 .... row9]\n", codeName);
        return 1;
    }
    if (strlen(argv[1]) != 81)
    {
        printf("Usage:%s <81chars_sudoku_string_withoutspace> OR [row1, row2 .... row9]\n", codeName);
        return 2;
    }
    solvedB = createSCArray(N, N);
    problemB = createSCArray(N, N);
    if (argc == 2)
    {
        for (int k = 0; k < 81; k++)
        {
            int i = k / 9;
            int j = k % 9;
            problemB[i][j] = ati(argv[1][k]);
            solvedB[i][j] = problemB[i][j];
        }
    }
    for (int k = 0; k < 81; k++)
    {
        int i = k / 9;
        int j = k % 9;
        solvedB[i][j] = problemB[i][j];
    }
    count = 0;
    if (!solveSudoku())
    {
        printf("Failed: Failed to solve sudoku\n");
        free(solvedB);
        free(problemB);
        return 0;
    }
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            printf("%i" RESET, solvedB[i][j]);
        }
        // printf("\n");
    }
    printf("\n%i", count);
    free(solvedB);
    free(problemB);
    return 0;
}
sC **createSCArray(int m, int n)
{
    sC *values = calloc(m * n, sizeof(sC));
    sC **rows = malloc(m * sizeof(sC *));
    for (int i = 0; i < m; ++i)
    {
        rows[i] = values + i * n;
    }
    return rows;
}
void destroySCArray(sC **arr)
{
    free(*arr);
    free(arr);
}
bool isSafe(int r, int c, int n)
{
    for (int i = 0; i < N; i++)
        if (solvedB[r][i] == n || solvedB[i][c] == n || solvedB[r - r % 3 + i / 3][c - c % 3 + i % 3] == n)
            return false;
    return true;
}
bool findUnassigned(int *r, int *c)
{
    for (*r = 0; *r < N; (*r)++)
    {
        for (*c = 0; *c < N; (*c)++)
        {
            count++;
            if (solvedB[*r][*c] == 0)
                return true;
        }
    }
    return false;
}
bool solveSudoku()
{
    int row, col;
    if (!findUnassigned(&row, &col))
        return true;
    for (int i = 0; i < 9; i++)
    {
        int num = i + 1;
        if (isSafe(row, col, num))
        {
            solvedB[row][col] = num;
            if (solveSudoku())
                return true;
            solvedB[row][col] = 0;
        }
    }
    return false;
}
int ati(char a)
{
    a -= '0';
    if (a >= 0 && a <= 9)
        return a;
    else
        return -1;
}
