echo "Enter the file name"
read file_name

starter_code="class Solution:
    def solve(self, k, target):
        return 0


sample = Solution()
print(sample.solve())
"

echo $starter_code > $file_name.py