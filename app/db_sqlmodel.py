from sqlmodel import SQLModel,create_engine,Session

DATABASE_URL = ("postgresql://myproject:log@127.0.0.1:5432/postgres")
engine = create_engine(DATABASE_URL,echo=True)
def get_session():
    with Session(engine) as Section:
       yield Session