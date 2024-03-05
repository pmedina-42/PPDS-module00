import datetime as d


epocht = d.datetime.now().timestamp()
print(f'Seconds since January 1, 1970: {epocht:,.4f} \
or {epocht:.2e} in scientific notation')
print(f'{d.date.today().strftime("%b %d %Y")}')
