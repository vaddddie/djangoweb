from .models import Cell, Mode
from datetime import datetime, timedelta, timezone
from django.core.exceptions import ObjectDoesNotExist

# time of the last message
boundary_interval = 15

temperature_border = 5
humidity_border = 10

def timer():
    cells = Cell.objects.all()
    for cell in cells:
        try:
            mode = Mode.objects.get(Name=cell.Mode)
            seconds = int((cell.TimeTarget - datetime.now(timezone.utc)).total_seconds())

            if seconds > 0:
                days, _ = divmod(seconds, 86400)
                hours, _ = divmod(_, 3600)
                minutes, _ = divmod(_, 60)

                hours = f"{hours}".zfill(2)
                minutes = f"{minutes}".zfill(2)
            else:
                days = 0
                hours = minutes = '00'

            if days == 1:
                suffix = ''
            else:
                suffix = 's'

            cell.TimeLeft = f'{days} day{suffix}, {hours}:{minutes}'

            ABSTime = mode.GrowingTime.total_seconds()

            if seconds > 0:
                cell.GrowthProcess = (1 - seconds / ABSTime) * 100
            else:
                cell.GrowthProcess = 100

        except Mode.DoesNotExist:
            cell.GrowthProcess = 0
            cell.TimeLeft = 'None'

        # Checking online
        try:
            if abs(datetime.now(timezone.utc) - cell.TimeOfTheLastMessage) > timedelta(0, boundary_interval):
                cell.Online = False
            else:
                cell.Online = True
        except TypeError:
            print("======== TypeError! ==========")
            cell.TimeOfTheLastMessage = datetime.now(timezone.utc) - timedelta(0, boundary_interval)
        cell.save()


def choose_the_arrow():  # 0 - none; +-1 - green arrow; +-2 - red arrow;
    cells = Cell.objects.all()
    for cell in cells:
        str_mode = cell.Mode
        try:
            mode = Mode.objects.get(Name=str_mode)

            # ================ Temperature ================
            tmp = cell.Temperature - mode.Temperature
            if tmp > 0:
                sign = 1
            else:
                sign = -1

            if abs(tmp) == 0:
                t_value = 0
            elif abs(tmp) < temperature_border:
                t_value = 1 * sign
            else:
                t_value = 2 * sign

            # ================ Humidity ================
            tmp = cell.Humidity - mode.Humidity
            if tmp > 0:
                sign = 1
            else:
                sign = -1

            if abs(tmp) == 0:
                h_value = 0
            elif abs(tmp) < humidity_border:
                h_value = 1 * sign
            else:
                h_value = 2 * sign

            cell.Temperature_arrow = t_value
            cell.Humidity_arrow = h_value
            cell.save()
        except ObjectDoesNotExist:
            print("======== Mode not found! ==========")
            cell.Temperature_arrow = 0
            cell.Humidity_arrow = 0
            cell.save()
