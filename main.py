animal = ""
while animal != "yes":
  animal_sound = input('''\n\nwhich animal sound you want to hear?\n
  1. cow
  2. lion
  3. duck
  4. dog
  5. cat
  6. sheep
  7. horse
  8. pig
  9. chicken
  10. goat
  11. donkey
  12. tiger
  13. elephant
  14. mouse
  15. fox
  16. wolf
  17. bear
  18. deer
  19. frog
  20. snake
  21. bird
  22. monkey
  23. hamster
  24. rabbit
  25. turtle
  26. fish
  27. shark
  28. whale
  29. dolphin
  30. octopus

  type any name from this list 
  ---> ''')
  if animal_sound == "cow":
    print("\033[32m", "\n\nthe sound of cow is 🐄moo", "\033[0m")

  elif animal_sound == "lion":
    print("\033[32m", "\n\nthe sound of lion is 🦁roar", "\033[0m")

  elif animal_sound == "duck":
    print("\033[32m", "\n\nthe sound of duck is 🦆quack", "\033[0m")

  elif animal_sound == "dog":
    print("\033[32m", "\n\nthe sound of dog is 🐶bark", "\033[0m")

  elif animal_sound == "cat":
    print("\033[32m", "\n\nthe sound of cat is 😺meow", "\033[0m")

  elif animal_sound == "sheep":
    print("\033[32m", "\n\nthe sound of sheep is 🐏baa", "\033[0m")

  elif animal_sound == "horse":
    print("\033[32m", "\n\nthe sound of horse is 🐎neigh", "\033[0m")

  elif animal_sound == "pig":
    print("\033[32m", "\n\nthe sound of pig is 🐷oink", "\033[0m")

  elif animal_sound == "chicken":
    print("\033[32m", "\n\nthe sound of chicken is 🐔cluck", "\033[0m")

  elif animal_sound == "goat":
    print("\033[32m", "\n\nthe sound of goat is 🐐baa", "\033[0m")

  elif animal_sound == "donkey":
    print("\033[32m", "\n\nthe sound of donkey is 🫏hee-haw", "\033[0m")

  elif animal_sound == "tiger":
    print("\033[32m", "\n\nthe sound of tiger is 🐯roar", "\033[0m")

  elif animal_sound == "elephant":
    print("\033[32m", "\n\nthe sound of elephant is 🐘trumpet", "\033[0m")

  elif animal_sound == "mouse":
    print("\033[32m", "\n\nthe sound of mouse is 🐭squeak", "\033[0m")

  elif animal_sound == "fox":
    print("\033[32m",
          "\n\nthe sound of fox is 🦊ring-ding-ding-ding-dingeringeding!",
          "\033[0m")

  elif animal_sound == "wolf":
    print("\033[32m", "\n\nthe sound of wolf is 🐺howl", "\033[0m")

  elif animal_sound == "bear":
    print("\033[32m", "\n\nthe sound of bear is 🐻roar", "\033[0m")

  elif animal_sound == "deer":
    print("\033[32m", "\n\nthe sound of deer is 🦊baa", "\033[0m")

  elif animal_sound == "frog":
    print("\033[32m", "\n\nthe sound of frog is 🐸ribbit", "\033[0m")

  elif animal_sound == "snake":
    print("\033[32m", "\n\nthe sound of snake is 🐍hiss", "\033[0m")

  elif animal_sound == "bird":
    print("\033[32m", "\n\nthe sound of bird is 🐦tweet", "\033[0m")

  elif animal_sound == "monkey":
    print("\033[32m", "\n\nthe sound of monkey is 🙈ooh-ooh-ooh", "\033[0m")

  elif animal_sound == "hamster":
    print("\033[32m", "\n\nthe sound of hamster is 🐹squeak", "\033[0m")

  elif animal_sound == "rabbit":
    print("\033[32m", "\n\nthe sound of rabbit is 🐰squeak", "\033[0m")

  elif animal_sound == "turtle":
    print("\033[32m", "\n\nthe sound of turtle is 🐢hiss", "\033[0m")

  elif animal_sound == "fish":
    print("\033[32m", "\n\nthe sound of fish is 🐟blub", "\033[0m")

  elif animal_sound == "shark":
    print("\033[32m", "\n\nthe sound of shark is 🦈gurgle", "\033[0m")

  elif animal_sound == "whale":
    print("\033[32m", "\n\nthe sound of whale is 🐳oooh", "\033[0m")

  elif animal_sound == "dolphin":
    print("\033[32m", "\n\nthe sound of dolphin is 🐬click-click", "\033[0m")

  elif animal_sound == "octopus":
    print("\033[32m", "\n\nthe sound of octopus is 🐙click-click", "\033[0m")

  else:
    print(
        "\033[31m",
        "WRONG INPUT please enter the name of the animal which is there on the above list",
        "\033[0m")

  animal = input("\ndo you want to exit? (yes or no) ---> ")

else:
  print("\n----------THANKS FOR PLAYING---------------")
