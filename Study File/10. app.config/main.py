from flask import Flask

app = Flask(__name__)

app.config['CONFIG'] = 'hello?'
# app의 config를 통해 설정 값들을 저장할 수 있다

print(app.config['CONFIG']) # -> dict 형태의 app.config에서 CONFIG에 해당하는 값 출력
# [app.Flask}
#       self.config = self.make_config(...)
# 해당 객체는 config.Config 클래스의 인스턴스이며, 해당 클래스는 dict를 상속받고 있다.

app.config.update({ # -> config를 한번에 여러개 업데이트 한다
    'CONFIG_1': 1,
    'CONFIG_2': True
})
del app.config['CONFIG_2'] # -> config 중 CONFIG_2 값을 삭제한다
print('CONFIG_2' in app.config) # -> print(app.config['CONFIG_2']) 와 같다 -> 없으므로 False return

# --

print(app.config)
# 수많은 설정 값(DEBUG, TESTING 등)들이 이미 들어가 있다
# 이미 들어가 있는 해당 설정 값들의 일부는 프로퍼티 형태로 즉시 접근 가능하다
print(app.debug, app.testing, app.secret_key)

# app.config는 딕셔너리를 상속받고, config를 외부에서 load하기 위해 여러 메소드들이 있다
# [app.config]
#    def from_envvar(self, variabel_name, silent=False)
#    def from_pyfile(self, filename, silent= False)
#    def from_object(self, obj)

class SomeConfig(object): # ->  from_object를 이용해 config 값을 추가 할 수 있게 해주는 객체
    SOME_CONFIG = 1

app.config.from_object(SomeConfig)  # -> app.config.from_object(class 이름)을 통해 config 추가
print(app.config['SOME_CONFIG'])