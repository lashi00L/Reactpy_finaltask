from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component,event,html,use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import mongo_client

