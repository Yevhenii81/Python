# ------------------------------
# MODEL
# ------------------------------

class Actor:
    def __init__(self, full_name: str, role: str):
        self.full_name = full_name
        self.role = role

    def __str__(self):
        return f"{self.full_name} — {self.role}"


class Film:
    def __init__(self, title, genre, director, year, duration, studio, actors=None):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors if actors else []

    def add_actor(self, actor: Actor):
        self.actors.append(actor)


# ------------------------------
# TEMPLATE
# ------------------------------

FILM_TEMPLATE = """
---------------- Фільм ----------------
Назва: {title}
Жанр: {genre}
Режисер: {director}
Рік випуску: {year}
Тривалість: {duration} хв
Студія: {studio}

Акторський склад:
{actors}
--------------------------------------
"""


# ------------------------------
# VIEW
# ------------------------------

class FilmView:
    @staticmethod
    def render(film: Film):
        actors_rendered = "\n".join(f"   • {str(actor)}" for actor in film.actors)

        print(FILM_TEMPLATE.format(
            title=film.title,
            genre=film.genre,
            director=film.director,
            year=film.year,
            duration=film.duration,
            studio=film.studio,
            actors=actors_rendered if actors_rendered else "   (Немає даних)"
        ))


# ------------------------------
# CONTROLLER
# ------------------------------

class FilmController:
    def __init__(self, film: Film):
        self.film = film

    def add_actor(self, name, role):
        self.film.add_actor(Actor(name, role))

    def show(self):
        FilmView.render(self.film)


# ------------------------------
# USE CASE 
# ------------------------------

if __name__ == "__main__":
    film = Film(
        title="Інтерстеллар",
        genre="Фантастика",
        director="Крістофер Нолан",
        year=2014,
        duration=169,
        studio="Paramount Pictures"
    )

    controller = FilmController(film)

    controller.add_actor("Меттью Макконахі", "Купер")
    controller.add_actor("Енн Гетевей", "Амілія Бранд")
    controller.add_actor("Джессіка Честейн", "Мерфі")

    controller.show()
