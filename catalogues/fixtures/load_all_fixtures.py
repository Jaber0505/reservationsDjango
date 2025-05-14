import subprocess
import sys

fixtures = [
    "catalogues/fixtures/users.json",
    "catalogues/fixtures/types.json",
    "catalogues/fixtures/localities.json",
    "catalogues/fixtures/locations.json",
    "catalogues/fixtures/prices.json",
    "catalogues/fixtures/shows.json",
    "catalogues/fixtures/artist.json",
    "catalogues/fixtures/artist_type.json",
    "catalogues/fixtures/representations.json",
    "catalogues/fixtures/reservations.json",
    "catalogues/fixtures/reservation_representation.json",
    "catalogues/fixtures/reviews.json",
]

for f in fixtures:
    print(f">>> loading {f}")
    subprocess.run([sys.executable, "manage.py", "loaddata", f])
