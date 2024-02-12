import math
text = input("Введите текст: ")
A = len(set(text.lower()))
print("Мощность алфавита = ", A)
infHartly = math.log(A,2)
print("Расчет информационной энтропии по Хартли: ", infHartly)
infShennonAVG = 0.0; ver = 0.0
for val in set(text.lower()):
    ver = text.count(val) / len(text)
    infShennonAVG = infShennonAVG - (ver * math.log(ver,2))
print("Расчет информационной энтропии по Шеннону по формуле: ", infHartly)
D = ((infHartly - infShennonAVG) / infHartly) * 100
print("Расчет избыточности алфавита: ", D)