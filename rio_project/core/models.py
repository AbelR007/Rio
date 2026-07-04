from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    tasks = relationship("Task", back_populates="project")

    def __repr__(self):
        return f"<Project(name='{self.name}')>"

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    project_id = Column(Integer, ForeignKey('projects.id'))

    project = relationship("Project", back_populates="tasks")

    def __repr__(self):
        return f"<Task(title='{self.title}')>"
