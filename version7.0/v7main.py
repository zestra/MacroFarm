8# MacroFarm, Version 6
# Started on 21 Jan 2023, finished on ... Jan 2023
# By Czeslaw H.Z.T
# for self-satisfaction, Aldar Academies, friends, and family

from basics import *

pygame.init()
WIDTH, HEIGHT = 1470, 956  
my_window = pygame.display.set_mode((WIDTH, HEIGHT), NOFRAME)


images = {"Animal" : {"chick": {"down" : "chick_front", 
                                 "up"   : "chick_back",
                                 "right": "chick_right",
                                 "left" : "chick_left"}, \

                       "goat" : {"down" : "goat_front", 
                                 "up"   : "goat_back",
                                 "right": "goat_right",
                                 "left" : "goat_left"}, \

                       "sheep": {"down" : "sheep_front", 
                                 "up"   : "sheep_back",
                                 "right": "sheep_right",
                                 "left" : "sheep_left"}, \

                       "pig"  : {"down" : "pig_front", 
                                 "up"   : "pig_back",
                                 "right": "pig_right",
                                 "left" : "pig_left"}, \
                                 
                        "mole": {"down"  : "mole_front", 
                                 "up"    : "mole_back",
                                 "right" : "mole_right",
                                 "left"  : "mole_left"}, \

                       "rabbit": {"down" : "rabbit_front", 
                                  "up"   : "rabbit_back",
                                  "right": "rabbit_right",
                                  "left" : "rabbit_left"}, \

                       "snail" : {"down" : "snail_front", 
                                  "up"   : "snail_back",
                                  "right": "snail_right",
                                  "left" : "snail_left"}},

          "Player"  : {"1": {"down" : "1front", 
                             "up"   : "1back",
                             "right": "1right",
                             "left" : "1left"},

                       "2": {"down" : "2front", 
                             "up"   : "2back",
                             "right": "2right",
                             "left" : "2left"},

                       "3": {"down" : "3front", 
                             "up"   : "3back",
                             "right": "3right",
                             "left" : "3left"}},

          "Object"  : {"axe"        : "axe", 
                       "coin"       : "coin", 
                       "fence"      : "fence",
                       "log"        : "log", 
                       "nut"        : "nut", 
                       "meat"       : "meat",
                       "pear"       : "pear",
                       "broccoli"   : "broccoli",
                       "carrot"     : "carrot",
                       "shell"      : "shell",
                       "cherry"     : "cherry",
                       "wateringcan": "wateringcan",
                       "shovel"     : "shovel"},

          "Scenery" : {"autumn_tree": "autumn_tree",
                       "cherry_tree": "cherry_tree",
                       "norm_tree"  : "norm_tree"},

          "Building": {"bank"     : "bank",
                       "farm"    : "farm",
                       "well"     : "well",
                       "shop"     : "shop",
                       "carpenter": "carpenter",
                       "factory": "factory"},
                       
          "Block": {"dirt"  : "dirt",
                    "grass" : "grass",
                    "ground": "ground",
                    "stone" : "stone",
                    "water" : "water"}}

item_data = {"coin"       : {"race": "CURRENCY" , "cost": ["1 coin"]                    , "image_filename": images["Object"]["coin"]         },
                                                                                                                                             
             "meat"       : {"race": "FOOD"     , "cost": ["1 coin"]                    , "image_filename": images["Object"]["meat"]         },
             "pear"       : {"race": "FOOD"     , "cost": ["2 coin"]                    , "image_filename": images["Object"]["pear"]         },
             "cherry"     : {"race": "FOOD"     , "cost": ["3 coin"]                    , "image_filename": images["Object"]["cherry"]       },
             "carrot"     : {"race": "FOOD"     , "cost": ["2 coin"]                    , "image_filename": images["Object"]["carrot"]       },
             "broccoli"   : {"race": "FOOD"     , "cost": ["3 coin"]                    , "image_filename": images["Object"]["broccoli"]     },

             "shell"      : {"race": "FUEL"     , "cost": ["4 coin"]                    , "image_filename": images["Object"]["shell"]        },
             "nut"        : {"race": "FUEL"     , "cost": ["2 coin"]                    , "image_filename": images["Object"]["nut"]          },
             "wateringcan": {"race": "FUEL"     , "cost": ["2 coin"]                    , "image_filename": images["Object"]["wateringcan"]  },
             "log"        : {"race": "FUEL"     , "cost": ["2 coin"]                    , "image_filename": images["Object"]["log"]          },
                                                                                                                                             
             "axe"        : {"race": "CARPENTRY", "cost": ["1 coin", "1 log", "1 stone"], "image_filename": images["Object"]["axe"]          },
             "shovel"     : {"race": "CARPENTRY", "cost": ["1 coin", "1 log", "1 stone"], "image_filename": images["Object"]["shovel"]       },
             "fence"      : {"race": "CARPENTRY", "cost": ["2 coin", "2 log"]           , "image_filename": images["Object"]["fence"]        },

             "chick"      : {"race": "ANIMAL"   , "cost": ["8 coin", "2 meat"]          , "image_filename": images["Animal"]["chick"]["down"]},
             "sheep"      : {"race": "ANIMAL"   , "cost": ["6 coin", "1 shell"]         , "image_filename": images["Animal"]["sheep"]["down"]},
             "goat"       : {"race": "ANIMAL"   , "cost": ["7 coin", "2 pear"]          , "image_filename": images["Animal"]["goat"]["down"] },
             "pig"        : {"race": "ANIMAL"   , "cost": ["7 coin", "1 cherry"]        , "image_filename": images["Animal"]["pig"]["down"]  },

             "snail"      : {"race": "PEST"     , "cost": ["3 shell"]                   , "image_filename": images["Animal"]["snail"]["down"]},

             "dirt"       : {"race": "BLOCK"    , "cost": ["2 coin"]                    , "image_filename": images["Block"]["dirt"]          },
             "grass"      : {"race": "BLOCK"    , "cost": ["2 coin"]                    , "image_filename": images["Block"]["grass"]         },
             "ground"     : {"race": "BLOCK"    , "cost": ["2 coin"]                    , "image_filename": images["Block"]["ground"]        },
             "stone"      : {"race": "BLOCK"    , "cost": ["2 coin"]                    , "image_filename": images["Block"]["stone"]         },
             "water"      : {"race": "BLOCK"    , "cost": ["2 coin"]                    , "image_filename": images["Block"]["water"]         }
             }

inventory = {"coin": {"image_filename": item_data["coin"]["image_filename"],
                      "count": 20,
                      "activated": False},

             "meat": {"image_filename": item_data["meat"]["image_filename"],
                      "count": 70,
                      "activated": False},

             "pear": {"image_filename": item_data["pear"]["image_filename"],
                      "count": 50,
                      "activated": False},

             "cherry": {"image_filename": item_data["cherry"]["image_filename"],
                        "count": 20,
                        "activated": False},

             "carrot": {"image_filename": item_data["carrot"]["image_filename"],
                        "count": 15,
                        "activated": False},

             "broccoli": {"image_filename": item_data["broccoli"]["image_filename"],
                            "count": 10,
                            "activated": False},

             "wateringcan": {"image_filename": item_data["wateringcan"]["image_filename"],
                             "count": 6,
                             "activated": False},

             "nut": {"image_filename": item_data["nut"]["image_filename"],
                     "count": 2,
                     "activated": False},

             "log": {"image_filename": item_data["log"]["image_filename"],
                     "count": 12,
                     "activated": False},

             "shell": {"image_filename": item_data["shell"]["image_filename"],
                       "count": 6,
                       "activated": False},

             "axe": {"image_filename": item_data["axe"]["image_filename"],
                     "count": 6,
                     "activated": False},

             "shovel": {"image_filename": item_data["shovel"]["image_filename"],
                        "count": 4,
                        "activated": False},

             "fence": {"image_filename": item_data["fence"]["image_filename"],
                       "count": 12,
                       "activated": False},

             "chick": {"image_filename": item_data["chick"]["image_filename"],
                       "count": 2,
                       "activated": False},

             "goat": {"image_filename": item_data["goat"]["image_filename"],
                      "count": 2,
                      "activated": False},

             "pig": {"image_filename": item_data["pig"]["image_filename"],
                     "count": 2,
                     "activated": False},

             "sheep": {"image_filename": item_data["sheep"]["image_filename"],
                       "count": 2,
                       "activated": False},

             "snail": {"image_filename": item_data["snail"]["image_filename"],
                       "count": 2,
                       "activated": False},

             "dirt": {"image_filename": item_data["dirt"]["image_filename"],
                      "count": 2,
                      "activated": False},
             "ground": {"image_filename": item_data["ground"]["image_filename"],
                        "count": 2,
                        "activated": False},
             "grass": {"image_filename": item_data["grass"]["image_filename"],
                       "count": 2,
                       "activated": False},
             "stone": {"image_filename": item_data["stone"]["image_filename"],
                       "count": 2,
                       "activated": False},
             "water": {"image_filename": item_data["water"]["image_filename"],
                       "count": 2,
                       "activated": False}
             }

sorted_inventory = {}
for item in item_data:
    sorted_inventory[item_data[item]["race"]] = []
for item in inventory:
    sorted_inventory[item_data[item]["race"]].append(item)

print(sorted_inventory)

shop = {"log", "meat", "pear", "cherry", "nut", "stone"}

carpenter = {"axe", "shovel", "fence"}

farm = {'chick', "sheep", "goat", "pig"}

factory = {"grass", "dirt", "stone", "ground", "water"}

well = {"wateringcan"}

inventory_indexes = []
for sector in sorted_inventory:
    for item in sorted_inventory[sector]:
        inventory_indexes.append(item)

print(inventory_indexes)

shop_indexes = []
for item in shop:
    shop_indexes.append(item)

carpenter_indexes = []
for item in carpenter:
    carpenter_indexes.append(item)

farm_indexes = []
for item in farm:
    farm_indexes.append(item)

factory_indexes = []
for item in factory:
    factory_indexes.append(item)

well_indexes = []
for item in well:
    well_indexes.append(item)

timer = {"minutes": 10, "seconds": 30}
clock = pygame.time.Clock()
time_up = False

class Sprite:
    """The Sprite class is the parent class for both organisms and objects."""
    
    def __init__(self, race, x, y):
        self.race = race
        self.x, self.y = x, y
    
    def render(self):
        if self.race == "":
            return

        if int(visible_width_index - (visible_window_width + 1)/2) < self.x < int(visible_width_index + (visible_window_width + 1)/2) and \
           int(visible_height_index - (visible_window_height + 1)/2) < self.y < int(visible_height_index + (visible_window_height + 1)/2):
            draw_image(my_window, self.image_filename, (self.x - int(visible_width_index - (visible_window_width + 1)/2))*TILE + mid_x_coord, 
                                                       (self.y - 1 - int(visible_height_index - (visible_window_height + 1)/2))*TILE - mid_y_coord, 
                                                       img_dir, True)
    
    def update(self):
        return

class Organism(Sprite):

    """Organism is the parent class for all organisms in the game.
    These organisms include the main player, nice animals, and bad animals."""

    def __init__(self, race, x, y):
        super().__init__(race, x, y)

        self.direction = "down"
        self.clock = pygame.time.Clock()
        self.motion_timer = 0
        self.motion_max = 0.5
        self.health_timer = 0
        self.health = 100
        self.money_timer = 0
        self.money_owed = 0

    def update(self):        
        if self.health <= 0:
            animal_map[self.y][self.x] = Blank(self.x, self.y)
            return False
            
        time_passed_milliseconds = self.clock.tick()
        time_passed_seconds = time_passed_milliseconds/1000
        self.motion_timer += time_passed_seconds
        self.health_timer += time_passed_seconds
        self.money_timer += time_passed_seconds

        if self.motion_timer < self.motion_max:
            return False
        else:
            self.motion_timer = 0
        
        if self.health_timer > 4:
            self.health -= 10
            self.health_timer = 0
        if self.money_timer > 5:
            self.money_owed += 2
            self.money_timer = 0
    
    def draw_health(self):
        image_width, image_height = image_to_surface(self.image_filename, img_dir, True).get_size()

        draw_rect(my_window, 
                  (self.x - int(visible_width_index - (visible_window_width + 1)/2))*TILE + mid_x_coord - (2/3)*(image_width/2),
                  (self.y - 1 - int(visible_height_index - (visible_window_height + 1)/2))*TILE - mid_y_coord + 10 - (2/3)*image_height, 
                  30, 10, "white", True, "left")

        if self.health > 70:
            health_bar_colour = "green"
        elif self.health > 40:
            health_bar_colour = "orange"
        else:
            health_bar_colour = "red"

        draw_rect(my_window, 
                  (self.x - int(visible_width_index - (visible_window_width + 1)/2))*TILE + mid_x_coord - (2/3)*(image_width/2), 
                  (self.y - 1 - int(visible_height_index - (visible_window_height + 1)/2))*TILE - mid_y_coord + 10 - (2/3)*image_height, 
                  self.health*3/10, 10, health_bar_colour, True, "left")

        draw_text(my_window, str(self.health) + " %", 
                  (self.x - int(visible_width_index - (visible_window_width + 1)/2))*TILE + mid_x_coord + 15 - (2/3)*(image_width/2), 
                  (self.y - 1 - int(visible_height_index - (visible_window_height + 1)/2))*TILE - mid_y_coord + 5 - (2/3)*image_height,
                  7, "black", "arial", "center")

    def render(self):
        Sprite.render(self)
        self.draw_health()

class Player(Organism):

    """The Player is the class for your player."""

    def __init__(self, x, y):
        super().__init__("player", x, y)
        self.motion_max = 0.05

        self.style = "1"
        self.frame = 0
        
        self.image_filename = images["Player"][self.style][self.direction] + str(self.frame)

        self.selected_inventory_item_index = 0
        self.selected_inventory_item = inventory_indexes[self.selected_inventory_item_index]

        self.selected_consumer_item_index = 0
        self.selected_consumer_item = shop_indexes[self.selected_consumer_item_index]

        self.current_storage = "inventory"

        self.currency = "coin"

        self.financial_stock_value = 0

        self.automate_survival = False

        self.in_building = False

        self.axe_hits = 0
        self.shovel_hits = 0

        self.money_owed = 20

        self.notify = False
        self.notification_visibility = 100
        self.transition_timer = pygame.time.Clock()

        self.fade_in = 1

    def transition(self):
        if self.notify is False:
            return

        self.transition_timer = pygame.time.Clock()
        milliseconds_passed = self.transition_timer.tick()
        seconds_passed = milliseconds_passed*1000

        if self.fade_in == 0:
            self.notification_visibility += seconds_passed*(100/10)
            if self.notification_visibility > 100:
                self.fade_in = 1
                self.notify = False
        
        if self.fade_in == 2:
            self.notification_visibility -= seconds_passed*(100/10)
            if self.notification_visibility < 0:
                self.fade_in = 1
                self.notify = False
        
        pygame.time.delay(10000000)

    def draw_inventory(self):
        draw_rect(my_window, 275 / 2, HEIGHT / 2 + 2, 275, visible_window_height * TILE, "white", True)
        draw_rect(my_window, 275 / 2, HEIGHT / 2 + 2, 270, visible_window_height * TILE - 5, (40, 40, 40), True)

        row_index_max = 3

        row_index2 = 0
        for sector in sorted_inventory:
            if sector == item_data[self.selected_inventory_item]["race"]:
                row_index = -row_index2
            row_index2 += int(len(sorted_inventory[sector])) + 1

        item_row_index = 0
        for sector in sorted_inventory:
            if sector == item_data[self.selected_inventory_item]["race"]:
                draw_rect(my_window, 260, HEIGHT / 2 + 2, 5, 450, "white", False)
                draw_rect(my_window, 260, HEIGHT / 2 - 223 + 450 * (item_row_index / row_index2), 5, 45, "white")

            if (325 + row_index * (TILE + 35) < HEIGHT / 2 - 180) \
                    or (325 + row_index * (TILE + 35) > HEIGHT / 2 + 275):
                pass
            else:
                draw_rect(my_window, 275/2, 325 + row_index * (TILE + 35),
                          210, 40, "white")
                draw_text(my_window, sector,
                          275/2,
                          315 + row_index * (TILE + 35), 30, "black",
                          "DIN condensed")
            column_index = 0
            index = 0
            for item in sorted_inventory[sector]:

                if column_index % 3 == 0:
                    column_index = 0

                if index % row_index_max == 0:
                    row_index += 1
                    item_row_index += 1

                if (325 + row_index * (TILE + 35) < HEIGHT/2 - 180)\
                   or (325 + row_index * (TILE + 35) > HEIGHT/2 + 275):
                    continue

                item_image = item_data[item]["image_filename"]

                draw_image(my_window, item_image, 55 + column_index * (TILE + 35),
                           325 + row_index * (TILE + 35), img_dir,
                           True)

                draw_text(my_window, str(inventory[item]["count"]),
                          75 + column_index * (TILE + 35),
                          300 + row_index * (TILE + 35), 20, "red",
                          "DIN condensed")

                if inventory[item]["activated"] is True:
                    draw_rect(my_window, 60 + column_index * (TILE + 35),
                              320 + row_index * (TILE + 35), 60, 60, "blue", True)

                draw_rect(my_window, 60 + column_index * (TILE + 35),
                          320 + row_index * (TILE + 35), 60, 60, "white", False)

                if item == self.selected_inventory_item:
                    draw_image(my_window, item_image, 55 + column_index * (TILE + 35),
                               325 + row_index * (TILE + 35), img_dir,
                               True)
                    draw_text(my_window, str(inventory[item]["count"]),
                              75 + column_index * (TILE + 35),
                              300 + row_index * (TILE + 35), 20, "red",
                              "DIN condensed")
                    draw_image(my_window, "selection", 60 + column_index * (TILE + 35),
                               320 + row_index * (TILE + 35), img_dir, True)

                column_index += 1
                index += 1

            row_index += 1
            item_row_index += 1


        # draw_rect(my_window, 275 / 2, HEIGHT / 2 - 248, 275, 160, (40, 40, 40), True)
        draw_text(my_window, "INVENTORY", 275 / 2, HEIGHT / 2 - 265, 45, "white", "din condensed")
        draw_rect(my_window, 275/2, HEIGHT/2 - 220, 120, 2)

    # def draw_store(self):
    #     draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 275, visible_window_height * TILE, "white", True)
    #     draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 270, visible_window_height * TILE - 5, (40, 40, 40), True)
    #     draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 260, visible_window_height * TILE - 15, "white", True)
    #     draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 255, visible_window_height * TILE - 20, (40, 40, 40), True)
    #
    #     index = 0
    #
    #     if self.current_storage == "farm":
    #         storage = farm
    #     elif self.current_storage == "shop":
    #         storage = shop
    #     elif self.current_storage == "carpenter":
    #         storage = carpenter
    #     elif self.current_storage == "factory":
    #         storage = factory
    #
    #     for item in storage:
    #         image = item_data[item]["image_filename"]
    #
    #         draw_image(my_window, image, WIDTH - 275 / 2 - 5,
    #                    HEIGHT / 4 + 110 + index * (TILE + 35) + 5, img_dir, True)
    #
    #         draw_rect(my_window, WIDTH - 275 / 2,
    #                   350 + index * (TILE + 35), 60, 60, "white", False)
    #
    #         if item == self.selected_consumer_item:
    #             draw_image(my_window, "selection", WIDTH - 275 / 2,
    #                        350 + index * (TILE + 35), img_dir, True)
    #         index += 1
    #
    #     self.draw_prize_banner(self.selected_consumer_item)
    #
    #     draw_text(my_window, self.current_storage.upper(), WIDTH - 275 / 2, HEIGHT / 2 - 265, 45, "white", "din condensed")
    #     draw_rect(my_window, WIDTH - 275/2, HEIGHT/2 - 220, 120, 2)

    def draw_store(self):
        draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 275, visible_window_height * TILE, "white", True)
        draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 270, visible_window_height * TILE - 5, (40, 40, 40), True)
        draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 260, visible_window_height * TILE - 15, "white", True)
        draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 255, visible_window_height * TILE - 20, (40, 40, 40), True)

        row_index_max = 3

        row_index = -int(self.selected_consumer_item_index/3)

        column_index = 0
        index = 0

        if self.current_storage == "factory":
            list = factory
        elif self.current_storage == "farm":
            list = farm
        elif self.current_storage == "carpenter":
            list = carpenter
        elif self.current_storage == "shop":
            list = shop

        for item in list:
            if column_index % 3 == 0:
                column_index = 0

            if index % row_index_max == 0:
                row_index += 1

            if (265 + row_index * (TILE + 35) < HEIGHT / 2 - 180) \
                    or (267.5 + row_index * (TILE + 35) > HEIGHT / 2 + 275):
                continue

            item_image = item_data[item]["image_filename"]

            draw_image(my_window, item_image, WIDTH - 205 + column_index * (TILE + 35),
                       265 + row_index * (TILE + 35), img_dir,
                       True)

            draw_rect(my_window, WIDTH - 205 + column_index * (TILE + 35),
                      267.5 + row_index * (TILE + 35), 60, 60, "white", False)

            if item == self.selected_consumer_item:
                draw_image(my_window, item_image, WIDTH - 205 + column_index * (TILE + 35),
                           265 + row_index * (TILE + 35), img_dir,
                           True)
                draw_image(my_window, "selection", WIDTH - 205 + column_index * (TILE + 35),
                           267.5 + row_index * (TILE + 35), img_dir, True)
            column_index += 1
            index += 1

        draw_text(my_window, self.current_storage.upper(), WIDTH - 275 / 2, HEIGHT / 2 - 265, 45, "white", "din condensed")
        draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 - 220, 120, 2)

        self.draw_prize_banner(self.selected_consumer_item)

    def draw_bank(self):
        draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 275, visible_window_height * TILE, "white", True)
        draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 270, visible_window_height * TILE - 5, (40, 40, 40), True)
        draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 260, visible_window_height * TILE - 15, "white", True)
        draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 255, visible_window_height * TILE - 20, (40, 40, 40), True)

        draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 - 120, 175, 120, "white", True)
        draw_text(my_window, "Collect", WIDTH - 275 / 2, HEIGHT / 2 - 160, 30, "black", "dincondensed")
        draw_text(my_window, "Earned Money", WIDTH - 275 / 2, HEIGHT / 2 - 130, 30, "black", "dincondensed")
        draw_text(my_window, str(self.money_owed)+" $", WIDTH - 275 / 2, HEIGHT / 2 - 100, 30, "black", "dincondensed")

        draw_text(my_window, self.current_storage.upper(), WIDTH - 275 / 2, HEIGHT / 2 - 265, 45, "white",
                  "din condensed")
        draw_rect(my_window, WIDTH - 275/2, HEIGHT/2 - 220, 120, 2)

    def draw_well(self):
        draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 275, visible_window_height * TILE, "white", True)
        draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 270, visible_window_height * TILE - 5, (40, 40, 40), True)
        draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 260, visible_window_height * TILE - 15, "white", True)
        draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 + 2, 255, visible_window_height * TILE - 20, (40, 40, 40), True)

        draw_rect(my_window, WIDTH - 275 / 2, HEIGHT / 2 - 120, 175, 120, "white", True)
        draw_text(my_window, "Collect", WIDTH - 275 / 2, HEIGHT / 2 - 165, 30, "black", "dincondensed")
        draw_text(my_window, "Bucket of Water", WIDTH - 275 / 2, HEIGHT / 2 - 135, 30, "black", "dincondensed")
        draw_image(my_window, item_data["wateringcan"]["image_filename"], WIDTH - 275 / 2, HEIGHT / 2 - 85, img_dir, True)
        self.draw_prize_banner("wateringcan")

        draw_text(my_window, self.current_storage.upper(), WIDTH - 275 / 2, HEIGHT / 2 - 265, 45, "white",
                  "din condensed")
        draw_rect(my_window, WIDTH - 275/2, HEIGHT/2 - 220, 120, 2)

    def draw_information(self):
        self.draw_current_storage()
        self.draw_health()

    def draw_current_storage(self):
        draw_rect(my_window, WIDTH/2, 62, 1200, 124, (40, 40, 40), True)

        draw_rect(my_window, WIDTH/2 - 420, 80, 2, 50, "white", True)
        draw_rect(my_window, WIDTH/2 + 420, 80, 2, 50, "white", True)

        draw_text(my_window, "current storage", WIDTH/2, 40, 25, "white", "arial")
        draw_text(my_window, self.current_storage, WIDTH/2, 75, 40, "white", "din condensed")

        draw_text(my_window, "selected inventory item", WIDTH/2 - 250, 55, 15, "white", "arial")
        draw_text(my_window, self.selected_inventory_item, WIDTH/2 - 250, 80, 25, "white", "din condensed")

        draw_text(my_window, "selected consumer item", WIDTH/2 + 250, 55, 15, "white", "arial")
        draw_text(my_window, self.selected_consumer_item, WIDTH/2 + 250, 80, 25, "white", "din condensed")

    def draw_health(self):
        Organism.draw_health(self)

        draw_rect(my_window, 275/2, 50, 40, 150, (40, 40, 40), True)
        draw_circle(my_window, 117, 0, 124, (40, 40, 40), True)

        draw_text(my_window, "health bar", 180, 50, 14, "white", "Arial")

        draw_rect(my_window, 120, 85, 120, 25, "white", True, "left")

        if self.health > 70:
            health_bar_colour = "green"
        elif self.health > 40:
            health_bar_colour = "orange"
        else:
            health_bar_colour = "red"

        draw_rect(my_window, 
                  120, 85,
                  self.health*12/10, 25, health_bar_colour, True, "left")

        draw_text(my_window, str(self.health) + " %", 
                  180, 75,
                  18, "black", "arial", "center")

    def draw_exterior_storage(self):
        if self.in_building is False:
            return
        if self.current_storage in ["shop", "carpenter", "farm", "factory"]:
            self.draw_store()
        elif self.current_storage == "bank":
            self.draw_bank()
        elif self.current_storage == "well":
            self.draw_well()

    def compute_item_cost(self, item):
        expenses = []
        expense = item_data[item]["cost"]
        for currency in expense:
            prize, unit = currency.split(" ")
            expenses.append([prize, unit])
        return expenses
    
    def draw_prize_banner(self, item):
        banner_y = 230

        width_formula = 0
        height_formula = 0
        for expense in self.compute_item_cost(item):
            width_formula += text_to_surface(expense[0], 25).get_size()[0] + 10 + image_to_surface(expense[1], img_dir, True).get_size()[0]/2 + 40
            if image_to_surface(expense[1], img_dir, True).get_size()[1] > height_formula:
                height_formula = image_to_surface(expense[1], img_dir, True).get_size()[1]
        height_formula += 30
        width_formula -= 40
        if width_formula + height_formula < text_to_surface(item, 25).get_size()[0]:
            width_formula = text_to_surface(item, 25).get_size()[0] + 40

        banner_surface = pygame.Surface((width_formula + height_formula, height_formula))
        banner_width, banner_height = banner_surface.get_size()

        draw_rect(banner_surface, banner_width/2, banner_height/2, width_formula, height_formula)
        draw_circle(banner_surface, height_formula/2, banner_height/2, height_formula/2)
        draw_circle(banner_surface, banner_width - height_formula/2, banner_height/2, height_formula/2)

        width_index = 0

        for expense in self.compute_item_cost(item):
            
            text_to_image(expense[0], trash_dir, 25, "black", "dincondensed")
            text_PIXAR = image_to_PIXAR_surface(expense[0], trash_dir, (True, "white"))
            text_height = text_PIXAR.get_size()[1]
            width_index += text_PIXAR.get_size()[0]/2
            draw_surface(banner_surface, text_PIXAR, banner_width/2 - width_formula/2 + width_index, banner_height/2 + 2*text_height/3)

            # draw_text(banner_surface, expense[0], banner_width/2 - width_formula/2 + width_index, banner_height/2, 25, "black", "dincondensed")

            image_PIXAR = image_to_PIXAR_surface(expense[1], img_dir, (True, "white"))
            image_height = image_PIXAR.get_size()[1]
            width_index += 10 + image_PIXAR.get_size()[0]/2
            draw_surface(banner_surface, image_PIXAR, banner_width/2 - width_formula/2 + width_index, banner_height/2 + image_height/3)

            
            # draw_image(banner_surface, expense[1], banner_width/2 - width_formula/2 + width_index, banner_height/2, img_dir, True)
            width_index += 30
        
        text_to_image(item, trash_dir, 20, "black", "arial")
        text_PIXAR2 = image_to_PIXAR_surface(item, trash_dir, (True, "white"))
        draw_surface(banner_surface, text_PIXAR2, banner_width/2, banner_height/2 - 15)

        surface_to_image(banner_surface, "hi", trash_dir)

        new_surface = pygame.Surface((banner_width, banner_height))

        for x in range(0, int(banner_width)):
            for y in range(0, int(banner_height)):
                new_surface.set_at([x, y], banner_surface.get_at([x, y]))

        new_surface.set_alpha(self.notification_visibility*(255/100))

        draw_surface(my_window, new_surface, WIDTH/2, banner_y)

    def controls(self):
        keys_down = pygame.key.get_pressed()

        if self.axe_hits == 0:
            inventory[self.selected_inventory_item]["activated"] = False

        if self.shovel_hits == 0:
            inventory[self.selected_inventory_item]["activated"] = False

        if self.frame != 0:
            return

        if keys_down[K_UP] and self.y > 0:
            self.direction = "up"

            if scenery_map[self.y - 1][self.x].race != "":
                if self.axe_hits > 0:
                    scenery_map[self.y - 1][self.x].race = ""
                    self.axe_hits -= 1
                    inventory["log"]["count"] += 1

                    earn_fruit = random.choice(["no", "no", "yes"])
                    earn_stone = random.choice(["no", "no", "yes"])
                    earn_log = random.choice(["no", "no", "no", "yes"])
                    earn_coin = random.choice(["no", "no", "no", "no", "yes"])

                    if earn_fruit == "yes":
                        inventory[random.choice(["pear", "cherry", "cherry"])]["count"] += 1
                    if earn_stone == "yes":
                        inventory[random.choice(["grass", "grass", "stone", "dirt", "dirt", "dirt", "ground"])]["count"] += 1
                    if earn_log == "yes":
                        inventory["log"]["count"] += 1
                    if earn_coin == "yes":
                        inventory["coin"]["count"] += 1

                else:
                    return

            if block_map[self.y][self.x].race == "water":
                return

            self.y -= 1
            self.frame = 1
            if self.in_building is True:
                self.in_building = False
                self.current_storage = "inventory"

        elif keys_down[K_DOWN] and self.y < map_height - 2:
            self.direction = "down"

            if scenery_map[self.y + 1][self.x].race != "":
                if self.axe_hits > 0:
                    scenery_map[self.y + 1][self.x].race = ""
                    self.axe_hits -= 1
                    inventory["log"]["count"] += 1

                    earn_fruit = random.choice(["no", "no", "yes"])
                    earn_stone = random.choice(["no", "no", "yes"])
                    earn_log = random.choice(["no", "no", "no", "yes"])
                    earn_coin = random.choice(["no", "no", "no", "no", "yes"])

                    if earn_fruit == "yes":
                        inventory[random.choice(["pear", "cherry", "cherry"])]["count"] += 1
                    if earn_stone == "yes":
                        inventory[random.choice(["grass", "grass", "stone", "dirt", "dirt", "dirt", "ground"])]["count"] += 1
                    if earn_log == "yes":
                        inventory["log"]["count"] += 1
                    if earn_coin == "yes":
                        inventory["coin"]["count"] += 1

                else:
                    return

            if block_map[self.y + 2][self.x].race == "water":
                return
                    
            self.y += 1
            self.frame = 1
            
            if self.in_building is True:
                self.in_building = False
                self.current_storage = "inventory"

        elif keys_down[K_RIGHT] and self.x < map_width - 1:
            self.direction = "right"
            
            if scenery_map[self.y][self.x + 1].race != "":
                if self.axe_hits > 0:
                    scenery_map[self.y][self.x + 1].race = ""
                    self.axe_hits -= 1
                    inventory["log"]["count"] += 1

                    earn_fruit = random.choice(["no", "no", "yes"])
                    earn_stone = random.choice(["no", "no", "yes"])
                    earn_log = random.choice(["no", "no", "no", "yes"])
                    earn_coin = random.choice(["no", "no", "no", "no", "yes"])

                    if earn_fruit == "yes":
                        inventory[random.choice(["pear", "cherry", "cherry"])]["count"] += 1
                    if earn_stone == "yes":
                        inventory[random.choice(["grass", "grass", "stone", "dirt", "dirt", "dirt", "ground"])]["count"] += 1
                    if earn_log == "yes":
                        inventory["log"]["count"] += 1
                    if earn_coin == "yes":
                        inventory["coin"]["count"] += 1

                else:
                    return

            if block_map[self.y + 1][self.x + 1].race == "water":
                return

            self.x += 1
            self.frame = 1

            if self.in_building is True:
                self.in_building = False
                self.current_storage = "inventory"

        elif keys_down[K_LEFT] and self.x > 0:
            self.direction = "left"
            
            if scenery_map[self.y][self.x - 1].race != "":
                if self.axe_hits > 0:
                    scenery_map[self.y][self.x - 1].race = ""
                    self.axe_hits -= 1
                    inventory["log"]["count"] += 1

                    earn_fruit = random.choice(["no", "no", "yes"])
                    earn_stone = random.choice(["no", "no", "yes"])
                    earn_log = random.choice(["no", "no", "no", "yes"])
                    earn_coin = random.choice(["no", "no", "no", "no", "yes"])

                    if earn_fruit == "yes":
                        inventory[random.choice(["pear", "cherry", "cherry"])]["count"] += 1
                    if earn_stone == "yes":
                        inventory[random.choice(["grass", "grass", "stone", "dirt", "dirt", "dirt", "ground"])]["count"] += 1
                    if earn_log == "yes":
                        inventory["log"]["count"] += 1
                    if earn_coin == "yes":
                        inventory["coin"]["count"] += 1
                else:
                    return

            if block_map[self.y + 1][self.x - 1].race == "water":
                return

            self.x -= 1
            self.frame = 1    

            if self.in_building is True:
                self.in_building = False
                self.current_storage = "inventory"
        
        if keys_down[K_RETURN]:
            if self.current_storage == "inventory":
                if self.selected_inventory_item in images["Object"]:
                    if item_data[self.selected_inventory_item]["race"] == "FOOD" \
                    and self.health < 100 \
                    and inventory[self.selected_inventory_item]["count"] > 0:
                        inventory[self.selected_inventory_item]["count"] -=1
                        self.health += 10

                    if self.selected_inventory_item == "axe" \
                        and self.axe_hits == 0 \
                        and inventory[self.selected_inventory_item]["count"] > 0:
                        inventory[self.selected_inventory_item]["count"] -= 1
                        self.axe_hits = 3
                        inventory[self.selected_inventory_item]["activated"] = True

                    elif self.selected_inventory_item == "shovel" \
                        and self.shovel_hits == 0 \
                        and inventory[self.selected_inventory_item]["count"] > 0 \
                        and block_map[self.y + 1][self.x].race in ["grass", "dirt", "stone"]:
                        inventory[self.selected_inventory_item]["count"] -= 1
                        inventory[block_map[self.y + 1][self.x].race]["count"] += 1
                        if block_map[self.y + 1][self.x].race == "grass":
                            block_map[self.y + 1][self.x] = Block("dirt", self.x, self.y + 1)
                        elif block_map[self.y + 1][self.x].race == "dirt":
                            block_map[self.y + 1][self.x] = Block("stone", self.x, self.y + 1)
                        elif block_map[self.y + 1][self.x].race == "stone":
                            block_map[self.y + 1][self.x] = Block("ground", self.x, self.y + 1)

            elif self.current_storage in ["shop", "carpenter", "farm", "well", "factory"]:
                not_enough_money = False
                for expense in self.compute_item_cost(self.selected_consumer_item):
                    if not_enough_money:
                        continue
                    currency, quantity = expense[1], int(expense[0])
                    if inventory[currency]["count"] < quantity:
                        not_enough_money = True
                if not_enough_money is False:
                    for expense in self.compute_item_cost(self.selected_consumer_item):
                        currency, quantity = expense[1], int(expense[0])
                        inventory[currency]["count"] -= quantity
                    inventory[self.selected_consumer_item]["count"] += 1
                    self.selected_inventory_item = self.selected_consumer_item

            elif self.current_storage == "bank":
                inventory[self.currency]["count"] += self.money_owed
                self.money_owed = 0

        if keys_down[K_TAB]:
            self.current_storage = "inventory"
            self.selected_inventory_item_index += 1
            if self.selected_inventory_item_index > len(inventory) - 1:
                self.selected_inventory_item_index = 0  
            self.selected_inventory_item = inventory_indexes[self.selected_inventory_item_index]
            pygame.time.delay(50)

        if keys_down[K_BACKSPACE] and self.in_building is True:
            self.selected_consumer_item_index += 1
            list = None
            indexes = None
            if self.current_storage == "shop":
                list = shop
                indexes = shop_indexes
            elif self.current_storage == "carpenter":
                list = carpenter
                indexes = carpenter_indexes
            elif self.current_storage == "farm":
                list = farm
                indexes = farm_indexes
            elif self.current_storage == "well":
                list = well
                indexes = well_indexes
            elif self.current_storage == "factory":
                list = factory
                indexes = factory_indexes
            if self.selected_consumer_item_index > len(list) - 1:
                self.selected_consumer_item_index = 0  
            self.selected_consumer_item = indexes[self.selected_consumer_item_index]
        
        if keys_down[K_SPACE]:
            if animal_map[self.y][self.x].race != "":
                self.selected_inventory_item = animal_map[self.y][self.x].race
                index = 0
                for item in inventory:
                    if item == self.selected_inventory_item:
                        self.selected_inventory_item_index = index
                    index += 1
                inventory[self.selected_inventory_item]["count"] += 1
                animal_map[self.y][self.x] = Blank(self.x, self.y)

            if object_map[self.y][self.x].race != "":
                self.selected_inventory_item = object_map[self.y][self.x].race
                index = 0
                for item in inventory:
                    if item == self.selected_inventory_item:
                        self.selected_inventory_item_index = index
                    index += 1
                inventory[self.selected_inventory_item]["count"] += 1
                object_map[self.y][self.x] = Blank(self.x, self.y)
                if self.health < 40 and self.selected_inventory_item in ["pear", "meat", "cherry"]:
                    self.health += 10
                    inventory[self.selected_inventory_item]["count"] -= 1

            if building_map[self.y][self.x].race != "":
                self.in_building = True
                self.current_storage = building_map[self.y][self.x].race

                if self.current_storage in ["farm", "shop", "carpenter", "well", "factory"]:
                    self.selected_consumer_item_index = 0
                    if self.current_storage == "farm":
                        storage = farm
                    elif self.current_storage == "shop":
                        storage = shop
                    elif self.current_storage == "carpenter":
                        storage = carpenter
                    elif self.current_storage == "well":
                        storage = well
                    elif self.current_storage == "factory":
                        storage = factory
                    self.selected_consumer_item = find_item(self.selected_consumer_item_index, storage)

        if keys_down[K_BACKSLASH]:
            if inventory[self.selected_inventory_item]["count"] > 0 \
               and animal_map[player.y][player.x].race == "" \
               and object_map[player.y][player.x].race == "":
                if self.selected_inventory_item in images["Animal"]:
                    animal_map[self.y][self.x] = NAnimal(self.selected_inventory_item, self.x, self.y)
                    inventory[self.selected_inventory_item]["count"] -= 1
                elif self.selected_inventory_item in images["Object"]:
                    object_map[self.y][self.x] = Object(self.selected_inventory_item, self.x, self.y)
                    inventory[self.selected_inventory_item]["count"] -= 1
                elif self.selected_inventory_item in images["Block"]:
                    inventory[block_map[self.y][self.x].race]["count"] += 1
                    block_map[self.y][self.x] = Block(self.selected_inventory_item, self.x, self.y)
                    inventory[self.selected_inventory_item]["count"] -= 1

        if keys_down[K_ESCAPE]:
            pygame.quit()
            quit()

    def update(self):
        if Organism.update(self) is False:
            return

        self.controls()
        if self.frame != 0:
            self.frame += 1
            if self.frame == 4:
                self.frame = 0
        self.image_filename = images["Player"][self.style][self.direction] + str(self.frame)

class NAnimal(Organism):

    """NAnimal is the class for all nice animals, 
    which consists of chicks, goats, and sheep.
    These animals just try to live out their lives:
    walking around, eating fruits they come upon,
    reproducing, and not purposefully trying to get 
    in the way of your farm."""
    
    def __init__(self, race, x, y):
        super().__init__(race, x, y)
        self.clock = pygame.time.Clock()
        self.reproduction_timer = 0
        self.image_filename = images["Animal"][self.race][self.direction]
    
    def update(self):
        if self.health <= 0:
            animal_map[self.y][self.x] = Blank(self.x, self.y)
            return False

        time_passed_milliseconds = self.clock.tick()
        time_passed_seconds = time_passed_milliseconds / 1000
        self.motion_timer += time_passed_seconds
        self.health_timer += time_passed_seconds

        if self.motion_timer < self.motion_max:
            return False
        else:
            self.motion_timer = 0

        paths = [(self.x, self.y), (self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1),
                    (self.x, self.y + 1)]
        possible_paths = []
        for path in paths:
            if (1 <= path[0] <= map_width - 2) and (1 <= path[1] <= map_height - 2):
                if (object_map[path[1]][path[0]].race in ["", "pear", "cherry"]) \
                        and (block_map[path[1]][path[0]].race != "water") \
                        and (scenery_map[path[1] + 1][path[0]].race == "") \
                        and (animal_map[path[1]][path[0]].race == "") \
                        and (building_map[path[1]][path[0]].race == "") \
                        and ((path[0] == player.x and path[1] == player.y + 1) is False):
                    possible_paths.append(path)

        if len(possible_paths) > 0:
            path_take = random.choice(possible_paths)
            animal = NAnimal(self.race, path_take[0], path_take[1])
            animal_map[self.y][self.x] = Blank(self.x, self.y)
            animal_map[path_take[1]][path_take[0]] = animal

            if path_take[0] - self.x > 0:
                animal.direction = "right"
            elif path_take[0] - self.x < 0:
                animal.direction = "left"
            elif path_take[1] - self.y > 0:
                animal.direction = "down"
            elif path_take[1] - self.y < 0:
                animal.direction = "up"
            else:
                animal.direction = "down"
            
            animal.image_filename = images["Animal"][animal.race][animal.direction]
            
            animal.reproduction_timer = self.reproduction_timer
            animal.health = self.health
            animal.health_timer = self.health_timer

            if block_map[animal.y][animal.x].race != "grass":
                animal.health -= 25

            if object_map[animal.y][animal.x].race in ["pear", "cherry"]:
                animal.reproduction_timer += 1
                object_map[animal.y][animal.x] = Blank(animal.x, animal.y)

                if animal.reproduction_timer >= 3:
                    animal.health -= 25

                    possible_positions = [(animal.x - 1, animal.y - 1), (animal.x, animal.y - 1),
                                            (animal.x + 1, animal.y - 1),
                                            (animal.x - 1, animal.y), (animal.x + 1, animal.y),
                                            (animal.x - 1, animal.y + 1), (animal.x, animal.y + 1),
                                            (animal.x + 1, animal.y + 1)]

                    new_possible_positions = []
                    for position in possible_positions:
                        if (1 <= position[0] <= map_width - 2) and (1 <= position[1] <= map_height - 2):
                            if (object_map[position[1]][position[0]].race == "") \
                                    and (scenery_map[position[1] + 1][position[0]].race == "") \
                                    and (animal_map[position[1]][position[0]].race == "") \
                                    and (building_map[position[1]][position[0]].race == "") \
                                    and ((position[0] == player.x and position[1] == player.y + 1) is False):
                                new_possible_positions.append(position)

                    if len(new_possible_positions) > 0:
                        position = random.choice(new_possible_positions)
                        animal2 = NAnimal(self.race, position[0], position[1])
                        animal_map[position[1]][position[0]] = animal2

                    animal.reproduction_timer = 0

class BAnimal(Organism):

    """BAnimal is the class for all bad animals,
    which is composed of moles, rabbits, and snails.
    These animals live as kings and queens, taking
    what they want, destroying everything in their way,
    and may even attempt to harm other animals. Their 
    mission is to make the farm a graveyard. Beware."""

    def __init__(self, race, x, y):
        super().__init__(race, x, y)
        self.reproduction_timer = 0

        self.image_filename = images["Animal"][self.race][self.direction]
        
    def update(self):
        if Organism.update(self) is False:
            return

        paths = [(self.x, self.y), (self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y - 1),
                 (self.x, self.y + 1)]
        possible_paths = []
        for path in paths:
            if (1 <= path[0] <= map_width - 2) and (1 <= path[1] <= map_height - 2):
                if (object_map[path[1]][path[0]].race in ["", "pear", "cherry"]) \
                        and (block_map[path[1]][path[0]].race != "water") \
                        and (scenery_map[path[1] + 1][path[0]].race == "") \
                        and (animal_map[path[1]][path[0]].race == "") \
                        and (building_map[path[1]][path[0]].race == "") \
                        and ((path[0] == player.x and path[1] == player.y + 1) is False):
                    possible_paths.append(path)

        if len(possible_paths) > 0:
            path_take = random.choice(possible_paths)
            animal = BAnimal(self.race, path_take[0], path_take[1])
            animal_map[self.y][self.x] = Blank(self.x, self.y)
            animal_map[animal.y][animal.x] = animal

            if path_take[0] - self.x > 0:
                animal.direction = "right"
            elif path_take[0] - self.x < 0:
                animal.direction = "left"
            elif path_take[1] - self.y > 0:
                animal.direction = "down"
            elif path_take[1] - self.y < 0:
                animal.direction = "up"
            else:
                animal.direction = "down"

            animal.image_filename = images["Animal"][animal.race][animal.direction]

            animal.reproduction_timer = self.reproduction_timer
            animal.health = self.health
            animal.health_timer = self.health_timer

            ruin_ground = random.choice(["no", "no", "no", "no", "no", "no", "no", "yes"])
            if ruin_ground == "yes":
                if block_map[animal.y][animal.x].race == "grass":
                    block_map[animal.y][animal.x] = Block("dirt", animal.x, animal.y)
                elif block_map[animal.y][animal.x].race == "dirt":
                    block_map[animal.y][animal.x] = Block("stone", animal.x, animal.y)
                elif block_map[animal.y][animal.x].race == "stone":
                    block_map[animal.y][animal.x] = Block("ground", animal.x, animal.y)
                else:
                    block_map[animal.y][animal.x] = Block("water", animal.x, animal.y)

class Building(Sprite):
    def __init__(self, race, x, y):        
        super().__init__(race, x, y)

        self.image_filename = images["Building"][self.race]

class Block(Sprite):
    def __init__(self, race, x, y):        
        super().__init__(race, x, y)

        self.image_filename = images["Block"][self.race]

class Scenery(Sprite):
    def __init__(self, race, x, y):        
        super().__init__(race, x, y)

        self.image_filename = images["Scenery"][self.race]

class Object(Sprite):

    """Object is the parent class for all objects,
    which consist of axes, nuts, fruits, fences, shells, etc."""

    def __init__(self, race, x, y):        
        super().__init__(race, x, y)

        if self.race != "":
            self.image_filename = images["Object"][self.race]

class Nut(Object):

    """The nut is a unique object in the game: it can
    transform into another object, more speciffically a
    tree. Hence, it has its own class, the Nut."""

    def __init__(self, x, y):
        super().__init__("nut", x, y)
        self.water = 0

    def update(self):
        pass

class Blank(Object):

    """The class Blank is used as a space_holder.
    For example if there isn't an Object on a particular coordinate, 
    we assign that coordinate a Blank Object, so that it is not empty
    and will not crash the program."""

    def __init__(self, x, y):
        super().__init__("", x, y)
    
    def render(self):
        pass


main_dir = "/Users/czeslawtracz/Library/Mobile Documents/com~apple~CloudDocs/MasterClass/MacroFarm/"
img_dir = "/Users/czeslawtracz/Library/Mobile Documents/com~apple~CloudDocs/MasterClass/MacroFarm/images/"
trash_dir = "/Users/czeslawtracz/Library/Mobile Documents/com~apple~CloudDocs/MasterClass/MacroFarm/trash/"
sound_dir = "/Users/czeslawtracz/Library/Mobile Documents/com~apple~CloudDocs/MasterClass/MacroFarm/sounds/"

map_width = 20
map_height = 20

TILE = 40

player = Player(int(map_width/2), int(map_height/2))

visible_window_width = 21

visible_window_height = 15

mid_x_coord = (WIDTH - (visible_window_width + 1)*TILE)/2
mid_y_coord = -(HEIGHT - (visible_window_height + 1)*TILE)/2

block_map = []
for row in range(0, map_height):
    block_map.append([])
    for column in range(0, map_width):
        random_num = random.randint(0, 50)
        if random_num > 6:
            block_map[len(block_map) - 1].append(Block("grass", column, row))
        elif random_num > 2:
            block_map[len(block_map) - 1].append(Block("dirt", column, row))
        else:
            block_map[len(block_map) - 1].append(Block("stone", column, row))

scenery_map = []
for row in range(0, map_height):
    scenery_map.append([])
    for column in range(0, map_width):
        random_num = random.randint(0, 50)
        if random_num < 6:
            scenery_map[len(scenery_map) - 1].append(Scenery(random.choice(["norm_tree", "norm_tree", "norm_tree", "norm_tree", "norm_tree",
                                                                             "cherry_tree"]), column, row))
        else:
            scenery_map[len(scenery_map) - 1].append(Blank(column, row))

animal_map = []
for row in range(0, map_height):
    animal_map.append([])
    for column in range(0, map_width):
        if scenery_map[row][column].race != "":
            animal_map[len(animal_map) - 1].append(Blank(column, row))
            continue
        random_num = random.randint(0, 50)
        if random_num <= 1:
            random_num2 = random.randint(0, 12)
            if random_num2 <= 1:
                animal_map[len(animal_map) - 1].append(BAnimal("snail", column, row))
            else:
                animal_map[len(animal_map) - 1].append(NAnimal(random.choice(["chick", "chick", "chick", "chick",
                                                                              "sheep", "sheep", "sheep",
                                                                              "goat", "goat", "goat",
                                                                              "pig", "pig"]),
                                                            column, row))
        else:
            animal_map[len(animal_map) - 1].append(Blank(column, row))

object_map = []
for row in range(0, map_height):
    object_map.append([])
    for column in range(0, map_width):
        if animal_map[row][column].race != "" \
            or scenery_map[row][column].race != "":
            object_map[len(object_map) - 1].append(Blank(column, row))
            continue

        random_num = random.randint(0, 50)
        if random_num <= 1:
            object_map[len(object_map) - 1].append(Object(random.choice(["axe", "axe", "axe", "axe",
                                                                         "shovel", "shovel", "shovel", "shovel",
                                                                         "coin", "coin",
                                                                         "fence",
                                                                         "log", "log", "log", "log",
                                                                         "nut", "nut", "nut",
                                                                         "pear", "pear", "pear", "pear",
                                                                         "shell", "shell",
                                                                         "cherry", "cherry", "cherry",
                                                                         "carrot", "carrot", "carrot",
                                                                         "broccoli", "broccoli",
                                                                         "wateringcan", "wateringcan"]),
                                                        column, row))
        else:
            object_map[len(object_map) - 1].append(Blank(column, row))

building_map = []
list = ["well", "well", "well", "well", "bank", "farm", "shop", "carpenter", "factory"]
for row in range(0, map_height):
    building_map.append([])
    for column in range(0, map_width):
        building_map[len(building_map) - 1].append(Blank(column, row))
for building in list:
    y, x = random.randint(0, map_height - 1), random.randint(0, map_width - 1)
    while animal_map[y][x].race != "" \
       or scenery_map[y][x].race != "" \
       or object_map[y][x].race != "":
        y, x = random.randint(0, map_height - 1), random.randint(0, map_width - 1)
    building_map[y][x] = Building(building, x, y)

while True:
    my_window.fill("black")

    for event in pygame.event.get():
        pass

    if player.health <= 0:
        pygame.quit()
        quit()

    for row in animal_map:
        for animal in row:
            animal.update()
    player.update()
    
    visible_width_index = player.x
    visible_height_index = player.y + 1
    
    for y in range(1, visible_window_height + 1):
        for x in range(1, visible_window_width + 1):
            draw_image(my_window, images["Block"]["water"],
                      (x*TILE + mid_x_coord),
                      (y*TILE - mid_y_coord),
                      img_dir, True)
            pass

    for row in range(int(visible_height_index - (visible_window_height + 1)/2), int(visible_height_index + (visible_window_height + 1)/2)):
        for column in range(int(visible_width_index - (visible_window_width + 1)/2), int(visible_width_index + (visible_window_width + 1)/2)):
            if 0 <= row <= map_height - 1 and 0 <= column <= map_width - 1:
                block_map[row][column].render()
                
    for row in range(int(visible_height_index - (visible_window_height + 1)/2), int(visible_height_index + (visible_window_height + 1)/2)):
        for column in range(int(visible_width_index - (visible_window_width + 1)/2), int(visible_width_index + (visible_window_width + 1)/2)):
            if 0 <= row <= map_height - 1 and 0 <= column <= map_width - 1:
                building_map[row][column].render()
                animal_map[row][column].render()
                object_map[row][column].render()
                if player.x == column and player.y == row:
                    player.render()
                scenery_map[row][column].render()

    draw_rect(my_window, WIDTH/2, (TILE/2-mid_y_coord)/2, WIDTH, TILE/2-mid_y_coord, "black")
    draw_rect(my_window, WIDTH/2, HEIGHT + mid_y_coord/2 - TILE/4, WIDTH, TILE/2-mid_y_coord, "black")
    draw_rect(my_window, mid_x_coord/2, HEIGHT/2, mid_x_coord + TILE, HEIGHT, "black")
    draw_rect(my_window, WIDTH - mid_x_coord/2, HEIGHT/2, mid_x_coord + TILE, HEIGHT, "black")

    player.draw_inventory()
    player.draw_information()
    player.draw_exterior_storage()

    draw_rect(my_window, WIDTH - 275 / 2, 50, 40, 150, (40, 40, 40), True)
    draw_circle(my_window, WIDTH - 155, 0, 124, (40, 40, 40), True)
    draw_circle(my_window, WIDTH - 117, 0, 124, (40, 40, 40), True)

    time_passed_milliseconds = clock.tick()
    time_passed_seconds = time_passed_milliseconds/(10**3)
    if timer["seconds"] < time_passed_seconds:
        if timer["minutes"] == 0:
            time_up = True
        timer["minutes"] -= 1
        timer["seconds"] += 60
    timer["seconds"] -= time_passed_seconds

    minutes = str(timer['minutes'])
    if len(minutes) < 2:
        minutes = "0" + minutes
    seconds = str(round(timer['seconds']))
    if len(seconds) < 2:
        seconds = "0" + seconds

    draw_text(my_window, "timer", WIDTH - 275/2, 45, 20)
    draw_text(my_window, f"{minutes}:{seconds}", WIDTH - 275/2, 70, 35)

    if time_up:
        pygame.quit()
        quit()
        break

    pygame.display.update()