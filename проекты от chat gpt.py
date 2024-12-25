import arcade
import random

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Избегай падающие объекты"

# Игрок
player_width = 50
player_height = 50
player_speed = 5

# Падающие объекты
falling_object_width = 50
falling_object_height = 50
falling_object_speed = 5

# Счет
score = 0

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Инициализация переменных
        self.player = arcade.SpriteSolidColor(player_width, player_height, arcade.color.BLUE)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = 50

        self.falling_objects = arcade.SpriteList()

        self.score = 0
        self.game_over = False

    def on_draw(self):
        arcade.start_render()

        # Отображаем игрока
        self.player.draw()

        # Отображаем падающие объекты
        self.falling_objects.draw()

        # Отображаем счет
        arcade.draw_text(f"Счет: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.BLACK, 20)

        # Если игра окончена
        if self.game_over:
            arcade.draw_text("Игра окончена", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, arcade.color.RED, 30)

    def on_update(self, delta_time):
        global score

        if self.game_over:
            return

        # Двигаем падающие объекты
        self.falling_objects.update()

        # Проверка на столкновение с объектами
        hit_list = arcade.check_for_collision_with_list(self.player, self.falling_objects)
        if hit_list:
            self.game_over = True
            return

        # Увеличиваем счет за каждое падающее препятствие, которое не столкнулось
        for obj in self.falling_objects:
            if obj.bottom < 0:
                self.falling_objects.remove(obj)
                self.score += 1

        # Появление новых падающих объектов
        if random.random() < 0.02:  # 2% шанс на создание объекта
            self.create_falling_object()

    def on_key_press(self, key, modifiers):
        # Управление игроком
        if key == arcade.key.LEFT and self.player.center_x > player_width // 2:
            self.player.center_x -= player_speed
        elif key == arcade.key.RIGHT and self.player.center_x < SCREEN_WIDTH - player_width // 2:
            self.player.center_x += player_speed

    def create_falling_object(self):
        # Создаем падающий объект
        falling_object = arcade.SpriteSolidColor(falling_object_width, falling_object_height, arcade.color.RED)
        falling_object.center_x = random.randint(falling_object_width // 2, SCREEN_WIDTH - falling_object_width // 2)
        falling_object.center_y = SCREEN_HEIGHT + falling_object_height // 2
        falling_object.change_y = -falling_object_speed  # Двигается вниз
        self.falling_objects.append(falling_object)

def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()

