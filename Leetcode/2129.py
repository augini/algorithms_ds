class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.lower()
        words = title.split(" ")
        length = len(words)

        for i in range(length):
            curr = words[i]

            if len(curr) >= 3:
                characters = list(curr)
                characters[0] = characters[0].upper()
                words[i] = "".join(characters)

        return " ".join(words)
