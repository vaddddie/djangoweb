from .models import Cell, Mode
from django.shortcuts import redirect
from .mqttController import output_msg
from datetime import datetime, timezone


def get_button(request, client):
    cells = Cell.objects.all()
    for cell in cells:
        ID = cell.id
        if request.POST.get(f"Rename{ID}") and request.POST.get(f"ChangeName{ID}") != '':
            cell.Name = request.POST.get(f"ChangeName{ID}")
            cell.save()
            return redirect('/Management')

        # ========================= COOLER =========================
        if request.POST.get(f"CoolerOn{ID}") is not None:  # states: 0 - off, 1 - on, 2 - default
            cell.CoolerState = 1
            cell.save()
            msg = {
                "MAC": cell.MacAddress,
                "state": 1
            }
            # output_msg(client, msg, 'test/cooler')
            break

        if request.POST.get(f"CoolerOff{ID}") is not None:
            cell.CoolerState = 0
            cell.save()
            msg = {
                "MAC": cell.MacAddress,
                "state": 2
            }
            # output_msg(client, msg, 'test/cooler')
            break

        if request.POST.get(f"CoolerDefault{ID}") is not None:
            cell.CoolerState = 2
            cell.save()
            msg = {
                "MAC": cell.MacAddress,
                "state": 0
            }
            # output_msg(client, msg, 'test/cooler')
            break

        # ========================= PUMP =========================
        if request.POST.get(f"WateringOn{ID}") is not None:
            cell.PumpState = 1
            cell.save()
            msg = {
                "MAC": cell.MacAddress,
                "state": 1
            }
            # output_msg(client, msg, 'test/pump')
            break

        if request.POST.get(f"WateringOff{ID}") is not None:
            cell.PumpState = 0
            cell.save()
            msg = {
                "MAC": cell.MacAddress,
                "state": 2
            }
            # output_msg(client, msg, 'test/pump')
            break

        if request.POST.get(f"WateringDefault{ID}") is not None:
            cell.PumpState = 2
            cell.save()
            msg = {
                "MAC": cell.MacAddress,
                "state": 0
            }
            # output_msg(client, msg, 'test/pump')
            break

        # ========================= LAMP =========================
        if request.POST.get(f"LightOn{ID}") is not None:
            cell.LampState = 1
            cell.save()
            msg = {
                "MAC": cell.MacAddress,
                "state": 1
            }
            # output_msg(client, msg, 'test/light')
            break

        if request.POST.get(f"LightOff{ID}") is not None:
            cell.LampState = 0
            cell.save()
            msg = {
                "MAC": cell.MacAddress,
                "state": 2
            }
            # output_msg(client, msg, 'test/light')
            break

        if request.POST.get(f"LightDefault{ID}") is not None:
            cell.LampState = 2
            cell.save()
            msg = {
                "MAC": cell.MacAddress,
                "state": 0
            }
            # output_msg(client, msg, 'test/light')
            break

        # ========================= Mode selection =========================
        if request.POST.get(f"Accept{ID}") and request.POST.get("ModsSelect") is not None:
            str_mode = request.POST.get("ModsSelect")
            mode = Mode.objects.get(Name=str_mode)
            cell.Mode = str_mode
            cell.TimeTarget = datetime.now(timezone.utc) + mode.GrowingTime
            cell.save()
            j_string = {
                "ID": cell.MacAddress,
                "IWater": int(mode.Watering_interval.total_seconds() * 1000),
                "TWater": int(mode.Watering_time.total_seconds() * 1000),
                "ILight": int(mode.Lighting_interval.total_seconds() * 1000),
                "TLight": int(mode.Lighting_time.total_seconds() * 1000),
                "Temperature": mode.Temperature,
                "Humidity": mode.Humidity
            }
            # output_msg(client, j_string, 'test/mode')
            break

        if request.POST.get(f'Delete{ID}') is not None:
            cell.delete()
            return redirect('/Management')
