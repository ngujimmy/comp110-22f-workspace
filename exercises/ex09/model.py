"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730574005" 


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Calculate distance between 2 points."""
        distance: float = sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def contract_disease(self) -> None:
        """Assign infected constant to sickness attribute of cell."""
        self.sickness = constants.INFECTED

    def tick(self) -> None:
        """Updates simulation."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
      
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "red"
        if self.is_immune():
            return "blue"

    def is_vulnerable(self) -> bool:
        """Returns True if cell's sickness attribute is equal to vulenrable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Returns True if cell's sickness attribute is equal to infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def contact_with(self, other: Cell) -> None:
        """Creates infected if other cell is infected."""
        if other.is_infected() and self.is_vulnerable():
            self.contract_disease()
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
    
    def immunize(self) -> None:
        """Assigns cell as immune. GWEN W."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Returns True if cell's sickness attribute is equal to immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected >= cells or infected <= 0:
            raise ValueError("Must infect some # of cell objects")
        if immune > cells or immune < 0:
            raise ValueError("Must immune some # of cell objects")
        for _ in range(cells - infected - immune):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for _ in range(infected):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            infected_cell: Cell = Cell(start_location, start_direction)
            infected_cell.contract_disease()
            self.population.append(infected_cell)
        for _ in range(immune):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            immune_cell: Cell = Cell(start_location, start_direction)
            immune_cell.immunize()
            self.population.append(immune_cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y: 
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Checks contact between 2 cells."""
        for index_1 in range(constants.CELL_COUNT):
            # index_2: int = index_1 + 1
            # while index_2 < len(self.population):
            for index_2 in range(constants.CELL_COUNT):
                if self.population[index_2].location.distance(self.population[index_1].location) < constants.CELL_RADIUS:
                    self.population[index_2].contact_with(self.population[index_1])
                # index_2 += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for index in self.population:
            if index.is_infected():
                return False
        return True