articleToAuthor = dict()
newauthorId = dict()
newId = 0
with open("export2.csv", "r", encoding="utf-8") as f:
    for line in f:
        line_arr = line.split("|")
        doi = line_arr[0]
        authorId = line_arr[1]
        articleId = line_arr[2]
        aName = str(line_arr[3]).strip().lower()
        apos = line_arr[4]

        if aName not in newauthorId:
            newId = newId + 1
            newauthorId[aName] = newId

        if doi in articleToAuthor:
            array = articleToAuthor[doi]
            if aName not in array:
                articleToAuthor[doi].append(newauthorId[aName])

        else:
            articleToAuthor[doi] = [newauthorId[aName]]
        # print(line_arr)

newauthorIdrev = inv_dict = {v: k for k, v in newauthorId.items()}
articleToAuthormerged = {}
for key, value in articleToAuthor.items():
    mergeda = set(value)
    articleToAuthormerged[key] = mergeda
with open("export_neo4j_bioinformatic_family.csv", "w", encoding="utf-8") as f:
    for key, value in articleToAuthormerged.items():
        LINE = str(key) + "|"
        for authorId in articleToAuthormerged[key]:
            LINE = LINE + str(newauthorIdrev[authorId]) + "|"
        LINE = LINE + "\n"
        f.write(LINE)


with open("export_neo4j_bioinformatic_numbers.csv", "w", encoding="utf-8") as f:
    for key, value in articleToAuthormerged.items():
        LINE = str(key) + "|"
        for authorId in articleToAuthormerged[key]:
            LINE = LINE + str(authorId) + "|"
        LINE = LINE + "\n"
        f.write(LINE)
