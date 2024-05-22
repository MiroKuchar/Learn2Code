import random
import time

class Fighter:
    def __init__(self, name, hp, dmg, hit_timer, hit_rating, dodge_rating, critical_chance):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.dmg = dmg
        self.hit_timer = hit_timer
        self.hit_rating = hit_rating
        self.dodge_rating = dodge_rating
        self.critical_chance = critical_chance
        self.last_hit_time = 0

    def check_critical_hit(self):
        critical_roll = random.randint(1, 10)
        return critical_roll <= self.critical_chance

    def is_alive(self):
        return self.hp > 0

    def attack(self, opponent):
        current_time = time.time()
        if current_time - self.last_hit_time >= self.hit_timer:
            self.last_hit_time = current_time
            critical_hit = self.check_critical_hit()
            if random.random() <= self.hit_rating:
                if random.random() > opponent.dodge_rating:
                    dice_roll = random.randint(1, self.dmg // 2)  # Adjust dice roll range
                    base_damage = self.dmg + dice_roll
                    if critical_hit:
                        return min(base_damage * 2, opponent.hp), critical_hit
                    else:
                        return min(base_damage, opponent.hp), critical_hit
                else:
                    return 0, False  # Return 0 damage if the attack is dodged
            else:
                return 0, False  # Return 0 damage if the attack misses
        else:
            return 0, False  # Return 0 damage if hit timer hasn't elapsed
