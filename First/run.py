from my_app import app
from config import DevelopmentConfig


#print(app.default_config) #конфигурация по умолчанию
app.config.from_object("config.DevelopmentConfig")

#print("\n================ after loading ================\n")
#print(app.config) #словарь настроек для запуска 


if __name__ == "__main__":
    app.run(port=DevelopmentConfig.PORT)