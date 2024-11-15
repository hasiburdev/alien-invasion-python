class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.title = "Alien Invasion"
        self.frame_rate = 60

        # Ship settings
        self.ship_limit = 3
        self.ship_speed = 1.5

        # Bullet setting
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Alien settings
        self.alien_speed = 40.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
