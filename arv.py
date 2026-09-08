#Robot class
class Robot():
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def walk(self):
        pass

    def rest(self):
        pass
    def greet(self):
        print(f"{self.name} is a robot with {self.energy} energy.")
    def move(self, distance):
        energy_cost = abs(distance) * 2
        if self.energy >= energy_cost:
            self.energy -= energy_cost
            print(f"{self.name} moved {distance} units. Energy left: {self.energy}")
        else:
            print(f"{self.name} does not have enough energy to move {distance} units.")

greet = Robot("Arv", 100)
greet.greet()



#BattleRobot
class BattleRobot(Robot):
    def shootLaser(self):
        if self.energy >= 10:
            self.energy -= 10
            print(f"{self.name} shoots a laser! Energy left: {self.energy}")
        else:
            print(f"{self.name} does not have enough energy to shoot a laser.")

print("\nCreating a BattleRobot:")
BattleRobot("BattleBot", 100).shootLaser()

#RepairRobot
class RepairRobot(BattleRobot):
    def repair(self):
        if self.energy >= 5:
            self.energy -= 5
            print(f"{self.name} repairs itself! Energy left: {self.energy}")
        else:
            print(f"{self.name} does not have enough energy to repair itself.")

#MovementRobot
class MovementRobot(RepairRobot):
    def move(self, distance):
        energy_cost = abs(distance) * 1.5
        if self.energy >= energy_cost:
            self.energy -= energy_cost
            print(f"{self.name} moved {distance} units. Energy left: {self.energy}")
        else:
            print(f"{self.name} does not have enough energy to move {distance} units.")




# Creating all robots
print("\nCreating a MovementRobot:")
movement_robot = MovementRobot("MovementBot", 50)
movement_robot.greet()
movement_robot.move(10)

print("\nCreating a RepairRobot:")
repair_robot = RepairRobot("RepairBot", 30)
repair_robot.greet()

print("\nCreating a BattleRobot:")
battle_robot = BattleRobot("BattleBot", 100)
battle_robot.greet()