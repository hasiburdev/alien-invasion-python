import sys
import pygame
from alien import Alien
from bullet import Bullet
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        # currentRez = (pygame.display.Info().current_w, pygame.display.Info().current_h)

        # self.screen = pygame.display.set_mode(currentRez, pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.clock = pygame.time.Clock()

        pygame.display.set_caption(self.settings.title)

    def _create_fleet(self):
        alien = Alien(self)

        alien_width, alien_height = alien.rect.size
        ship_height = self.ship.rect.height

        available_space_x = self.settings.screen_width - (2 * alien_width)
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_of_aliens_x = available_space_x // (2 * alien_width)
        number_of_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_of_rows):
            for alien_number in range(number_of_aliens_x):
                self.create_alien(alien_number, row_number)

    def create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x

        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

        self.aliens.add(alien)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_f:
            pygame.display.toggle_fullscreen()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def check_event(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            bullet.draw_bullet()

    def update_aliens(self):
        self.check_fleet_edges()
        self.aliens.update()

    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        self.update_bullets()
        self.update_aliens()

        self.aliens.draw(self.screen)

        pygame.display.flip()

    def run_game(self):
        while True:
            self.check_event()

            self.ship.update()

            self.update_screen()

            self.clock.tick(self.settings.frame_rate)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()