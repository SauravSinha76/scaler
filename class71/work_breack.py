# public class Solution {
#     boolean solve(String A,Set<String> set){
#         if(A.length() == 0){
#             return true;
#         }
#
#         for(int i = 0;i < Math.min(20,A.length());i++){
#             String str = A.substring(0,i + 1);
#             if(set.contains(str) && solve(A.substring(i + 1),set)){
#                 return true;
#             }
#         }
#
#         return false;
#     }
#     public int wordBreak(String A, ArrayList<String> B) {
#         return solve(A,new HashSet<>(B)) ? 1 : 0;
#     }
# }




def solve(A,B):
    dp = [0] * (len(A) + 1)
    dp[len(A)] = 1
    for i in range(len(A) - 1, -1, -1):
        for w in B:
            if (i + len(w)) <= len(A) and A[i: i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break
    return dp[0]

def wordBerack(A,B):
    return solve(A,B)

A = "myinterviewtrainer"
B = ["trainer", "my", "interview"]
# A = "a"
# B = ["aaa"]
print(solve(A,B))
x = "saurav"
print(x[:1])