def find_max_num_balanced_substrings(l, r):
  max_num_substrings = 0
  # TODO: Add logic to find the maximum possible number of balanced non-empty
  # substrings
  return max_num_substrings


def main():
  # Get number of test cases
  test_cases = int(raw_input())
  for test_case in range(1, test_cases + 1):
    # Get total of left and right parentheses
    l, r = map(int, raw_input().split())
    ans = find_max_num_balanced_substrings(l, r)
    print("Case #%d: %d" % (test_case, ans))


if __name__ == "__main__":
  main()
