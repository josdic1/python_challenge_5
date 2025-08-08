import sqlite3
from lib.character import Character
from lib.fighting_style import FightingStyle
from lib.special_move import SpecialMove
from lib.combo import Combo

CONN = sqlite3.connect('database.db')
CURSOR = CONN.cursor()

with open('schema.sql', 'r') as f:
    CURSOR.executescript(f.read())

CONN.commit()
CONN.close()

ryu = Character.add_new("Ryu", "Japan")
ken = Character.add_new("Ken", "USA")
chun_li = Character.add_new("Chun-Li", "China")
e_honda = Character.add_new("E. Honda", "Japan")
blanka = Character.add_new("Blanka", "Brazil")
zangief = Character.add_new("Zangief", "Soviet Union")
guile = Character.add_new("Guile", "USA")
dhalsim = Character.add_new("Dhalsim", "India")
balrog = Character.add_new("Balrog", "USA")
vega = Character.add_new("Vega", "Spain")
sagat = Character.add_new("Sagat", "Thailand")
m_bison = Character.add_new("M. Bison", "Shadaloo")

shotokan_karate = FightingStyle.add_new("Shotokan Karate")
kung_fu = FightingStyle.add_new("Kung Fu")
sumo_wrestling = FightingStyle.add_new("Sumo Wrestling")
capoeira = FightingStyle.add_new("Capoeira")
sambo = FightingStyle.add_new("Sambo")
military_fighting = FightingStyle.add_new("Military Fighting")
yoga = FightingStyle.add_new("Yoga")
boxing = FightingStyle.add_new("Boxing")
ninjutsu = FightingStyle.add_new("Ninjutsu")
muay_thai = FightingStyle.add_new("Muay Thai")
psycho_power = FightingStyle.add_new("Psycho Power")

qcf_p = Combo.add_new("QCF + P")   # Quarter-circle Forward + Punch
dp_p = Combo.add_new("DP + P")    # Dragon Punch motion + Punch
qcb_k = Combo.add_new("QCB + K")   # Quarter-circle Back + Kick
hold_b_f_p = Combo.add_new("Hold B, F + P") # Hold back, then forward + Punch
hold_d_u_k = Combo.add_new("Hold D, U + K")  # Hold down, then up + Kick

# Ryu (character_id: 1), Combos (combo_id: 1-3)
hadoken_ryu = SpecialMove.add_new("Hadoken", "PUNCH", 1, 1)
shoryuken_ryu = SpecialMove.add_new("Shoryuken", "PUNCH", 1, 2)
tatsu_ryu = SpecialMove.add_new("Tatsumaki Senpukyaku", "KICK", 1, 3)

# Ken (character_id: 2), Combos (combo_id: 1-3)
hadoken_ken = SpecialMove.add_new("Hadoken", "PUNCH", 2, 1)
shoryuken_ken = SpecialMove.add_new("Shoryuken", "PUNCH", 2, 2)
tatsu_ken = SpecialMove.add_new("Tatsumaki Senpukyaku", "KICK", 2, 3)

# Chun-Li (character_id: 3), Combos (combo_id: 4-5)
kicks_chunli = SpecialMove.add_new("Hyakuretsu Kyaku", "KICK", 3, 4)
sbk_chunli = SpecialMove.add_new("Spinning Bird Kick", "KICK", 3, 5)

# Blanka (character_id: 5), Combo (combo_id: 4)
thunder_blanka = SpecialMove.add_new("Electric Thunder", "PUNCH", 5, 4)

print("✅ database.db initialized from schema.sql")
