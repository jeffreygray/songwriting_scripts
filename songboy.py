####################################################
## songboy.py: generate 4-chord groupings within a key, modular for expansion
##  for Nick to start learning python3
##
##  usage suggestion: python3 songboy.py 6
####################################################


# sometimes you have to import items so you can do perform functionality that isn't built-in
import sys, random

# only hit this condition if you give an argument at runtime
if len(sys.argv) == 2:
  print("####################################################")
  print(f"## songboy.py: generating {sys.argv[1]} clusters!")
  print("####################################################")

  # "hard coded" values for the scale we're working with. Add others here as you learn them
  f_major_simple = ["F", "Gm", "Am", "Bb", "C7", "Dm", "Em"]
  f_major_complex = ["Fmaj7", "Gm7", "Am7", "Bbmaj7","C7","Dm7","Em7b5"]
  my_other_scale = ["put","7","here","like","above"]

  # output n 4-chord sequences in this scale
  for i in range(1, (int(sys.argv[1])+1)):
    # learn the functionality of fstrings below, google them
    #print(f"{random.randint(1,7)}")
    print(f"option {i}: {f_major_simple[random.randint(0,6)]}, {f_major_simple[random.randint(0,6)]}, {f_major_simple[random.randint(0,6)]}, {f_major_simple[random.randint(0,6)]}")

else:
  print("bad argument #, example usage: python3 songboy.py 5")
