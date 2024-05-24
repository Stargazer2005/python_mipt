"""
В этом модуле хранятся функции для применения МНК
"""


from typing import Optional
from numbers import Real       # раскомментируйте при необходимости

from lsm_project.event_logger.event_logger import EventLogger

from lsm_project.lsm.enumerations import MismatchStrategies
from lsm_project.lsm.models import (
    LSMDescription,
    LSMStatistics,
    LSMLines,
)


PRECISION = 3                   # константа для точности вывода
event_logger = EventLogger()    # для логирования


def get_lsm_description(
    abscissa: list[float], ordinates: list[float],
    mismatch_strategy: MismatchStrategies = MismatchStrategies.FALL
) -> LSMDescription:
    """
    Функции для получения описания рассчитаной зависимости

    :param: abscissa - значения абсцисс
    :param: ordinates - значение ординат
    :param: mismatch_strategy - стратегия обработки несовпадения

    :return: структура типа LSMDescription
    """

    global event_logger
    event_logger.info('Started calculating dependency description')

    _is_valid_measurements(abscissa)
    event_logger.info('Abscissa measurements are right')
    _is_valid_measurements(ordinates)
    event_logger.info('Ordinates measurements are right')

    if len(abscissa) != len(ordinates):
        event_logger.warning('Abscissa and ordinates mismatch')
        _process_mismatch(abscissa, ordinates, mismatch_strategy)

    event_logger.info('Description was got successfully')
    return _get_lsm_description(abscissa, ordinates)


def get_lsm_lines(
    abscissa: list[float], ordinates: list[float],
    lsm_description: Optional[LSMDescription] = None
) -> LSMLines:
    """
    Функция для расчета значений функций с помощью результатов МНК

    :param: abscissa - значения абсцисс
    :param: ordinates - значение ординат
    :param: lsm_description - описание МНК

    :return: структура типа LSMLines
    """

    event_logger.info('Started calculating dependency lines')

    if (lsm_description is None):
        lsm_description = _get_lsm_description(abscissa, ordinates)

    if not (isinstance(lsm_description, LSMDescription)):
        event_logger.error('Wrong dependency description')
        raise TypeError()

    n = len(abscissa)

    line_predicted = [lsm_description.incline*abscissa[i] + lsm_description.shift for i in range(n)]

    line_above = [(lsm_description.incline + lsm_description.incline_error)*abscissa[i] +
                  (lsm_description.shift + lsm_description.shift_error) for i in range(n)]

    line_under = [(lsm_description.incline - lsm_description.incline_error)*abscissa[i] +
                  (lsm_description.shift - lsm_description.shift_error) for i in range(n)]
    event_logger.info('Lines were calculated successfully')
    return LSMLines(
        abscissa,
        ordinates,
        line_predicted,
        line_above,
        line_under
    )


def get_report(
    lsm_description: LSMDescription, path_to_save: str = ''
) -> str:
    """
    Функция для формирования отчета о результатах МНК

    :param: lsm_description - описание МНК
    :param: path_to_save - путь к файлу для сохранения отчета

    :return: строка - отчет определенного формата
    """
    global PRECISION
    report = 'LSM computing result'.center(100, '=') + '\n\n'
    report += f'[INFO]: incline: {lsm_description.incline:.{PRECISION}f};\n'
    report += f'[INFO]: shift: {lsm_description.shift:.{PRECISION}f};\n'
    report += f'[INFO]: incline error: {lsm_description.incline_error:.{PRECISION}f};\n'
    report += f'[INFO]: shift error: {lsm_description.shift_error:.{PRECISION}f};\n\n' + 100*'='
    if (path_to_save != ''):
        file = open(path_to_save, 'w')
        file.write(report)
    return report


# служебная функция для валидации
def _is_valid_measurements(measurements: list[float]) -> bool:
    if (not (isinstance(measurements, list))):
        if not (list(measurements)):
            event_logger.error('Can not turn measurement data into list-type')
            raise TypeError()

    for num in measurements:
        if not (isinstance(num, Real)):
            event_logger.error('Data is not numeric')
            raise ValueError()

    if (len(measurements) <= 2):
        event_logger.error('Not enough measurement data')
        raise ValueError()

    return True


# служебная функция для обработки несоответствия размеров
def _process_mismatch(
    abscissa: list[float], ordinates: list[float],
    mismatch_strategy: MismatchStrategies = MismatchStrategies.FALL
) -> tuple[list[float], list[float]]:
    global event_logger
    if (mismatch_strategy == MismatchStrategies.FALL):
        event_logger.error('Mismatched data')
        raise RuntimeError()

    elif (mismatch_strategy == MismatchStrategies.CUT):
        min_l = min(len(abscissa), len(ordinates))
        abscissa = abscissa[:min_l]
        ordinates = ordinates[:min_l]
        event_logger.warning('Some measuremnet data was cut')

    else:
        event_logger.error('Invalid mismatch stragedy')
        raise ValueError()

    return [abscissa, ordinates]


# служебная функция для получения статистик
def _get_lsm_statistics(
    abscissa: list[float], ordinates: list[float]
) -> LSMStatistics:
    global event_logger, PRECISION
    n = len(abscissa)

    Sx = sum(abscissa)
    abscissa_mean = Sx/n

    Sy = sum(ordinates)
    ordinate_mean = Sy/n

    Sxy = sum(abscissa[i]*ordinates[i] for i in range(n))
    product_mean = Sxy/n

    Sxx = sum(abscissa[i]**2 for i in range(n))
    abs_squared_mean = Sxx/n

    return LSMStatistics(
        abscissa_mean,
        ordinate_mean,
        product_mean,
        abs_squared_mean
    )


# служебная функция для получения описания МНК
def _get_lsm_description(
    abscissa: list[float], ordinates: list[float]
) -> LSMDescription:
    global event_logger, PRECISION

    lsm_statistics = _get_lsm_statistics(abscissa, ordinates)

    incline = ((lsm_statistics.product_mean -
                lsm_statistics.abscissa_mean * lsm_statistics.ordinate_mean) /
               (lsm_statistics.abs_squared_mean - (lsm_statistics.abscissa_mean)**2))

    shift = lsm_statistics.ordinate_mean - incline * lsm_statistics.abscissa_mean

    n = len(abscissa)

    sigma_y = (sum((ordinates[i] - incline * abscissa[i] - shift)**2
                   for i in range(n))/(n-2))**(1/2)

    incline_error = (sigma_y**2/(n*(lsm_statistics.abs_squared_mean -
                                    lsm_statistics.abscissa_mean**2)))**(1/2)

    shift_error = ((sigma_y**2 * lsm_statistics.abs_squared_mean) /
                   (n*(lsm_statistics.abs_squared_mean - lsm_statistics.abscissa_mean**2)))**(1/2)
    return LSMDescription(
        incline,
        shift,
        incline_error,
        shift_error
    )
