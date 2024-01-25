from typing_extensions import Annotated
from .. import config
from ..crud import crud

from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/words",
    tags=["words"]
)

settings = config.Settings()

@router.get("/test")
async def get_test(random: Annotated[int, Query()]):
    
    sql_res = await crud.get_single_test()
    print(sql_res)
    res = {"Hello": random}
    return res

@router.get("/nouns")
async def get_nouns(samplings: Annotated[int, Query()],
                    description="명사(noun) 목록을 랜덤으로 알려줍니다.",
                    summary="""samplings 수 만큼의 명사(noun)를 랜덤으로 응답합니다."""):
    sql_res = await crud.get_nouns(sampling=samplings)
    print(sql_res)
    res = {"명사(nouns)": sql_res}
    return res

@router.get("/pronouns")
async def get_pronouns(samplings: Annotated[int, Query()],
                        description="대명사(pronoun) 목록을 랜덤으로 알려줍니다.",
                        summary="""samplings 수 만큼의 대명사(pronoun)를 랜덤으로 응답합니다."""):
    sql_res = await crud.get_pronouns(sampling=samplings)
    print(sql_res)
    res = {"대명사(pronouns)": sql_res}
    return res

@router.get("/verbs")
async def get_verbs(samplings: Annotated[int, Query()],
                    description="동사(verb) 목록을 랜덤으로 알려줍니다.",
                    summary="""samplings 수 만큼의 동사(verb)를 랜덤으로 응답합니다."""):
    sql_res = await crud.get_verbs(sampling=samplings)
    print(sql_res)
    res = {"동사(verbs)": sql_res}
    return res

@router.get("/adjectives")
async def get_adjectives(samplings: Annotated[int, Query()],
                        description="형용사(adjective) 목록을 랜덤으로 알려줍니다.",
                        summary="""samplings 수 만큼의 형용사(adjective)를 랜덤으로 응답합니다."""):
    sql_res = await crud.get_adjectives(sampling=samplings)
    print(sql_res)
    res = {"형용사(adjectives)": sql_res}
    return res

@router.get("/adverbs")
async def get_adverbs(samplings: Annotated[int, Query()],
                        description="부사(adverb) 목록을 랜덤으로 알려줍니다.",
                        summary="""samplings 수 만큼의 부사(adverb)를 랜덤으로 응답합니다."""): 
    sql_res = await crud.get_adverbs(sampling=samplings)
    print(sql_res)
    res = {"부사(adverbs)": sql_res}
    return res

@router.get("/prepositions")
async def get_prepositions(samplings: Annotated[int, Query()],
                            description="전치사(preposition) 목록을 랜덤으로 알려줍니다.",
                            summary="""samplings 수 만큼의 전치사(preposition)를 랜덤으로 응답합니다."""): 
    sql_res = await crud.get_prepositions(sampling=samplings)
    print(sql_res)
    res = {"전치사(prepositions)": sql_res}
    return res

@router.get("/conjunctions")
async def get_conjunctions(samplings: Annotated[int, Query()],
                            description="접속사(conjunction) 목록을 랜덤으로 알려줍니다.",
                            summary="""samplings 수 만큼의 접속사(conjunction)를 랜덤으로 응답합니다."""): 
    sql_res = await crud.get_conjunctions(sampling=samplings)
    print(sql_res)
    res = {"접속사(conjunctions)": sql_res}
    return res

@router.get("/interjections")
async def get_interjections(samplings: Annotated[int, Query()],
                            description="감탄사(interjection) 목록을 랜덤으로 알려줍니다.",
                            summary="""samplings 수 만큼의 감탄사(interjection)를 랜덤으로 응답합니다."""): 
    sql_res = await crud.get_interjections(sampling=samplings)
    print(sql_res)
    res = {"감탄사(interjections)": sql_res}
    return res