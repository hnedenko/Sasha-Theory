import math
import random
import time
from datetime import datetime
import os


class Person:
    def __init__(self, names, appearance, interests, biography, activities, volition, location):
        # Загрузка всех настроек Саши: имён, внешности, интересов, биографии, времяпровождений и местоположения
        self.names = names
        self.appearance = appearance
        self.interests = interests
        self.biography = biography
        self.activities = activities
        self.volition = volition
        self.location = location

        # инициализация случайного состояния и времяпровождения, ы котором быть
        self.state = {
            "schizoid": random.random(),
            "neurotic": random.random(),
            "narcissistic": random.random()
        }

    def live(self, delay):

        while self.is_alive():

            # Вывод состояния
            print("Состояние:", self.state)

            # Готовность к переписке
            self.chat()

            # Обновление состояния из-за времени жизни
            self.update_state_by_circadian_rhythms()

            # Задержка времени
            time.sleep(delay)

    def chat(self):
        pass

    def get_current_state(self):
        return self.state

    def get_sun_cycle_state(self):
        # Получаем текущую дату и дату Нового Года
        today = datetime.now().date()
        date_NewYear = datetime(2025, 1, 1).date()

        # Задаём базовые настройки для функции
        amplitude = 0.5
        frequency = 1 / 365
        elapsed_time = today - date_NewYear
        shift = 0.5

        # Рассчитываем влияние на напряжение шизоида, невротика и нарцисса
        phase_shift = 105
        schizoid_sin_state = amplitude * math.cos(math.pi * frequency * (elapsed_time.days - phase_shift)) + shift
        phase_shift = 196
        neurotic_sin_state = amplitude * math.cos(math.pi * frequency * (elapsed_time.days - phase_shift)) + shift
        phase_shift = 288
        narcissistic_sin_state = amplitude * math.cos(math.pi * frequency * (elapsed_time.days - phase_shift)) + shift
        lunar_cycle_state = {
            "schizoid": schizoid_sin_state,
            "neurotic": neurotic_sin_state,
            "narcissistic": narcissistic_sin_state
        }

        return lunar_cycle_state

    def get_lunar_cycle_state(self):
        # Получаем текущую дату и дату полнолуния
        today = datetime.now().date()
        date_full_moon = datetime(2025, 11, 7).date()

        # Задаём базовые настройки для функции
        amplitude = 0.5
        frequency = 1 / 14
        elapsed_time = today - date_full_moon
        shift = 0.5

        # Рассчитываем влияние на напряжение шизоида, невротика и нарцисса
        phase_shift = 0
        schizoid_sin_state = amplitude * math.cos(math.pi * frequency * (elapsed_time.days - phase_shift)) + shift
        phase_shift = 14
        neurotic_sin_state = amplitude * math.cos(math.pi * frequency * (elapsed_time.days - phase_shift)) + shift
        phase_shift = 7
        narcissistic_sin_state = amplitude * math.cos(math.pi * frequency * (elapsed_time.days - phase_shift)) + shift
        lunar_cycle_state = {
            "schizoid": schizoid_sin_state,
            "neurotic": neurotic_sin_state,
            "narcissistic": narcissistic_sin_state
        }

        return lunar_cycle_state

    def det_Earth_cycle_state(self):
        # Получаем текущее время и время полуночи
        datetime_now = datetime.now()
        datetime_midnight = datetime(2025, 10, 30, 0,0,0)

        # Задаём базовые настройки для функции
        amplitude = 0.5
        frequency = 1 / (12*3600)
        elapsed_time = (datetime_now - datetime_midnight).total_seconds()
        shift = 0.5

        # Рассчитываем влияние на напряжение шизоида, невротика и нарцисса
        phase_shift = 10*3600
        schizoid_sin_state = amplitude * math.cos(math.pi * frequency * (elapsed_time - phase_shift)) + shift
        phase_shift = 14*3600
        neurotic_sin_state = amplitude * math.cos(math.pi * frequency * (elapsed_time - phase_shift)) + shift
        phase_shift = 18*3600
        narcissistic_sin_state = amplitude * math.cos(math.pi * frequency * (elapsed_time - phase_shift)) + shift
        Earth_cycle_state = {
            "schizoid": schizoid_sin_state,
            "neurotic": neurotic_sin_state,
            "narcissistic": narcissistic_sin_state
        }

        return Earth_cycle_state

    def det_hourly_cycle_state(self):
        # Получаем текущее время и время полуночи
        datetime_now = datetime.now()
        datetime_midnight = datetime(2025, 10, 30, 0,0,0)

        # Задаём базовые настройки для функции
        amplitude = 0.5
        frequency = 1 / (3600)
        elapsed_time = (datetime_now - datetime_midnight).total_seconds()
        shift = 0.5

        # Рассчитываем влияние на напряжение шизоида, невротика и нарцисса
        phase_shift = 0*3600
        schizoid_sin_state = amplitude * math.cos(math.pi * frequency * (elapsed_time - phase_shift)) + shift
        phase_shift = 0.5*3600
        neurotic_sin_state = amplitude * math.cos(math.pi * frequency * (elapsed_time - phase_shift)) + shift
        phase_shift = 1*3600
        narcissistic_sin_state = amplitude * math.cos(math.pi * frequency * (elapsed_time - phase_shift)) + shift
        hourly_cycle_state = {
            "schizoid": schizoid_sin_state,
            "neurotic": neurotic_sin_state,
            "narcissistic": narcissistic_sin_state
        }

        return hourly_cycle_state

    def update_state_by_circadian_rhythms(self):
        # Получение текущего состояния
        current_state = self.get_current_state()

        # Получение солнечного влияния (времени года)
        sun_cycle_state = self.get_sun_cycle_state()
        # Получение лунного влияния (фазы луны)
        lunar_cycle_state = self.get_lunar_cycle_state()
        # Получение Земного влияния (времени дня)
        Earth_cycle_state = self.det_Earth_cycle_state()
        # Получение часового влияния
        hourly_cycle_state = self.det_hourly_cycle_state()

        # Расчёт итогового состояния
        weights_sum = (1 +
                       self.volition["sun_cycle"] +
                       self.volition["lunar_cycle"] +
                       self.volition["Earth_cycle"] +
                       self.volition["hourly_cycle"])
        decide_state = {
            "schizoid": (current_state["schizoid"] +
                        sun_cycle_state["schizoid"] * self.volition["sun_cycle"] +
                        lunar_cycle_state["schizoid"] * self.volition["lunar_cycle"] +
                        Earth_cycle_state["schizoid"] * self.volition["Earth_cycle"] +
                        hourly_cycle_state["schizoid"] * self.volition["hourly_cycle"])/weights_sum,
            "neurotic": (current_state["neurotic"] +
                        sun_cycle_state["neurotic"] * self.volition["sun_cycle"] +
                        lunar_cycle_state["neurotic"] * self.volition["lunar_cycle"] +
                        Earth_cycle_state["neurotic"] * self.volition["Earth_cycle"] +
                        hourly_cycle_state["neurotic"] * self.volition["hourly_cycle"])/weights_sum,
            "narcissistic": (current_state["narcissistic"] +
                            sun_cycle_state["narcissistic"] * self.volition["sun_cycle"] +
                            lunar_cycle_state["narcissistic"] * self.volition["lunar_cycle"] +
                            Earth_cycle_state["narcissistic"] * self.volition["Earth_cycle"] +
                            hourly_cycle_state["narcissistic"] * self.volition["hourly_cycle"])/weights_sum,
        }

        # Обновление состояния
        self.state = decide_state

    def update_state_by_message(self, message_code):
        # Получение текущего состояния
        current_state = self.get_current_state()

        # Расчёт итогового состояния
        weights_sum = (1 + self.volition["communication"])
        decide_state = {
            "schizoid": (current_state["schizoid"] +
                        message_code["schizoid"] * self.volition["communication"])/weights_sum,
            "neurotic": (current_state["neurotic"] +
                        message_code["neurotic"] * self.volition["communication"])/weights_sum,
            "narcissistic": (current_state["narcissistic"] +
                            message_code["narcissistic"] * self.volition["communication"])/weights_sum
        }

        # Обновление состояния
        self.state = decide_state

    def is_alive(self):
        return self.state["schizoid"]!=0 or self.state["neurotic"]!=0 or self.state["narcissistic"]!=0