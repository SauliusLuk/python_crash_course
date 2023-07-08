# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens_old = [alien_0, alien_1, alien_2]
#
# for alien in aliens_old:
#     print(alien)

aliens = []

# Make 30 green aliens_old.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'

# Show the first 5 aliens_old.
for alien in aliens[:10]:
    print(alien)
print('....')

# Show how many aliens_old have been created.
print(f"Total number of aliens: {len(aliens)}")