from django.shortcuts import render
from django.http import JsonResponse
import time
import csv
import os
from django.conf import settings


def dashboard(request):
    return render(request, "index.html")


def search_events(request):
    query = request.GET.get("query", "").lower().strip()
    start_time = request.GET.get("start_time", "").strip()
    end_time = request.GET.get("end_time", "").strip()

    start = time.time()
    results = []

    data_folder = os.path.join(settings.BASE_DIR, "data_files")

    if not os.path.exists(data_folder):
        return JsonResponse({
            "results": [],
            "search_time": 0,
            "error": f"Folder not found: {data_folder}"
        })

    for file_name in os.listdir(data_folder):
        if not file_name.endswith(".csv"):
            continue

        file_path = os.path.join(data_folder, file_name)

        with open(file_path, newline="", encoding="utf-8", errors="ignore") as f:
            reader = csv.DictReader(f)

            for row in reader:
                event_name = row.get("event", "").strip()
                event_time = row.get("time", "").strip()

                if not event_name or not event_time:
                    continue

                if query and query not in event_name.lower():
                    continue

                if start_time and event_time < start_time:
                    continue

                if end_time and event_time > end_time:
                    continue

                results.append({
                    "event": event_name,
                    "time": event_time,
                    "file": file_name
                })

    end = time.time()

    return JsonResponse({
        "results": results,
        "search_time": end - start
    })