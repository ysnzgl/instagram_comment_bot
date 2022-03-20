from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Hesaplar(Base):
    __tablename__ = 'hesaplar'

    id = Column(Integer, primary_key=True)
    isim = Column(String(250), nullable=False)

class Instagram(Base):
    __tablename__ = 'instagram'

    id = Column(Integer, primary_key=True)
    isim = Column(String(250), nullable=False)
    hesap_id = Column(Integer, ForeignKey('hesaplar.id'))


# sqlite olarak kayıtedilecek dosyayı gösteriyoruz
engine = create_engine('sqlite:///okul_sistemi.db')

# Tanımladığımız Base üzerindeki tabloları oluşturuyoruz
Base.metadata.create_all(engine)