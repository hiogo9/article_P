

# class Article():
#     def __init__(self, line):
#         self.articleId = line.split("|")[0]
#         self.authorPOS = line.split("|")[1]
#         self.articleAuthor = line.split("|")[2]
#         self.jname = line.split("|")[3]
#         self.doi = line.split("|")[4]
#         self.anumber = line.split("|")[5]
#         self.year = line.split("|")[6]


articleToAuthor = dict()
articleToAuthoFull = dict()
with open('_SELECT_s_KEY_ID_aa_POS_aa_KEY_ID_aa_NAME_LONG_s_JTITLE_s_DOI_s__202309281923.csv', "r") as f:
    for line in f:
        articleId = line.split("|")[0]
        authorPOS = line.split("|")[1]
        articleAuthorID = line.split("|")[2]
        articleAuthor = line.split("|")[3]
        jname = line.split("|")[4]
        doi = line.split("|")[5]
        anumber = line.split("|")[6]
        year = line.split("|")[7].strip()
        fullInfo = str(articleAuthorID)+'#'+str(articleAuthor)+'#' + \
                                               str(jname)+'#' + \
                                               str(doi)+'#' + str(year)+'#'+ \
                                               str(authorPOS)
        if articleId in articleToAuthor:
            articleToAuthor[articleId].append(articleAuthorID)
            articleToAuthoFull[articleId].append(fullInfo)
        else:
            articleToAuthor[articleId] = [articleAuthorID]
            articleToAuthoFull[articleId] = [fullInfo]
            
            


with open('export_wos_biophysics.csv','w') as data:
        for key in  articleToAuthor:
            if key == '"KEY_ID"':
                continue
            for articleAuthorID in articleToAuthor[key]:
                data.write(str(articleAuthorID)+'|')
            data.write('\n')
            
            
with open('export_wos_biophysics_FULL.csv','w') as data:
        for key in  articleToAuthoFull:
            if key == '"KEY_ID"':
                continue
            data.write(str(key)+'|')
            for articleAuthorID in articleToAuthoFull[key]:
                data.write(str(articleAuthorID)+'|')
            data.write('\n')