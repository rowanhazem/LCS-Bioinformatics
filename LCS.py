from appJar import gui


def lcs(x, y, m, n):

    l = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                l[i][j] = 0

            elif x[i - 1] == y[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
                arr[i][j] = "diagonal"
            else:
                l[i][j] = max(l[i - 1][j], l[i][j - 1])
                if i > 0 and j > 0:
                    if l[i-1][j] > l[i][j-1]:
                        arr[i][j] = "up"
                    elif l[i-1][j] == l[i][j-1]:
                        arr[i][j] = "left up"
                    else:
                        arr[i][j] = "left"

            table = l[i][j]

    index = l[m][n]
    lcs = [""] * (index + 1)
    lcs[index] = ""
    i = m
    j = n
    while i > 0 and j > 0:

        if x[i - 1] == y[j - 1]:
            lcs[index - 1] = x[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif l[i - 1][j] > l[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print("LCS of " + x + " and " + y + " is " + "".join(lcs))
    subsequence = "LCS of " + x + " and " + y + " is " + "".join(lcs)

    return l, subsequence


def stringg():

    new_table = [[''] * (n + 2) for i in range(m + 2)]
    for i in range(m + 2):
        for j in range(n + 2):
            if i == 0:
                if j > 1:
                    new_table[i][j] = y[j-2]
            elif j == 0:
                if i > 1:
                    new_table[i][j] = x[i-2]
            else:
                new_table[i][j] = str(table[i-1][j-1])
                if arr[i-1][j-1] == "diagonal":
                    new_table[i][j] = "\u2196" + new_table[i][j]
                elif arr[i-1][j-1] == "up":
                    new_table[i][j] = "\u2191" + new_table[i][j]
                elif arr[i-1][j-1] == "left up":
                    new_table[i][j] = "\u2190" + "\u2191" + new_table[i][j]
                elif arr[i-1][j-1] == "left":
                    new_table[i][j] = "\u2190" + new_table[i][j]
                else:
                    new_table[i][j] = "" + new_table[i][j]
    return new_table


def trace_back(i, j, new_table):

    while i > 0 and j > 0:

        if arr[i][j] == "diagonal":
            new_table[i+1][j+1] = "\u25C6" + new_table[i+1][j+1]
            i = i-1
            j = j-1

        elif arr[i][j] == "left":
            new_table[i + 1][j + 1] = "\u25C6" + new_table[i + 1][j + 1]
            j = j-1

        elif arr[i][j] == "up":
            new_table[i + 1][j + 1] = "\u25C6" + new_table[i + 1][j + 1]
            i = i-1

        elif arr[i][j] == "left up":
            new_table[i + 1][j + 1] = "\u25C6" + new_table[i + 1][j + 1]
            j = j - 1


print("Please enter the first sequence:")
x = input()
print("Please enter the second sequence")
y = input()

m = len(x)
n = len(y)

arr = [[""] * (n + 1) for i in range(m + 1)]
table, sequence = lcs(x, y, m, n)
new_table = stringg()
trace_back(m, n, new_table)

app = gui()
app.addLabel("title", "Longest Common Subsequence")
app.setLabelBg("title", "white")
app.addLabel("subsequence", sequence)
app.setLabelBg("subsequence", "white")
app.addTable("lcs", new_table)


app.go()


