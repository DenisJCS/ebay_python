def student(start_ls, unit, grade, school = 'Harvard', city = 'Boston'):
  return (f"Start_LS:{start_ls}, Unit:{unit}, Grade:{grade}, School:{school}, City:{city}

start_ls = input("What time your classes start ?: ")
unit = input(" What unit are you belong ?:")
grade = input("What year are you in school ?")
result = student(start_ls, unit, grade)
print(result)
