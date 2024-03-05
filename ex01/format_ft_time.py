from datetime import date as d
import time

# Month dictionary

month_dict = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}

# First output line (the subject output is in ms, not in s.
# So I'm right it's wrong)

epocht = time.time()
epochn = format(int(epocht), '.2e')
print('Seconds since January 1, 1970: ' + str(epocht) +
      ' or ' + epochn + ' in scientific notation')

# Second output line

today = str(d.today()).split('-')
print(month_dict[today[1]] + ' ' + today[2] + ' ' + today[0])
