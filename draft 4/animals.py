from basics import *
from variables import *

class Animal:
    def __init__(self, x, y, animal):
        self.x = x
        self.y = y

        self.animal = animal

        self.timer = 0

        self.direction = "down"

    def move(self, blocks_map, objects_map, scenery_map, animal_map):
        if self.timer == 0:
            paths = [(self.x, self.y), (self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1), (self.x, self.y + 1)]
            possible_paths = []
            for path in paths:
                if (blocks_map[path[1]][path[0]] != 3) \
                        and (objects_map[path[1]][path[0]] == "") \
                        and (scenery_map[path[1]][path[0]] == "") \
                        and (0 <= path[0] <= 17) and (0 <= path[1] <= 13):
                    possible_paths.append(path)

            if len(possible_paths) > 0:
                path_take = random.choice(possible_paths)
                animal = Animal(path_take[0], path_take[1], self.animal)
                animal_map[self.y][self.x] = ""
                animal_map[path_take[1]][path_take[0]] = animal
                if (path_take[0] - self.x) > 0:
                    animal.direction = "right"
                elif (path_take[0] - self.x < 0):
                    animal.direction = "left"
                elif (path_take[1] - self.y > 0):
                    animal.direction = "down"
                elif (path_take[1] - self.y < 0):
                    animal.direction = "up"
                else:
                    animal.direction = "down"

    def draw(self):
        draw_image(animal_images[self.animal][self.direction], mid_x_coord + self.x * TILE + TILE, mid_y_coord + self.y * TILE,
                   img_dir, my_screen, 1)

    def update(self, blocks_map, objects_map, scenery_map, animal_map):
        self.timer += 1
        if self.timer == 10:
            self.timer = 0
        self.move(blocks_map, objects_map, scenery_map, animal_map)
