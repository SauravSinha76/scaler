def check(A):

    if not A:
        return 0

    if not A.left and not A.right:
        return A.val

    left = check(A.left)
    right = check( A.right)

    if A.val != (left + right):
        A[0] =0
    return A.val + left + right

    def solve(self, A):
        ans = [1]

        def sum_binary_tree(root):
            if not root:
                return 0

            # if it is leaf node
            if not root.left and not root.right:
                return root.val

            left = sum_binary_tree(root.left)
            right = sum_binary_tree(root.right)

            if left + right != root.val:
                ans[0] = 0

            return left + right + root.val

        sum_binary_tree(A)
        return ans[0]