import click
from flask.cli import FlaskGroup

from app import app, db
from app.models.greeting import Greet
from app.models.user import User

cli = FlaskGroup(app)


@app.cli.command("create_db")
def create_db():
    """Create the database tables."""
    db.drop_all()
    db.create_all()
    db.session.commit()
    click.echo("Database tables created.")


@app.cli.command("drop_db")
def drop_db():
    """Drop the database tables."""
    db.drop_all()
    db.session.commit()
    click.echo("Database tables dropped.")


@app.cli.command("seed_db")
def seed_db():
    """Seed the database with initial data."""
    greetings = [
        Greet(msg="Hello, world!"),
        Greet(msg="Hi there!"),
        Greet(msg="Greetings!"),
    ]
    for greet in greetings:
        db.session.add(greet)

    db.session.commit()

    users = [
        User(username="admin", password="admin"),
        User(username="user", password="user"),
    ]

    for user in users:
        db.session.add(user)

    db.session.commit()

    click.echo("Database seeded with initial data.")


if __name__ == "__main__":
    cli()
