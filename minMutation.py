'''
433. Minimum Genetic Mutation

A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.
For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.
Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". 
If there is no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be valid.
You may assume start and end string is not the same.
 

Example 1:
start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]
return: 1

Example 2:
start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
return: 2

Example 3:
start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
return: 3

'''
def minMutation(self, start: str, end: str, bank: List[str]) -> int:
  if end not in bank or not start or not end or not bank:
      return -1
  q = deque()
  visited = set([start])
  q.append((start,0))
  # breadth first search
  while q:
      size = len(q)
      for _ in range(size):
          gene, count = q.popleft()
          for i in range(len(gene)):
            # check for all possible combinations of mutation by replacing each letter
              for j in ["A","C","G","T"]:
                  mutation = gene[:i]+j+gene[i+1:]
                  if mutation == end:
                      return count + 1
                  if mutation not in visited and mutation in bank:
                      q.append((mutation,count+1))
                      visited.add(mutation)
  return -1
