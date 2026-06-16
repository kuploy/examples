from django.db import connection
from django.http import HttpResponse


def home(request):
    with connection.cursor() as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS visits (count int)")
        cur.execute(
            "INSERT INTO visits (count) SELECT 0 WHERE NOT EXISTS (SELECT 1 FROM visits)"
        )
        cur.execute("UPDATE visits SET count = count + 1")
        cur.execute("SELECT count FROM visits")
        n = cur.fetchone()[0]
    return HttpResponse(f"Hello from Kuploy Stacks! Visits: {n}")
