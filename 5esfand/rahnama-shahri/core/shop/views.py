from django.shortcuts import render
from django.http import Http404

cities = {
    'Tehran': {
        'image':'tehran.jpg',
        'des':'Tehran is the vibrant capital of Iran and its largest city, home to millions of people and the center of politics, economy, and culture. Walking through Tehran, you’ll see a unique mix of modern architecture and historical landmarks like the Golestan Palace, Azadi Tower, and Milad Tower. The city never sleeps — it’s full of cafes, art galleries, and busy streets that show Iran’s modern life alongside its deep heritage.',
        'det':'Capital city, modern skyline, museums, and bustling bazaar',
    },
    
    'Esfehan': {
        'image':'esfehan.jpg',
        'des':'Isfahan is Iran’s cultural gem, known for its breathtaking Islamic architecture and traditional arts. Famous landmarks like Naqsh-e Jahan Square, Sheikh Lotfollah Mosque, and Si-o-se-pol Bridge make it one of the most beautiful cities in the Middle East. With tree-lined boulevards, cozy tea houses, and a peaceful river view, Isfahan truly captures the spirit of Persian elegance and history — a city where every corner feels like a painting.',
        'det':'Historic bridges, blue-tiled mosques, rich Persian art, and gardens.',
    },
    
    'Tabriz': {
        'image':'tabriz.jpg',
        'des':'Tabriz stands proudly in the northwest of Iran, surrounded by mountains and rich in history. It has long been a center of trade and culture, known for its famous Tabriz carpets and the grand Tabriz Bazaar — one of the world’s oldest covered markets. The city’s cool climate, friendly people, and artistic heritage make it a wonderful place to explore, offering a blend of tradition and modern life with a unique Turkish-Persian flavor.',
        'det':'Trade center, mountain air, carpet craftsmanship, ancient bazaar.',
    },
}



def index(request):
    return render(request, 'shop/index.html', {'cities':cities.items(),'caller': 'home'})

def city_det(request, x):
    item = " ".join(x.split('-'))
    if item in cities:
        return render(request, 'shop/city-det.html', {'city': item, 'details': cities[item],'caller': 'details'})
        
    raise Http404()