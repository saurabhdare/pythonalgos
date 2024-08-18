alien = { 'x' : 10, 'y' : 25, 'speed' : 'medium' }
print(f"Original position: {alien['x']}")

# determine how far the alien moves
if alien['speed'] == 'slow':
    x = 1
elif alien ['speed'] == 'medium':
    x = 2
else:
    # this must be fast alien
    x = 3

alien['x'] = alien['x'] + x
print(f"New position: {alien['x']}")

alien['points'] = 5
print(alien)

del alien['points']
# after delete
print(alien)

favorite = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language = favorite['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# using get to avoid value missing error
point_value = alien.get('points', 'No point value assigned.')
print(point_value)

