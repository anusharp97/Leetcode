'''
79. Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 
Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
'''
def exist(self, board: List[List[str]], word: str) -> bool:
  if not word or not board:
      return False
  q = deque()
  row = len(board)
  col = len(board[0])
  visited = set()
  start = []
  for i in range(row):
      for j in range(col):
          if board[i][j] == word[0]:
              start.append([i,j])
  if not start:
      return False
  for s in start:
      localVisited = set()
      r = s[0]
      c = s[1]
      if board[r][c] == word:
          return True
      localVisited.add((r,c))
      q.append((r,c,board[r][c],localVisited))
      while q:
          size = len(q)
          for _ in range(size):
              curRow, curCol, curString, seen = q.popleft()
              for new in [(0,-1),(-1,0),(1,0),(0,1)]:
                  newRow, newCol = curRow+new[0], curCol+new[1]
                  if newRow>=row or newRow<0 or newCol>=col or newCol<0:
                      continue
                  if (newRow,newCol) not in seen and board[newRow][newCol]== word[len(curString)]:
                      if curString+board[newRow][newCol] == word:
                          return True
                      localVisited = seen.union(set({(newRow,newCol)}))
                      q.append((newRow,newCol,curString+board[newRow][newCol], localVisited))
  return False
