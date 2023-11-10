from db_manager import db_manager
import sys

sys.path.append("D:/Program/Programing/Projects/model_agency/source/server") ## C:/Users/DELL/Documents/GitHub/model_agency/server

import settings

db_manager.create_base(f"{settings.SCRIPTS_DIR}/data.sql")