# https://leetcode.com/problems/simplify-path/description/


class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")

        curr_path = []

        for path in paths:
            if path == "..":
                if curr_path:
                    curr_path.pop()
                else:
                    continue
            elif path != "" and path != "/" and path != " " and path != ".":
                curr_path.append(path)

        return "/" + "/".join(curr_path)
