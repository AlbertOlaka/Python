guest_list = ['Elon Musk', 'Frank Kafka', 'Fydor Dostoevsky']
print(f'I would like to welcome {guest_list[0]}, to my dinner part at my home on 21st of June')
print(f'I would like to welcome {guest_list[1]}, to my dinner part at my home on 21st of June')
print(f'I would like to welcome {guest_list[2]}, to my dinner part at my home on 21st of June')
print(f'\nUnfortunately, {guest_list[0]}, can not make it to the dinner party')

# Changing Guest List
del guest_list[0]
guest_list.insert(0, 'Slyvia Plath')
print(f'\nI would like to welcome {guest_list[0]}, to my dinner part at my home on 21st of June')
print(f'I would like to welcome {guest_list[1]}, to my dinner part at my home on 21st of June')
print(f'I would like to welcome {guest_list[2]}, to my dinner part at my home on 21st of June')

# More Guests.
print(f'\nGood Afternoon {guest_list[0]}! I have found a bigger dinner table, so more guest would be able to join us for dinner')
print(f'Good Afternoon {guest_list[1]}! I have found a bigger dinner table, so more guest would be able to join us for dinner')
print(f'Good Afternoon {guest_list[2]}! I have found a bigger dinner table, so more guest would be able to join us for dinner')

guest_list.insert(0, 'Christopher Nolan')
guest_list.insert(2, 'J.K. Rowling')
guest_list.append('Keanu Reeves')

print(f'\nI would like to welcome {guest_list[0]}, to my dinner part at my home on 21st of June')
print(f'I would like to welcome {guest_list[1]}, to my dinner part at my home on 21st of June')
print(f'I would like to welcome {guest_list[2]}, to my dinner part at my home on 21st of June')
print(f'I would like to welcome {guest_list[3]}, to my dinner part at my home on 21st of June')
print(f'I would like to welcome {guest_list[4]}, to my dinner part at my home on 21st of June')
print(f'I would like to welcome {guest_list[5]}, to my dinner part at my home on 21st of June')

#Shrinking Guest List
print(f'\nUnfortunately, I can only invite two people for dinner')
removed_guest = guest_list.pop()
print(f'I am so sorry {removed_guest}, but I can only invite two people for dinner')
removed_guest = guest_list.pop(0)
print(f'I am so sorry {removed_guest}, but I can only invite two people for dinner')
removed_guest = guest_list.pop(1)
print(f'I am so sorry {removed_guest}, but I can only invite two people for dinner')
removed_guest = guest_list.pop(2)
print(f'I am so sorry {removed_guest}, but I can only invite two people for dinner')

print(f'\n{guest_list[0]} and {guest_list[1]} are still invited to the dinner party!')
print(len(guest_list))

del guest_list[0:2]
print(f'\n{guest_list}')