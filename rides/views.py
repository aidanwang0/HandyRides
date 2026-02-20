import re
from django.shortcuts import render
from django.db.models import Q

from .models import Person
from .forms import RideForm


def index(request):
    context = {}
    form = RideForm(request.GET or None)
    context["form"] = form

    state_raw = request.GET.get("state", "").strip()
    city_raw = request.GET.get("city", "").strip()

    if state_raw:
        # State: match destination state or origination state (case-insensitive); fallback to state in address
        if len(state_raw) == 2:
            state_in_address = ", " + state_raw + " "
            queryset = Person.objects.filter(
                Q(destination_state__iexact=state_raw)
                | Q(origination_state__iexact=state_raw)
                | Q(origination__icontains=state_in_address)
            )
        else:
            queryset = Person.objects.filter(
                Q(destination_state__iexact=state_raw)
                | Q(origination_state__iexact=state_raw)
            )
        if city_raw:
            city_escaped = re.escape(city_raw)
            city_in_address_regex = r",\s*[^,]*" + city_escaped + r"[^,]*,\s*[A-Za-z]{2}\s+\d"
            queryset = queryset.filter(
                Q(origin_city__icontains=city_raw)
                | Q(destination_city__icontains=city_raw)
                | Q(origination__iregex=city_in_address_regex)
            )
        context["people"] = queryset.order_by("date", "time")
        context["inputExists"] = True
    else:
        context["people"] = []
        context["inputExists"] = False

    return render(request, "index_view.html", context)
