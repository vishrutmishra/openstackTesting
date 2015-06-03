import re

def compare(regex, test):
	
  if type(regex) is not type(test):
    return False

  if type(test) is dict:
    for i in test:
      if type(test[i]) in [list, dict]:
				if not compare(regex[i], test[i]):
					return False
      else:
        if isinstance(test[i],(int, long, float, complex, bool)):
          if test[i] not in regex[i]:
            return False
        elif not re.match(regex[i], test[i]):
          return False

  else:
    sample_regex = regex[0]
    for sample_test in test:
      if not compare(sample_regex, sample_test):
        return False

  return True