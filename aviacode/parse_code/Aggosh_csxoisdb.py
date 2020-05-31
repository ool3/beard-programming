def main(a, b, c):
  a.update(b)
  a.update(c)
  return(a)

def tests():
    assert (main({1:10, 2:20}, {3:30, 4:40}, {5:50, 6:60}) == {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}), "Oh no! This assertion failed!"