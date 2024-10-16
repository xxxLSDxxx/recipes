from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def views_recipe(request):
    base=request.GET.get('servings', 'omlet')
    result=int(request.GET.get('kol', 1))
    for i in DATA:
        for j in DATA[i]:
            DATA[i][j]=DATA[i][j]*result
    print(DATA)
    context = {
        'recipe': DATA[base] ,
    }
    return render(request, 'calculator/index.html', context)

def omlet(request):
    
    result=int(request.GET.get('servings', 1))
    for i in DATA:
        for j in DATA[i]:
            DATA[i][j]=DATA[i][j]*result
    print(DATA)
    context = {
        'recipe': DATA['omlet'] ,
    }
    return render(request, 'calculator/index.html', context)

def pasta(request):
    
    result=int(request.GET.get('servings', 1))
    for i in DATA:
        for j in DATA[i]:
            DATA[i][j]=DATA[i][j]*result
    print(DATA)
    context = {
        'recipe': DATA['pasta'] ,
    }
    return render(request, 'calculator/index.html', context)
