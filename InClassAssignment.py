from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("mysql:///?User=root&Database=NorthWind&Server=127.0.0.1&Port=3306")

base = declarative_base()


class Orders(base):
    __tablename__ = "Orders"
    ShipName = Column(String, primary_key=True)
    Freight = Column(String)
    ShipCountry = Column(String)


engine = create_engine("mysql:///?User=root&Database=NorthWind&Server=myServer&Port=3306")

factory = sessionmaker(bind=engine)
session = factory()
for instance in session.query(Orders).filter_by(ShipCountry="USA"):
    print("ShipName: ", instance.ShipName)
    print("Freight: ", instance.Freight)
    print("---------")


Orders_table = Orders.metadata.tables["Orders"]
for instance in session.execute(Orders_table.select().where(Orders_table.c.ShipCountry == "USA")):
    print("ShipName: ", instance.ShipName)
    print("Freight: ", instance.Freight)
    print("---------")


new_rec = Orders(ShipName="placeholder", ShipCountry="USA")
session.add(new_rec)
session.commit()

updated_rec = session.query(Orders).filter_by(SOME_ID_COLUMN="SOME_ID_VALUE").first()
updated_rec.ShipCountry = "USA"
session.commit()

deleted_rec = session.query(Orders).filter_by(SOME_ID_COLUMN="SOME_ID_VALUE").first()
session.delete(deleted_rec)
session.commit()

