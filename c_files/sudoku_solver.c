#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define GREEN "<span class=\"ss_green\">"
#define YELLOW "<span class=\"ss_yellow\">"
#define RED "<span class=\"ss_red\">"
#define RESET "</span>"
#define N 9
unsigned char typedef sC;
sC **problemB;
sC **solvedB;
int count;
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
            if (solvedB[*r][*c] == 0)
                return true;
        }
    }
    return false;
}
bool solveSudoku()
{
    count++;
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
void getBoard()
{
    char str[10];
    for (int i = 0; i < N; i++)
    {
        printf("insert row %i of %i <%i Digit without space>\n", i + 1, N, N);
        *(str + 1) = '\0';
        while (strlen(str) != N || str[8] == '\n')
        {
            printf("Enter row %i of %i: ", i + 1, N);
            fgets(str, sizeof(str), stdin);
        }
        for (int j = 0; j < N; j++)
        {
            problemB[i][j] = ati(str[j]);
        }
    }
    printf("\n");
}
int main(int argc, char **argv)
{
    char *codeName = argv[0];
    if (argc != 2)
    {
        printf("Usage:%s <81chars_sudoku_string_withoutspace> OR [row1, row2 .... row9]\n", codeName);
        return 1;
    }
    solvedB = createSCArray(N, N);
    problemB = createSCArray(N, N);
    if (argc == 2)
    {
        if (strlen(argv[1]) != 81)
        {
            printf("Usage:%s <81chars_sudoku_string_withoutspace> OR [row1, row2 .... row9]\n", codeName);
            printf("input mennually :\n");
            getBoard();
        }
        else
            for (int k = 0; k < 81; k++)
            {
                int i = k / 9;
                int j = k % 9;
                problemB[i][j] = ati(argv[1][k]);
                solvedB[i][j] = problemB[i][j];
            }
    }
    else if (argc == 10)
    {
        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                problemB[i][j] = ati(argv[i + 1][j]);
                solvedB[i][j] = problemB[i][j];
            }
        }
    }
    else
    {
        getBoard();
    }
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            if (problemB[i][j] == 0)
                printf(RED);
            else
                printf(GREEN);
            printf("%i " RESET, problemB[i][j]);
        }
        printf("\n");
    }
    for (int k = 0; k < 81; k++)
    {
        int i = k / 9;
        int j = k % 9;
        solvedB[i][j] = problemB[i][j];
    }
    count = 0;
    if (solveSudoku())
        printf("Done: solved sudoku\n");
    else
        printf("Failed: Failed to solve sudoku\n");
    printf("complexity : %i\n", count);
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            if (problemB[i][j] == 0)
                printf(YELLOW);
            else
                printf(GREEN);
            printf("%i " RESET, solvedB[i][j]);
        }
        printf("\n");
    }
    free(solvedB);
    free(problemB);
    return 0;
}
