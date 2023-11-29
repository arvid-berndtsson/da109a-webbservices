# -*- coding: utf-8 -*-

from unicorns import storage
from unicorns.Unicorn import Unicorn
from unicorns.Location import Location

from flask import Flask, request

storage.setup()


app = Flask(__name__)


@app.route("/", methods=['GET'])
def get_unicorns():
    """
    Retrieves a list of unicorns from the storage and returns them as a dictionary.

    Returns:
        dict: A dictionary containing the serialized unicorns.
            The dictionary has a key "unicorns" which maps to a list of serialized unicorn objects.
    """
    unicorns = storage.fetch_unicorns()

    serialized_unicorns = []
    for unicorn in unicorns:
        serialized_unicorns.append(unicorn.to_dict())
    return {"unicorns": serialized_unicorns}


@app.route("/<int:id>", methods=['GET'])
def get_unicorn(id):
    unicorn = storage.fetch_unicorn(id)
    try:
        return unicorn.to_dict(), 200
    except AttributeError:
        return "Unicorn not found", 404


@app.route("/<int:id>", methods=['PUT'])
def update_unicorn(id):
    """
    Update the details of a unicorn.

    Args:
        id (int): The ID of the unicorn to update.

    Returns:
        str: The status of the update operation.

    Raises:
        KeyError: If any required field is missing in the request data.

    """

    data = request.json

    try:
        unicorn = Unicorn(
            id=id,
            name=data['name'],
            description=data['description'],
            reported_by=data['reportedBy'],
            spotted_where=Location(
                name=data['spottedWhere']['name'],
                lat=data['spottedWhere']['lat'],
                lon=data['spottedWhere']['lon']
            ),
            spotted_when=data['spottedWhen'],
            image=data['image']
        )

    except KeyError as e:
        return "Missing required field: " + str(e), 400

    if not storage.update_unicorn(unicorn):
        return "Unicorn not found", 404

    return "OK", 200


@app.route('/', methods=['POST'])
def add_unicorn():
    """
    Add a new unicorn.

    Returns:
        str: A string indicating the success of the update.

    Raises:
        KeyError: If any required fields are missing in the request data.
    """

    data = request.json

    unicorn = Unicorn(
        id=id,
        name=data['name'],
        description=data['description'],
        reported_by=data['reportedBy'],
        spotted_where=Location(
            name=data['spottedWhere']['name'],
            lat=data['spottedWhere']['lat'],
            lon=data['spottedWhere']['lon']
        ),
        spotted_when=data['spottedWhen'],
        image=data['image']
    )
    if not storage.add_unicorn(unicorn):
        return "Unicorn not added", 400
    return "OK", 201


@app.route('/<int:id>', methods=['DELETE'])
def delete_unicorn(id):
    """
    Delete a unicorn.

    Args:
        id (int): The ID of the unicorn to delete.

    Returns:
        str: A string indicating the success of the update.
    """

    if not storage.delete_unicorn(id):
        return "Unicorn not found", 404
    return "OK", 200


if __name__ == '__main__':
    app.run(debug=True)
