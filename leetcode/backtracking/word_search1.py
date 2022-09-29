# Python solution for word search


def word_search(board,word):

    width = len(board[0])
    height = len(board)
    l = len(word)
    def dfs(i,j,k):

        if k == l:
            return True

        elif 0 <= i < height and 0 <= j < width and board[i][j] == word[k]:

            temp = board[i][j]

            board[i][j] = '#'

            if dfs(i+1,j,k+1) or dfs(i-i,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1):
                return True

            board[i][j] = temp


    for i in range(rows):
        for j in range(cols):
            if dfs(i,j,0):
                return True
    
    return False