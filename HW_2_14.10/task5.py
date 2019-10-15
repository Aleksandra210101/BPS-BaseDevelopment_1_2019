"""
Creator: Aleksandra Krylova
"""
from flask import Flask

APP = Flask(__name__)

@APP.route('/')

def businesscard():
    """HTML"""
    return """
        <div style="display: flex; align-items: center; margin-left: 50px; margin-top: 25px; padding: 25px 25px; 
                    height: 250px; width:550px; background-color: rgb(255, 238, 221); border-radius: 5px;">
            <div style="margin-right: 30px;"><img src="https://avatars.mds.yandex.net/get-pdb/69339/10b16dfb-55d7-400c-bd09-569396fb4f25/s1200?webp=false" 
                style=" border-radius: 5px; width: 250px;height: 250px;"></div>
            <div style="width: 4px; height: 240px;background-color: rgb(43, 30, 19) ;"><div>
            <div style="margin-left: 30px; margin-top:-10px;width: 250px;">
                <h2 style="text-align: center; font-size: 26px; color: rgb(43, 30, 19);"><span style="font-size: 28px;">ДАРТВЕЙДОВ</span> Чубакка Чубасович<br><p style="margin-top:5px; font-size:18px; 
                font-weight: normal; line-height: 20px;">генеральный директор <br> ОАО "Pug Donat`s"<span></h2>
                <p style="margin-top:25px; text-align: center; font-size:20px;">Ешь пончики<br>и да пребудет с тобой сила!</p>
                <p style="margin-top: 30px; text-align: right;">тел.:<span style="font-style:italic"> +7 (916) 522-91-00</span></p>
            </div>
        </div>
        """
APP.run(port=8080, debug=True)
    