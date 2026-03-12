from django.shortcuts import render
from django.http import JsonResponse
import time
import csv
import os
from django.conf import settings


def dashboard(request):
    return render(request, "index.html")


def search_events(request):
    query = request.GET.get("query", "").lower()
    start_time = request.GET.get("start_time", "")
    end_time = request.GET.get("end_time", "")

    start = time.time()
    results = []

    data_folder = os.path.join(settings.BASE_DIR, "data_files")

    for file_name in os.listdir(data_folder):
        if file_name.endswith(".csv"):
            file_path = os.path.join(data_folder, file_name)

            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    event_name = row["event"].lower()
                    event_time = row["time"]

                    if query and query not in event_name:
                        continue

                    if start_time and event_time < start_time:
                        continue

                    if end_time and event_time > end_time:
                        continue

                    results.append({
                        "event": row["event"],
                        "time": row["time"],
                        "file": file_name
                    })

    end = time.time()

    return JsonResponse({
        "results": results,
        "search_time": end - start
    })