with open('/Users/szymon/Downloads/abbrev.txt') as f:
    lines = f.read().splitlines()

lines.sort()
final_string = "\n".join(lines)
# lines.replace("\\t\\t", "		")
# print (lines)
print (final_string)

with open("output.txt", "w") as text_file:
    text_file.write(final_string)