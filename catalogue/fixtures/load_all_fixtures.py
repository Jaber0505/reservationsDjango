import subprocess
import sys

fixtures = [
    "catalogue/fixtures/users.json",
    "catalogue/fixtures/types.json",
    "catalogue/fixtures/localities.json",
    "catalogue/fixtures/locations.json",
    "catalogue/fixtures/prices.json",
    "catalogue/fixtures/shows.json",
    "catalogue/fixtures/artist.json",
    "catalogue/fixtures/artist_type.json",
    "catalogue/fixtures/representations.json",
    "catalogue/fixtures/reservations.json",
    "catalogue/fixtures/reservation_representation.json",
    "catalogue/fixtures/reviews.json",
]

for f in fixtures:
    print(f">>> loading {f}")
    subprocess.run([sys.executable, "manage.py", "loaddata", f])
