from typing import Callable
import math

class DFT:
    """
    Класс для выполнения ДПФ
    """

    class ComplexAmplitude:
        """
        Комлпексная амплитуда
        """

        def __init__(self, freq: float, amplitude: float, phase: float):
            """
            Коструктор:

            Параметры:
                freq - частота
                amplitude - амплитуда
                phase - фаза
            """

            self.__freq: float = freq
            self.__amplitude: float = amplitude
            self.__phase: float = phase


        @property
        def freq(self) -> float:
            """
            Частота сигнала
            """

            return self.__freq


        @property
        def amplitude(self) -> float:
            """
            Амлитуда сигнала
            """

            return self.__amplitude


        @property
        def phase(self) -> float:
            """
            Фаза сигнала
            """

            return self.__phase


    def __init__(self, T: int, SF: int, F: Callable):
        """
        Коструктор

        Параметры:
            T - время измерений
            SF - частота дискртизации
            F - входная функция
        """

        self.T: int = T
        self.N: int = T * SF
        self.SF: int = SF

        self.input: list[float] = [F(i * self.T / self.N) for i in range(self.N)]
    

    def calculate(self) -> list[ComplexAmplitude]:
        """
        Запускает расчет ДПФ
        """

        freqs: list[int] = self.__freqs()
        result: list[float] = list()

        for i, k in enumerate(range(self.N)):
            xk: complex = self.__xk(k)

            module = (1 / self.N) * math.sqrt(pow(xk.real, 2) + pow(xk.imag, 2))
            argument = math.atan2(xk.imag, xk.real)

            result.append(DFT.ComplexAmplitude(freqs[i], module * 2, argument))

        return result


    def __xk(self, k: int) -> complex:
        """
        Просчитывает значение для определенного индекса частоты

        Параметры:
            k - индекс частоты

        Возвращаемое значение: результат вычисления для переденного k
        """

        return sum([self.input[i] * pow(math.e, (-(1j * 2 * math.pi) / self.N * k * i)) for i in range(0, self.N)])


    def __freqs(self) -> list[int]:
        """
        Подсчитывает частоты сигалов
        """

        f: list[int] = list()

        if self.N % 2 == 0:
            for i in range(int(self.N / 2 - 1 + 1)):
                f.append(i / ((1 / self.SF) * self.N))

            for i in range(int(-self.N / 2), -1 + 1):
                f.append(i / ((1 / self.SF) * self.N))
        else:
            for i in range(int((self.N - 1) / 2 + 1)):
                f.append(i / ((1 / self.SF) * self.N))

            for i in range(int(-(self.N - 1) / 2), -1 + 1):
                f.append(i / ((1 / self.SF) * self.N))

        return f