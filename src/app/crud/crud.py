from ..db.db import mydb

async def get_single_test():
    sql = "SELECT * FROM WORD_800 where words='a'"
    cursor = mydb.cursor()
    res = make_array_words(cursor=cursor, sql=sql)
    cursor.close()
    return res

async def get_nouns(sampling: int):
    sql = f"SELECT words FROM WORD_800 where noun=true order by rand() limit {sampling}"
    res = make_array_words(mydb=mydb, sql=sql)
    return res

async def get_pronouns(sampling: int):
    sql = f"SELECT words FROM WORD_800 where pronoun=true order by rand() limit {sampling}"
    res = make_array_words(mydb=mydb, sql=sql)
    return res

async def get_verbs(sampling: int):
    sql = f"SELECT words FROM WORD_800 where verb=true order by rand() limit {sampling}"
    res = make_array_words(mydb=mydb, sql=sql)
    return res

async def get_adjectives(sampling: int):
    sql = f"SELECT words FROM WORD_800 where adjective=true order by rand() limit {sampling}"
    res = make_array_words(mydb=mydb, sql=sql)
    return res

async def get_adverbs(sampling: int):
    sql = f"SELECT words FROM WORD_800 where adverb=true order by rand() limit {sampling}"
    res = make_array_words(mydb=mydb, sql=sql)
    return res

async def get_prepositions(sampling: int):
    sql = f"SELECT words FROM WORD_800 where preposition=true order by rand() limit {sampling}"
    res = make_array_words(mydb=mydb, sql=sql)
    return res

async def get_conjunctions(sampling: int):
    sql = f"SELECT words FROM WORD_800 where conjunction=true order by rand() limit {sampling}"
    res = make_array_words(mydb=mydb, sql=sql)
    return res

async def get_interjections(sampling: int):
    sql = f"SELECT words FROM WORD_800 where interjection=true order by rand() limit {sampling}"
    res = make_array_words(mydb=mydb, sql=sql)
    return res

def make_array_words(mydb: mydb, sql: str):
    cursor = mydb.cursor()
    cursor.execute(sql)
    res_arr = []
    res = cursor.fetchall()
    for row in res:
        res_arr.append("".join(row))
    cursor.close()
    return res_arr

