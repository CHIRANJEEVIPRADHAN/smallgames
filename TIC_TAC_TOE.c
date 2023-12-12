#include <stdio.h>


void printBoard(char board[3][3]) {
    printf("-------------\n");
    for (int i = 0; i < 3; i++) {
        printf("| %c | %c | %c |\n", board[i][0], board[i][1], board[i][2]);
        printf("-------------\n");
    }
}


int checkWin(char board[3][3], char player) {
    
    for (int i = 0; i < 3; i++) {
        if ((board[i][0] == player && board[i][1] == player && board[i][2] == player) ||
            (board[0][i] == player && board[1][i] == player && board[2][i] == player)) {
            return 1;
        }
    }

    
    if ((board[0][0] == player && board[1][1] == player && board[2][2] == player) ||
        (board[0][2] == player && board[1][1] == player && board[2][0] == player)) {
        return 1;
    }

    return 0;
}


int isBoardFull(char board[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == ' ') {
                return 0;
            }
        }
    }
    return 1;
}

int main() {
    char board[3][3] = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};
    int row, col;
    char currentPlayer = 'X';

    printf("Welcome to Tic-Tac-Toe!\n");

    do {
        printBoard(board);

        
        printf("Player %c, enter your move (row and column): ", currentPlayer);
        scanf("%d %d", &row, &col);

        
        if (row < 0 || row >= 3 || col < 0 || col >= 3 || board[row][col] != ' ') {
            printf("Invalid move. Try again.\n");
            continue;
        }

        
        board[row][col] = currentPlayer;

        
        if (checkWin(board, currentPlayer)) {
            printBoard(board);
            printf("Player %c wins! Congratulations!\n", currentPlayer);
            break;
        }

        
        if (isBoardFull(board)) {
            printBoard(board);
            printf("It's a tie! The game is over.\n");
            break;
        }

        
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';

    } while (1); 

    return 0;
}