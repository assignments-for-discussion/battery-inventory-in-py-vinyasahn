
def count_batteries_by_usage(cycles):
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  for i in counts:
    if i<310:
      lowcount+=1
    elif i>=310 and i<=929:
      mediumCount=mediumCount+1
    else:
      highCount=highCount+1
     print("Done Counting")
      



if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
