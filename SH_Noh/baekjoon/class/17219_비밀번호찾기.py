from sys import stdin, stdout

sites, toFind = map(int, stdin.readline().split())
siteDict = dict(stdin.readline().rstrip().split() for _ in range(sites))
# '''
# siteDict = {}
# for _ in range(sites):
#     site, passwd = stdin.readline().split()
#     siteDict[site] = passwd
# '''
for _ in range(toFind):
    stdout.write(siteDict[(stdin.readline().rstrip())] + '\n')