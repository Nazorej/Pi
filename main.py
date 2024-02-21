# Это программа на Python

# Десять последних цифр числа Пи: 7817924264
# https://fhgr.ch/en/themenschwerpunkte/applied-future-technologies/davis-centre/pi-challenge

# pip install MIDIUtil

from midiutil import MIDIFile

# Первые 10 цифр числа Пи
#piDigits = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Последние 10 цифр числа Пи
piDigits = [7, 8, 1, 7, 9, 2, 4, 2, 6, 4]

# Создаем MIDI-файл с одним треком
midi = MIDIFile(1)

# Начинаем с первого такта
time = 0

# Добавляем ноты в MIDI-файл
for digit in piDigits:
    # Используем цифры числа Пи как высоту ноты (с некоторым смещением)
    note = 60 + digit
    # Добавляем ноту в трек 0, с заданной высотой, начиная с текущего времени, продолжительностью 1 такт, громкостью 100
    midi.addNote(0, 0, note, time, 1, 100)
    # Переходим к следующему такту
    time += 1

# Записываем MIDI-файл
with open("piMelody.mid", "wb") as outputFile:
    midi.writeFile(outputFile)
